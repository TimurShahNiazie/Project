from PyQt6.QtWidgets import *
import formulas

import gui
from gui import *
import math
import sys


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None :
        """
        Establishes the final GUI that the main.py program runs
        """

        super().__init__()
        self.setupUi(self)
        self.Error1.hide()
        self.Error2.hide()
        self.Answer.hide()
        self.multi_2.clicked.connect(self.sumbit)
        self.Clear.clicked.connect(self.clearIT)

    def sumbit(self) -> None:
        """
        When the user clicks the equals button, this will trigger,
        read the inputs, do the math, and return the answer unless
        an error occurs

        """
        try:
            self.Error1.hide()
            self.Error2.hide()
            self.Answer.hide()
            num1 = float(self.lineEdit.text())
            num2 = float(self.lineEdit_2.text())
            val = [num1, num2]
            if self.radioButton.isChecked():
                addition = formulas.add(val)
                self.Answer.setText(f'{addition}')
                self.Answer.show()
            elif self.radioButton_2.isChecked():
                subtract = formulas.subtract(val)
                self.Answer.setText(f'{subtract}')
                self.Answer.show()
            elif self.radioButton_3.isChecked():
                divide = formulas.divide(val)
                self.Answer.setText(f'{divide}')
                self.Answer.show()
            elif self.radioButton_4.isChecked():
                multi = formulas.multiply(val)
                self.Answer.setText(f'{multi}')
                self.Answer.show()
        except ZeroDivisionError:
            self.Error1.hide()
            self.Error2.show()
            self.Answer.hide()

        except ValueError:
            self.Error2.hide()
            self.Error1.show()
            self.Answer.hide()

    def clearIT(self) -> None:
        """
        clears the GUI of all user inputs
        """
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.Error2.hide()
        self.Error1.hide()
        self.Answer.hide()



