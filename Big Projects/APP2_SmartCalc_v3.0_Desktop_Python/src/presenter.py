from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QTextCursor, QTextOption, QKeyEvent, QDoubleValidator, QRegularExpressionValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import webbrowser
import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class CalculatorPresenter:
    def __init__(self, ui, model):
        self.ui = ui
        self.model = model

        self.add_functions()
        self.set_text_to_out("0")
        self.kStep_ = 0.1  # Шаг для итераций
        # Векторы для хранения значений X и Y
        self.x_vector_ = []
        self.y_vector_ = []
        self.x_begin_ = -20.0
        self.x_end_ = 20.0
        self.y_begin_ = -20.0
        self.y_end_ = 20.0

        # Отключение фокуса на Mac
        self.ui.infix_expression.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.ui.x_value_for_calc.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.ui.xMin.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.ui.xMax.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.ui.yMin.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.ui.yMax.setAttribute(Qt.WA_MacShowFocusRect, 0)

        # Настройка осей графика
        self.ui.widget_plot.getPlotItem().setLabel('bottom', 'x')
        self.ui.widget_plot.getPlotItem().setLabel('left', 'y')

        # Установка начального диапазона для осей графика
        x_min, x_max = -10, 10
        y_min, y_max = -10, 10
        if x_min < x_max and y_min < y_max:
            self.ui.widget_plot.setXRange(x_min, x_max)
            self.ui.widget_plot.setYRange(y_min, y_max)
            self.ui.widget_plot.replot()

        # Установка валидаторов для ввода чисел
        double_validator = QDoubleValidator(-1000000.0, 1000000.0, 7)
        self.ui.xMin.setValidator(double_validator)
        self.ui.xMax.setValidator(double_validator)
        self.ui.yMin.setValidator(double_validator)
        self.ui.yMax.setValidator(double_validator)
        self.ui.x_value_for_calc.setValidator(double_validator)

        # Установка фокуса на поле ввода
        self.ui.infix_expression.setFocus()

        # Лимиты для графика (чтобы пользователь не мог сам двигать)
        self.ui.widget_plot.setMouseEnabled(x=False, y=False)

        self.history_file = self.history_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.json")
        self.history = self.load_history()

    def add_functions(self):
        self.ui.pushButton_0.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_0.text()))
        self.ui.pushButton_1.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_1.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_9.text()))
        self.ui.pushButton_X.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_X.text()))
        self.ui.pushButton_E.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_E.text()))
        self.ui.pushButton_dot.clicked.connect(lambda: self.DigitsNum(self.ui.pushButton_dot.text()))

        self.ui.pushButton_sin.clicked.connect(lambda: self.Function(self.ui.pushButton_sin.text()))
        self.ui.pushButton_asin.clicked.connect(lambda: self.Function(self.ui.pushButton_asin.text()))
        self.ui.pushButton_cos.clicked.connect(lambda: self.Function(self.ui.pushButton_cos.text()))
        self.ui.pushButton_acos.clicked.connect(lambda: self.Function(self.ui.pushButton_acos.text()))
        self.ui.pushButton_tan.clicked.connect(lambda: self.Function(self.ui.pushButton_tan.text()))
        self.ui.pushButton_atan.clicked.connect(lambda: self.Function(self.ui.pushButton_atan.text()))
        self.ui.pushButton_ln.clicked.connect(lambda: self.Function(self.ui.pushButton_ln.text()))
        self.ui.pushButton_log.clicked.connect(lambda: self.Function(self.ui.pushButton_log.text()))
        self.ui.pushButton_root.clicked.connect(lambda: self.Function(self.ui.pushButton_root.text()))

        self.ui.pushButton_div.clicked.connect(lambda: self.Operators(self.ui.pushButton_div.text()))
        self.ui.pushButton_mul.clicked.connect(lambda: self.Operators(self.ui.pushButton_mul.text()))
        self.ui.pushButton_minus.clicked.connect(lambda: self.Operators(self.ui.pushButton_minus.text()))
        self.ui.pushButton_plus.clicked.connect(lambda: self.Operators(self.ui.pushButton_plus.text()))
        self.ui.pushButton_mod.clicked.connect(lambda: self.Operators(self.ui.pushButton_mod.text()))
        self.ui.pushButton_square.clicked.connect(lambda: self.Operators(self.ui.pushButton_square.text()))

        self.ui.pushButton_open_bracet.clicked.connect(lambda: self.Brackets(self.ui.pushButton_open_bracet.text()))
        self.ui.pushButton_close_bracet.clicked.connect(lambda: self.Brackets(self.ui.pushButton_close_bracet.text()))

        self.ui.pushButton_AC.clicked.connect(lambda: self.remove_ac())
        self.ui.pushButton_equal.clicked.connect(lambda: self.show_res(self.ui.pushButton_equal.text()))

        self.ui.pushButton_make_plot.clicked.connect(lambda: self.plot_graph())

        self.ui.xMin.editingFinished.connect(lambda: self.axis_edited())
        self.ui.xMax.editingFinished.connect(lambda: self.axis_edited())
        self.ui.yMin.editingFinished.connect(lambda: self.axis_edited())
        self.ui.yMax.editingFinished.connect(lambda: self.axis_edited())

        self.ui.action.triggered.connect(self.open_about_page)
        self.ui.delete_hist.triggered.connect(lambda: self.clear_history())
        self.ui.show_hist.triggered.connect(lambda: self.show_history())
        self.ui.delete_hist.triggered.connect(lambda: self.clear_history())

    def open_about_page(self):
        app_dir = os.path.dirname(os.path.abspath(__file__))
        index_path = os.path.join(app_dir, "frontend", "index.html")
        webbrowser.open("file://" + index_path)

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                return json.load(file)
        return []

    def save_history(self):
        with open(self.history_file, "w") as file:
            json.dump(self.history, file)

    def add_operation(self, operation, result):
        self.history.append({"operation": operation, "result": result})
        self.save_history()

    def clear_history(self):
        self.history = []
        self.save_history()

    def get_history(self):
        return self.history

    def open_json_file(self):
        with open(self.history_file, "r") as file:
            json_data = json.load(file)
            self.display_json(json_data)

    def show_history(self):
        self.history_widget = QtWidgets.QWidget()
        self.ui_history = self.ui.Ui_history_widget()
        self.ui_history.setupUi(self.history_widget)

#         # Заполнение истории
        self.ui_history.listWidget_hist.setRowCount(len(self.history))
        self.ui_history.listWidget_hist.setColumnCount(2)
        self.ui_history.listWidget_hist.setHorizontalHeaderLabels(['Operation', 'Result'])
        for row, entry in enumerate(self.history):
            self.ui_history.listWidget_hist.setItem(row, 0, QtWidgets.QTableWidgetItem(entry["operation"]))
            self.ui_history.listWidget_hist.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry["result"])))

        # Добавление обработчика кликов по элементам таблицы
        self.ui_history.listWidget_hist.cellClicked.connect(self.insert_history_item)

        self.history_widget.show()

    def insert_history_item(self, row, column):
        # Получение текста операции из первой колонки выбранной строки
        operation = self.ui_history.listWidget_hist.item(row, 0).text()
        # Вставка текста операции в infix_expression
        self.set_text_to_out(operation)
#         self.ui.infix_expression.setPlainText(operation)

    def write_number(self, number):
        self.ui.infix_expression.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.ui.x_value_for_calc.setAttribute(Qt.WA_MacShowFocusRect, 0)

        if self.ui.infix_expression.toPlainText() == "0":
            self.ui.infix_expression.setText(number)
        else:
            self.ui.infix_expression.setText(self.ui.infix_expression.toPlainText() + number)

    def DigitsNum(self, button):
        current_text = self.ui.infix_expression.toPlainText()
        if self.isNothingStr(current_text) or current_text == "+":
            current_text = ""
        if button == "X":
            self.SetTextX(current_text)
        elif button == "e":
            self.SetTextE(current_text)
        elif button == ".":
            self.SetTextDot(current_text)
        else:
            self.SetTextDigits(current_text, button)

    def Function(self, button_text):
        current_text = self.ui.infix_expression.toPlainText()

        if self.isNothingStr(current_text):
            current_text = ""

        if not current_text:
            self.set_text_to_out(button_text + "(")
        elif (len(current_text) > 1 and current_text[-1].isdigit()) or current_text.endswith('x'):
            self.set_text_to_out(current_text + '*' + button_text + "(")
        elif self.isOperator(current_text[-1]):
            self.set_text_to_out(current_text + "(" + button_text + "(")
        else:
            self.set_text_to_out(current_text + button_text + "(")

    def SetTextX(self, current_text):
        if self.isNothingStr(current_text) or current_text == "+":
            current_text = ""

        if not current_text:
            self.set_text_to_out("x")
        elif current_text[-1].isdigit() or current_text[-1] == ')' or current_text[-1] == 'x':
            self.set_text_to_out(current_text + "*x")
        elif 'e' not in self.GetLastNumber(current_text):
            self.set_text_to_out(current_text + "x")

    def SetTextE(self, current_text):
        last_number = self.GetLastNumber(current_text)
        if current_text and current_text[-1].isdigit() and 'e' not in last_number:
            self.set_text_to_out(current_text + "e")

    def SetTextDot(self, current_text):
        if not current_text or self.isOperator(current_text[-1]) or current_text.endswith('('):
            self.set_text_to_out(current_text + "0.")
        else:
            last_number = self.GetLastNumber(current_text)
            if '.' not in last_number and 'e' not in last_number:
                self.set_text_to_out(current_text + ".")

    def SetTextDigits(self, current_text, button_text):
        if self.isNothingStr(current_text) or current_text == "+":
            current_text = ""

        if current_text.endswith(')') or current_text.endswith('x'):
            self.set_text_to_out(current_text + "*" + button_text)
        elif button_text == "0" and current_text.endswith('('):
            self.set_text_to_out(current_text + button_text + ".")
        elif (current_text.endswith('+') and len(current_text) >= 2 and
              current_text[-2] == '(') or current_text == "+":
            current_text = current_text[:-1]
            self.set_text_to_out(current_text + button_text)
        else:
            self.set_text_to_out(current_text + button_text)

    def GetLastNumber(self, current_text):
        last_number_start = -1
        for i in range(len(current_text) - 1, -1, -1):
            ch = current_text[i]
            if ch.isdigit() or ch == '.' or ch == 'e' or (ch == '-' and i > 0 and current_text[i - 1] == 'e'):
                last_number_start = i
            else:
                break
        if last_number_start >= 0:
            return current_text[last_number_start:]
        return ""

    def isNothingStr(self, current_text):
        return not current_text or current_text == "0" or current_text == "Error" or current_text.endswith("\u221E")

    def isOperator(self, ch):
        operators = {'+', '-', '*', '/', '^', '%'}
        return ch in operators

    def Operators(self, button_text):
        current_text = self.ui.infix_expression.toPlainText()

        # Замена текста кнопки на соответствующий оператор
        if button_text == "×":
            button_text = '*'
        elif button_text == "÷":
            button_text = '/'
        elif button_text == "mod":
            button_text = '%'

        self.SetTextOperator(current_text, button_text)

    def SetTextOperator(self, current_text, button_text):
        if self.isNothingStr(current_text):
            current_text = ""
        elif self.isOperator(current_text[-1]) or current_text[-1] == '.':
            current_text = current_text[:-1]

        if not current_text or current_text.endswith('(') or current_text.endswith('e'):
            if button_text in ("+", "-"):
                self.set_text_to_out(current_text + button_text)
        else:
            if current_text[-1].isdigit() or current_text.endswith('x') or current_text.endswith(')'):
                self.set_text_to_out(current_text + button_text)

    def axis_edited(self):
        try:
            x_min = float(self.ui.xMin.text().replace(",", "."))
            x_max = float(self.ui.xMax.text().replace(",", "."))
            y_min = float(self.ui.yMin.text().replace(",", "."))
            y_max = float(self.ui.yMax.text().replace(",", "."))
        except ValueError:
            QMessageBox.information(self.ui, "ERROR", "Set domain & codomain correctly")
            return

        if x_min < x_max and y_min < y_max:
            self.ui.widget_plot.setXRange(x_min, x_max)
            self.ui.widget_plot.setYRange(y_min, y_max)
            self.ui.widget_plot.replot()
        self.plot_graph()

    def remove_ac(self):
        self.set_text_to_out("0")

    def set_text_to_out(self, string):
        self.ui.infix_expression.setText(string)
        self.ui.infix_expression.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        cursor = self.ui.infix_expression.textCursor()

        cursor.movePosition(QTextCursor.End)
        self.ui.infix_expression.setTextCursor(cursor)
        self.ui.infix_expression.setWordWrapMode(QTextOption.NoWrap)
        self.ui.infix_expression.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def Brackets(self, button_text):
        current_text = self.ui.infix_expression.toPlainText()

        if self.isNothingStr(current_text) or current_text == "+":
            current_text = ""

        if button_text == "(":
            self.SetTextOpenBrackets(current_text)
        elif button_text == ")":
            self.SetTextClosedBrackets(current_text)

    def SetTextOpenBrackets(self, current_text):
        if self.isNothingStr(current_text) or current_text == "+":
            current_text = ""

        if not current_text:
            self.set_text_to_out("(")
        elif self.isOperator(current_text[-1]) or current_text[-1] == '(':
            self.set_text_to_out(current_text + '(')
        elif not current_text.endswith('('):
            self.set_text_to_out(current_text + "*(")

    def SetTextClosedBrackets(self, current_text):
        if (current_text.count('(') > current_text.count(')') and
            not current_text.endswith('(') and
            (current_text[-1].isdigit() or current_text.endswith('x') or
             current_text.endswith(')'))):
            self.set_text_to_out(current_text + ')')

    def chop_zero(self, result):
        # Преобразование числа в строку с фиксированной точностью до 6 знаков после запятой
        res_string = f"{result:.6f}"

        # Удаление конечных нулей
        res_string = res_string.rstrip('0')

        # Удаление конечной точки, если она есть
        if res_string.endswith('.') or res_string.endswith(','):
            res_string = res_string[:-1]

        return res_string

    def show_res(self, button_text):
        if button_text == "=":
            operation = self.ui.infix_expression.toPlainText()
            self.calculate()
            result = self.ui.infix_expression.toPlainText()
            self.add_operation(operation, result)
        elif button_text == "PLOT":
            self.plot_graph()

    def calculate(self):
        current_text = self.add_close_brackets()
        x_value_convert = False
        try:
            x_value = float(self.ui.x_value_for_calc.text())
            x_value_convert = True
        except ValueError:
            x_value = 0

        count_x = current_text.count('x')

        if (count_x == 0 and not x_value_convert) or (count_x > 0 and x_value_convert) or len(current_text) <= 255:
            self.model.set_expression(current_text, x_value)
            self.model.calculate()

            if self.model.get_status() == "ok":
                result = self.model.get_result()
                result_text = self.chop_zero(result)
                self.set_text_to_out(result_text)

                infix_text = self.ui.infix_expression.toPlainText()
                if infix_text.startswith("nan"):
                    self.set_text_to_out("Error")
                elif infix_text.endswith("-inf"):
                    self.set_text_to_out("-∞")
                elif infix_text.endswith("inf"):
                    self.set_text_to_out("∞")
            else:
                self.set_text_to_out("Error")
        elif count_x > 0 and not x_value_convert:
            QMessageBox.information(self.ui, "ERROR", "Set value of x correctly")
        else:
            self.set_text_to_out("Error")

    def add_close_brackets(self):
        current_text = self.ui.infix_expression.toPlainText()
        # Подсчёт количества открывающих и закрывающих скобок
        open_brackets_count = current_text.count('(')
        close_brackets_count = current_text.count(')')

        # Добавление закрывающих скобок, если необходимо
        while open_brackets_count > close_brackets_count and \
              not current_text.endswith('('):
            current_text += ')'
            close_brackets_count += 1

        return current_text

    def plot_graph(self):
        current_text = self.add_close_brackets()
        self.set_text_to_out(current_text)
        x_value_str = self.ui.x_value_for_calc.text()
        self.plot(current_text, x_value_str)

    def chop_text(self, current_text):
        if len(current_text) > 1:
            current_text = current_text[:-1]
            while (current_text and
                   ((ord(current_text[-1]) >= 97 and
                     ord(current_text[-1]) <= 122 and
                     current_text[-1] != 'x') or
                    current_text.endswith('E'))):
                current_text = current_text[:-1]
            self.set_text_to_out(current_text)
        else:
            self.set_text_to_out("0")

    def plot(self, expression, x_value_str):
        self.x_vector_.clear()
        self.y_vector_.clear()
        self.ui.widget_plot.clear()

        try:
            x_begin_ = float(self.ui.xMin.text())
            x_end_ = float(self.ui.xMax.text())
            y_begin_ = float(self.ui.yMin.text())
            y_end_ = float(self.ui.yMax.text())
        except ValueError:
            QMessageBox.information(self.ui, "ERROR", "Set domain & codomain correctly")
            return

        if x_begin_ < -1000000 or x_end_ > 1000000 or y_begin_ < -1000000 or y_end_ > 1000000:
            error = "Set parameters in the range from -1000000 to 1000000"
            QMessageBox.information(self.ui, "ERROR", error)
            return

        try:
            x_value = float(x_value_str)
            convert_x_value_status = True
        except ValueError:
            x_value = None
            convert_x_value_status = False

        if convert_x_value_status:
            x_cord_ = x_begin_
            while x_cord_ <= x_end_:
                self.model.set_expression(expression, x_cord_)
                self.model.calculate()
                y_cord_ = self.model.get_result()

                if y_begin_ <= y_cord_ <= y_end_ and self.model.get_status() == "ok":
                    self.x_vector_.append(x_value)
                    self.y_vector_.append(y_cord_)

                x_cord_ += self.kStep_
        else:
            x_cord_ = x_begin_
            while x_cord_ <= x_end_:
                self.model.set_expression(expression, x_cord_)
                self.model.calculate()
                y_cord_ = self.model.get_result()

                if y_begin_ <= y_cord_ <= y_end_ and self.model.get_status() == "ok":
                    self.x_vector_.append(x_cord_)
                    self.y_vector_.append(y_cord_)

                x_cord_ += self.kStep_

        pen = pg.mkPen(color=(71, 86, 121), width=2)
        self.ui.widget_plot.plot(self.x_vector_, self.y_vector_, pen=pen)

        self.ui.widget_plot.setRange(xRange=(x_begin_, x_end_), yRange=(y_begin_, y_end_))
        self.ui.widget_plot.showGrid(x=True, y=True)

        # Вызов обновления отображения графика
        self.ui.widget_plot.getPlotItem().replot()
