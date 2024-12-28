#include "s21_calc_model.h"

namespace s21 {

void CalcModel::eval_expression() {
  status_ = create_polish_str();
  if (!status_) {
    for (auto it = postfix_.begin(); it != postfix_.end(); ++it) {
      if (*it == ' ') {
        continue;
      } else if (isNumber(it)) {
        NumberToStack(it);
      } else if (isOperators(it)) {
        CalcSimple(it);
      } else {
        CalcFunc(it);
      }
      if (status_ == ok && !stack_.empty()) {
        result_ = stack_.top();
      }
    }
  }
  if (status_ == ok && !stack_.empty()) {
    stack_.pop();
  }

  if (!stack_.empty()) {
    status_ = err;
  }
}

Status CalcModel::create_polish_str() {
  if (!isValid()) return err;
  expression_clear();
  status_ = infix_to_polish();
  return status_;
}

Status CalcModel::infix_to_polish() {
  if (!isValid()) return err;
  clear_stack();
  for (auto it = infix_.begin(); it != infix_.end(); ++it) {
    if (*it == ' ' || *it == '\0') {
      if (infix_.length() == 1) {
        status_ = err;
      }
      continue;
    } else if (isNumber(it)) {
      NumberToPostfix(it);
    } else if (isUnar(it)) {
      UnarToPostfix(it);
    } else if (isBrackets(it)) {
      BracketsToPostfix(it);
    } else if (isFunction(it)) {
      FunctionToPostfix(it);
    } else if (isPow(it)) {
      PowToPostfix(it);
    } else if (isOperators(it)) {
      while (!stack_.empty() && Priority(*it) <= Priority(stack_.top())) {
        PushBackPostfix();
      }
      stack_.push(*it);
    } else {
      status_ = err;
    }
  }
  while (!stack_.empty()) {
    PushBackPostfix();
  }
  if (status_ != ok) {
    status_ = err;
  }
  return status_;
}

void CalcModel::expression_clear() {
  lower();
  remove_spaces();
  replace_unary_minus();
  remove_unary_plus();
}

void CalcModel::lower() {
  std::string ptr_tmp = infix_;
  auto it2 = ptr_tmp.begin();
  for (auto it = infix_.begin(); it != infix_.end(); ++it) {
    if (*it >= 'A' && *it <= 'Z') {
      *it = *it + 32;
    } else {
      *it = *it2;
    }
    it2++;
  }
}

void CalcModel::remove_spaces() {
  int new_len = 0;
  std::string ptr_tmp = infix_;
  auto it2 = ptr_tmp.begin();
  for (auto it = infix_.begin(); it != infix_.end(); ++it) {
    if (*it != ' ') {
      *it2 = *it;
      it2++;
      new_len++;
    }
  }
  ptr_tmp.resize(new_len);
  infix_ = ptr_tmp;
}

void CalcModel::replace_unary_minus() {
  std::string ptr_tmp = infix_;
  for (int i = 0; i <= (int)infix_.length(); i++) {
    ptr_tmp[i] = (infix_[i] == '-') && (i == 0 || infix_[i - 1] == '(' ||
                                        infix_[i - 1] == '^')
                     ? '~'
                     : infix_[i];
  }
  infix_ = ptr_tmp;
}

void CalcModel::remove_unary_plus() {
  int new_len = 0;
  std::string ptr_tmp = infix_;
  auto it = ptr_tmp.begin();
  for (int i = 0; i <= (int)infix_.length(); i++) {
    if ((infix_[i] == '+') &&
        (i == 0 || infix_[i - 1] == '(' || infix_[i - 1] == '^')) {
      continue;
    }
    *it = infix_[i];
    it++;
    new_len++;
  }
  ptr_tmp.resize(new_len);
  infix_ = ptr_tmp;
}

bool CalcModel::isNumber(std::string::iterator &it) noexcept {
  return isdigit(*it) || *it == '.' || *it == ',' || *it == 'e' || *it == 'x' ||
         ((*it == '-' || *it == '+') &&
          (it != infix_.begin() && *(it - 1) == 'e'));
}

bool CalcModel::isUnar(std::string::iterator &it) noexcept {
  return (*it == '-' || *it == '+' || *it == '~') &&
         (it == infix_.begin() || *(it - 1) == '(');
}

bool CalcModel::isBrackets(std::string::iterator &it) noexcept {
  return *it == '(' || *it == ')';
}

bool CalcModel::isOperators(std::string::iterator &it) noexcept {
  return *it == '-' || *it == '+' || *it == '*' || *it == '/' || *it == '%' ||
         *it == '^';
}

bool CalcModel::isFunction(std::string::iterator &it) noexcept {
  char ch = ChangeFunctions(it);
  return ch >= 65 && ch <= 73 && *it != ch;
}

bool CalcModel::isPow(std::string::iterator &it) noexcept { return *it == '^'; }

void CalcModel::NumberToPostfix(std::string::iterator &it) {
  while (isNumber(it)) {
    postfix_.push_back(*it++);
  }
  *it--;
  postfix_.push_back(' ');
}

void CalcModel::UnarToPostfix(std::string::iterator &it) {
  char ch = *it;
  //    while (!stack_.empty() && Priority(ch) <= Priority(stack_.top())) {
  //        PushBackPostfix();
  //    }
  stack_.push(ch);
}

void CalcModel::BracketsToPostfix(std::string::iterator &it) {
  if (*it == '(')
    stack_.push(*it);
  else {
    while (!stack_.empty() && stack_.top() != '(') {
      PushBackPostfix();
    }
    if (!stack_.empty() && stack_.top() == '(') {
      stack_.pop();
    }
    //        else
    //            status_ = err;
  }
}

void CalcModel::PowToPostfix(std::string::iterator &it) {
  while (!stack_.empty() && Priority(*it) < Priority(stack_.top()))
    PushBackPostfix();
  stack_.push(*it);
}

void CalcModel::FunctionToPostfix(std::string::iterator &it) {
  char func_name = ChangeFunctions(it, true);
  //    while (!stack_.empty() && Priority(func_name) <= Priority(stack_.top()))
  //        PushBackPostfix();
  stack_.push(func_name);
}

int CalcModel::Priority(char ch) noexcept {
  if (ch == '+' || ch == '-')
    return 1;
  else if (ch == '*' || ch == '/')
    return 2;
  else if (ch == '^')
    return 3;
  else if ((ch >= 65 && ch <= 74) || ch == '%')
    return 4;
  else if (ch == '~')
    return 5;
  else if (ch == '(')
    return -1;
  return 0;
}

bool CalcModel::isValid() {
  if (infix_ == "" || infix_ == "\0") {
    status_ = err;
    return false;
  }
  int open = 0, closed = 0;
  for (auto it = infix_.begin(); it != infix_.end(); ++it) {
    if (*it == '(') {
      ++open;
    } else if (*it == ')') {
      ++closed;
    }
  }
  if (open != closed) {
    status_ = err;
  }
  return open == closed;
}

void CalcModel::clear_stack() {
  postfix_ = "";
  status_ = ok;
  result_ = 0;
  //    while (!stack_.empty()) {
  //        stack_.pop();
  //    }
}

char CalcModel::ChangeFunctions(std::string::iterator &it, bool iter) {
  std::vector<std::string> func = {"cos",  "sin",  "tan", "acos", "asin",
                                   "atan", "sqrt", "log", "ln"};
  for (int i = 0; i < (int)func.size(); ++i) {
    if (*it == *(func[i].begin()) &&
        (*(it + func[i].size() - 1) == *(func[i].end() - 1)) &&
        (*(it + func[i].size() - 2) == *(func[i].end() - 2))) {
      if (iter) {
        it += func[i].length() - 1;
      }
      return i + 65;
    }
  }
  return *it;
}

void CalcModel::PushBackPostfix() {
  if (!stack_.empty()) {
    postfix_.push_back(stack_.top());
    stack_.pop();
    postfix_.push_back(' ');
  }
}

void CalcModel::NumberToStack(std::string::iterator &it) {
  if (*it == 'x') {
    stack_.push(x_);
  } else {
    std::string digit;
    while (isNumber(it)) digit.push_back(*it++);
    *it--;
    try {
      stack_.push(std::stod(digit));
    } catch (const std::out_of_range &e) {
      status_ = err;
    }
  }
}

void CalcModel::CalcSimple(std::string::iterator &it) {
  long double second_operand = 0, first_operand = 0;
  if (stack_.empty()) {
    status_ = err;
  } else {
    second_operand = stack_.top();
    stack_.pop();
  }
  if (stack_.empty()) {
    status_ = err;
  } else {
    first_operand = stack_.top();
    stack_.pop();
  }
  if (*it == '+') {
    stack_.push(first_operand + second_operand);
  } else if (*it == '-') {
    stack_.push(first_operand - second_operand);
  } else if (*it == '*') {
    stack_.push(first_operand * second_operand);
  } else if (*it == '^') {
    stack_.push(std::pow(first_operand, second_operand));
  } else if (*it == '/') {
    if (second_operand != 0)
      stack_.push(first_operand / second_operand);
    else
      status_ = err;
  } else if (*it == '%') {
    stack_.push(std::fmod(first_operand, second_operand));
  }
}

void CalcModel::CalcFunc(std::string::iterator &it) {
  long double operand = 0;
  if (stack_.empty()) {
    status_ = err;
  } else {
    operand = stack_.top();
    stack_.pop();
  }
  if (*it == 'A') {
    stack_.push(std::cos(operand));
  } else if (*it == 'B') {
    stack_.push(std::sin(operand));
  } else if (*it == 'C') {
    stack_.push(std::tan(operand));
  } else if (*it == 'D') {
    stack_.push(std::acos(operand));
  } else if (*it == 'E') {
    stack_.push(std::asin(operand));
  } else if (*it == 'F') {
    stack_.push(std::atan(operand));
  } else if (*it == 'G') {
    if (operand >= 0) {
      stack_.push(std::sqrt(operand));
    } else
      status_ = err;
  } else if (*it == 'H') {
    if (operand > 0) {
      stack_.push(std::log10(operand));
    } else
      status_ = err;
  } else if (*it == 'I') {
    if (operand > 0) {
      stack_.push(std::log(operand));
    } else
      status_ = err;
  } else if (*it == '~') {
    stack_.push(operand * -1);
  }
}
//extern "C" {
void CalcModel::SetInfix(const std::string &infix) noexcept { infix_ = infix; }
//}
//extern "C" {
void CalcModel::SetX(const long double x) noexcept { x_ = x; }
//}

//extern "C" {
enum Status CalcModel::GetStatus() const { return status_; }
//}

//extern "C" {
long double CalcModel::GetResult() const { return result_; }
//}

}  // namespace s21

extern "C" {
  s21::CalcModel* CalcModel_new() { return new s21::CalcModel(); }
  void CalcModel_delete(s21::CalcModel* obj) { delete obj; }

  void CalcModel_SetInfix(s21::CalcModel* obj, const char* infix) {
    obj->SetInfix(std::string(infix));
  }

  void CalcModel_SetX(s21::CalcModel* obj, const long double x) {
    obj->SetX(x);
  }

  s21::Status CalcModel_GetStatus(const s21::CalcModel* obj) {
    return obj->GetStatus();
  }

  long double CalcModel_GetResult(const s21::CalcModel* obj) {
    return obj->GetResult();
  }

  void CalcModel_EvalExpression(s21::CalcModel* obj) {
    obj->eval_expression();
  }
}