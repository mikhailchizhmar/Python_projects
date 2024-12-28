#ifndef SRC_S21_CALC_MODEL_H
#define SRC_S21_CALC_MODEL_H

#define BUFF 1024
#define CNT 100
#define EPS 1e-7

#include <algorithm>
#include <cctype>  // tolower
#include <cmath>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

namespace s21 {
enum Status { ok, err };
class CalcModel {
 public:
  CalcModel() = default;
  ~CalcModel() = default;

//#ifdef __cplusplus
//extern "C" {
//#endif

  void eval_expression();
  enum Status GetStatus() const;
  long double GetResult() const;
  void SetX(const long double x) noexcept;
  void SetInfix(const std::string &infix) noexcept;

//#ifdef __cplusplus
//}
//#endif

 private:
  enum Status create_polish_str();
  enum Status infix_to_polish();
  void expression_clear();
  void lower();
  void remove_spaces();
  void replace_unary_minus();
  void remove_unary_plus();

  void NumberToStack(std::string::iterator &it);
  void CalcSimple(std::string::iterator &it);
  void CalcFunc(std::string::iterator &it);

  void NumberToPostfix(std::string::iterator &it);
  void UnarToPostfix(std::string::iterator &it);
  void BracketsToPostfix(std::string::iterator &it);
  void FunctionToPostfix(std::string::iterator &it);
  void PowToPostfix(std::string::iterator &it);

  inline bool isUnar(std::string::iterator &it) noexcept;
  inline bool isBrackets(std::string::iterator &it) noexcept;
  inline bool isFunction(std::string::iterator &it) noexcept;
  inline bool isOperators(std::string::iterator &it) noexcept;
  inline bool isPow(std::string::iterator &it) noexcept;
  bool isNumber(std::string::iterator &it) noexcept;

  int Priority(char ch) noexcept;
  bool isValid();
  void clear_stack();
  inline char ChangeFunctions(std::string::iterator &it, bool iter = false);
  void PushBackPostfix();

  enum Status status_ = ok;
  std::stack<char> symbol_;
  std::stack<long double> stack_;
  long double x_ = 0;
  long double result_ = 0;
  std::string infix_ = "";
  std::string postfix_;
};

//extern "C" {
#ifdef __cplusplus
extern "C" {
#endif
  s21::CalcModel* CreateCalcModel();
  void DestroyCalcModel(s21::CalcModel* model);
  void SetInfix(s21::CalcModel* model, const char* infix);
  void SetX(s21::CalcModel* model, long double x);
  void EvaluateExpression(s21::CalcModel* model);
  long double GetResult(s21::CalcModel* model);
  int GetStatus(s21::CalcModel* model);
//}
#ifdef __cplusplus
}
#endif
}  // namespace s21

#endif  // SRC_S21_CALC_MODEL_H
