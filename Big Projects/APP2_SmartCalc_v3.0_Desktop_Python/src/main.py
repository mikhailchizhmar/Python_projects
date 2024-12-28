from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from model import CalcModelMVP
from frontend.view import Ui_MainWindow
from presenter import CalculatorPresenter
import sys


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    model = CalcModelMVP()

    presenter = CalculatorPresenter(ui, model)

    MainWindow.setWindowTitle("SmartCalc_V3")

    MainWindow.show()
    sys.exit(app.exec_())
