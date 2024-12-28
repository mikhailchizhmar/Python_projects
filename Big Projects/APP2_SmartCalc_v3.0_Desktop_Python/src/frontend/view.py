from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from pyqtgraph import PlotWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QTextOption, QKeyEvent, QDoubleValidator, QFont, QCursor
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
from pyqtgraph import PlotWidget



class Ui_MainWindow(QWidget):

    class Ui_history_widget(object):
        def setupUi(self, history_widget):
            history_widget.setObjectName("history_widget")
            history_widget.resize(400, 300)
            history_widget.setMinimumSize(QtCore.QSize(400, 300))
            history_widget.setMaximumSize(QtCore.QSize(400, 300))
            self.listWidget_hist = QtWidgets.QTableWidget(history_widget)
            self.listWidget_hist.setGeometry(QtCore.QRect(0, 0, 400, 300))
            self.listWidget_hist.setObjectName("listWidget_hist")

            self.retranslateUi(history_widget)
            QtCore.QMetaObject.connectSlotsByName(history_widget)

        def retranslateUi(self, history_widget):
            _translate = QtCore.QCoreApplication.translate
            history_widget.setWindowTitle(_translate("history_widget", "Form"))


    def setupUi(self, MainWindow):
        MainWindow.resize(852, 366)
        MainWindow.setMinimumSize(QtCore.QSize(852, 366))
        MainWindow.setMaximumSize(QtCore.QSize(852, 366))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infix_expression = QtWidgets.QTextEdit(self.centralwidget)
        self.infix_expression.setGeometry(QtCore.QRect(0, 22, 366, 38))
        self.infix_expression.setMaximumSize(QtCore.QSize(366, 38))
        font = QFont()
        font.setPointSize(15)
        self.infix_expression.setFont(font)
        self.infix_expression.viewport().setProperty("cursor", QCursor(QtCore.Qt.IBeamCursor))
        self.infix_expression.setStyleSheet("QTextEdit {\n"
        "    background-color: rgb(70,70,70);\n"
        "    color: white;\n"
        "    border: 1px solid dimgray;\n"
        "    font-size: 15pt;\n"
        "    padding-right: 5px;\n"
        "    padding-left: 5px; \n"
        "    text-align: right;\n"
        "    vertical-align: middle;\n"
        "}\n"
        "")
        self.infix_expression.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.infix_expression.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.infix_expression.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.infix_expression.setReadOnly(True)
        self.infix_expression.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.infix_expression.setObjectName("infix_expression")
        self.label_eq = QtWidgets.QLabel(self.centralwidget)
        self.label_eq.setGeometry(QtCore.QRect(122, 60, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.label_eq.setFont(font)
        self.label_eq.setStyleSheet("QLabel {\n"
        "    background-color: rgb(97,96,96);\n"
        "    color: white;\n"
        "    border: 1px solid dimgray;\n"
        "    font-size: 22pt;\n"
        "}")
        self.label_eq.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eq.setObjectName("label_eq")
        self.label_expression = QtWidgets.QLabel(self.centralwidget)
        self.label_expression.setGeometry(QtCore.QRect(0, 0, 366, 22))
        self.label_expression.setText("")
        self.label_expression.setObjectName("label_expression")
        self.label_max_x = QtWidgets.QLabel(self.centralwidget)
        self.label_max_x.setGeometry(QtCore.QRect(500, 30, 41, 21))
        self.label_max_x.setObjectName("label_max_x")
        self.label_max_y = QtWidgets.QLabel(self.centralwidget)
        self.label_max_y.setGeometry(QtCore.QRect(750, 30, 41, 21))
        self.label_max_y.setObjectName("label_max_y")
        self.label_min_x = QtWidgets.QLabel(self.centralwidget)
        self.label_min_x.setGeometry(QtCore.QRect(390, 30, 41, 21))
        self.label_min_x.setObjectName("label_min_x")
        self.label_min_y = QtWidgets.QLabel(self.centralwidget)
        self.label_min_y.setGeometry(QtCore.QRect(630, 30, 41, 21))
        self.label_min_y.setObjectName("label_min_y")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(122, 315, 61, 51))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(122, 264, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(183, 264, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(244, 264, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(122, 213, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(183, 213, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(244, 213, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(122, 162, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(183, 162, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(244, 162, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_AC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AC.setGeometry(QtCore.QRect(0, 60, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_AC.setFont(font)
        self.pushButton_AC.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.pushButton_E = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_E.setGeometry(QtCore.QRect(244, 315, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_E.setFont(font)
        self.pushButton_E.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_E.setObjectName("pushButton_E")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(183, 315, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("QPushButton {\n"
"    background-color: rgb(128,126,126);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7f1);\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log.setGeometry(QtCore.QRect(61, 315, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_log.setFont(font)
        self.pushButton_log.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_log.setObjectName("pushButton_log")
        self.pushButton_ln = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ln.setGeometry(QtCore.QRect(0, 315, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_ln.setFont(font)
        self.pushButton_ln.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.pushButton_atan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atan.setGeometry(QtCore.QRect(61, 264, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_atan.setFont(font)
        self.pushButton_atan.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_atan.setObjectName("pushButton_atan")
        self.pushButton_tan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tan.setGeometry(QtCore.QRect(0, 264, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_tan.setFont(font)
        self.pushButton_tan.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_tan.setObjectName("pushButton_tan")
        self.pushButton_acos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_acos.setGeometry(QtCore.QRect(61, 213, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_acos.setFont(font)
        self.pushButton_acos.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_acos.setObjectName("pushButton_acos")
        self.pushButton_cos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cos.setGeometry(QtCore.QRect(0, 213, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.pushButton_asin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_asin.setGeometry(QtCore.QRect(61, 162, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_asin.setFont(font)
        self.pushButton_asin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_asin.setObjectName("pushButton_asin")
        self.pushButton_sin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sin.setGeometry(QtCore.QRect(0, 162, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.pushButton_square = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_square.setGeometry(QtCore.QRect(244, 111, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_square.setFont(font)
        self.pushButton_square.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_square.setObjectName("pushButton_square")
        self.pushButton_root = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_root.setGeometry(QtCore.QRect(183, 111, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_root.setFont(font)
        self.pushButton_root.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_close_bracet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close_bracet.setGeometry(QtCore.QRect(122, 111, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_close_bracet.setFont(font)
        self.pushButton_close_bracet.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_close_bracet.setObjectName("pushButton_close_bracet")
        self.pushButton_open_bracet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_bracet.setGeometry(QtCore.QRect(61, 111, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_open_bracet.setFont(font)
        self.pushButton_open_bracet.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_open_bracet.setObjectName("pushButton_open_bracet")
        self.pushButton_mod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mod.setGeometry(QtCore.QRect(0, 111, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_mod.setFont(font)
        self.pushButton_mod.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.pushButton_X = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_X.setGeometry(QtCore.QRect(61, 60, 61, 51))
        font = QFont()
        font.setPointSize(22)
        self.pushButton_X.setFont(font)
        self.pushButton_X.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 22pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_X.setObjectName("pushButton_X")
        self.x_value_for_calc = QtWidgets.QLineEdit(self.centralwidget)
        self.x_value_for_calc.setGeometry(QtCore.QRect(183, 60, 122, 51))
        font = QFont()
        font.setPointSize(15)
        self.x_value_for_calc.setFont(font)
        self.x_value_for_calc.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(70,70,70);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 15pt;\n"
"}\n"
"")
        self.x_value_for_calc.setObjectName("x_value_for_calc")
        self.pushButton_make_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_make_plot.setGeometry(QtCore.QRect(305, 60, 61, 51))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_make_plot.setFont(font)
        self.pushButton_make_plot.setStyleSheet("QPushButton {\n"
"    background-color: rgb(97,96,96);\n"
"    color: white;\n"
"    border: 1px solid dimgray;\n"
"    font-size: 15pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_make_plot.setObjectName("pushButton_make_plot")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(305, 111, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(305, 162, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(305, 213, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(305, 264, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(305, 315, 61, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    font-size: 24pt;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0,  y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.xMin = QtWidgets.QLineEdit(self.centralwidget)
        self.xMin.setGeometry(QtCore.QRect(430, 30, 51, 21))
        self.xMin.setObjectName("xMin")
        self.xMax = QtWidgets.QLineEdit(self.centralwidget)
        self.xMax.setGeometry(QtCore.QRect(540, 30, 51, 21))
        self.xMax.setObjectName("xMax")
        self.yMin = QtWidgets.QLineEdit(self.centralwidget)
        self.yMin.setGeometry(QtCore.QRect(670, 30, 51, 21))
        self.yMin.setObjectName("yMin")
        self.yMax = QtWidgets.QLineEdit(self.centralwidget)
        self.yMax.setGeometry(QtCore.QRect(790, 30, 51, 21))
        self.yMax.setObjectName("yMax")
        self.widget_plot = PlotWidget(self.centralwidget)
        self.widget_plot.setGeometry(QtCore.QRect(380, 60, 471, 305))
        self.widget_plot.setObjectName("widget_plot")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 852, 24))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.history = QtWidgets.QMenu(self.menuBar)
        self.history.setObjectName("history")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.show_hist = QtWidgets.QAction(MainWindow)
        self.show_hist.setObjectName("show_hist")
        self.delete_hist = QtWidgets.QAction(MainWindow)
        self.delete_hist.setObjectName("delete_hist")
        self.menu.addAction(self.action)
        self.history.addAction(self.show_hist)
        self.history.addAction(self.delete_hist)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.history.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_eq.setText(_translate("MainWindow", "="))
        self.label_max_x.setText(_translate("MainWindow", "max_x"))
        self.label_max_y.setText(_translate("MainWindow", "max_y"))
        self.label_min_x.setText(_translate("MainWindow", "min_x"))
        self.label_min_y.setText(_translate("MainWindow", "min_y"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_AC.setText(_translate("MainWindow", "AC"))
        self.pushButton_E.setText(_translate("MainWindow", "e"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_log.setText(_translate("MainWindow", "log"))
        self.pushButton_ln.setText(_translate("MainWindow", "ln"))
        self.pushButton_atan.setText(_translate("MainWindow", "atan"))
        self.pushButton_tan.setText(_translate("MainWindow", "tan"))
        self.pushButton_acos.setText(_translate("MainWindow", "acos"))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))
        self.pushButton_asin.setText(_translate("MainWindow", "asin"))
        self.pushButton_sin.setText(_translate("MainWindow", "sin"))
        self.pushButton_square.setText(_translate("MainWindow", "^"))
        self.pushButton_root.setText(_translate("MainWindow", "sqrt"))
        self.pushButton_close_bracet.setText(_translate("MainWindow", ")"))
        self.pushButton_open_bracet.setText(_translate("MainWindow", "("))
        self.pushButton_mod.setText(_translate("MainWindow", "mod"))
        self.pushButton_X.setText(_translate("MainWindow", "X"))
        self.pushButton_make_plot.setText(_translate("MainWindow", "plot"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_mul.setText(_translate("MainWindow", "×"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.xMin.setText(_translate("MainWindow", "-10"))
        self.xMax.setText(_translate("MainWindow", "10"))
        self.yMin.setText(_translate("MainWindow", "-10"))
        self.yMax.setText(_translate("MainWindow", "10"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.history.setTitle(_translate("MainWindow", "История"))
        self.action.setText(_translate("MainWindow", "О проекте"))
        self.show_hist.setText(_translate("MainWindow", "Посмотреть историю"))
        self.delete_hist.setText(_translate("MainWindow", "Удалить историю"))


