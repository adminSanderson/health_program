from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
# проверка типов вводимых значений
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # получаем данные об эксперименте
        self.exp = exp

        # создаём и настраиваем графические элементы:
        self.initUI()

        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()

    def results(self): #self = сам
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 21:
                return txt_res1 #вернуть строку txt_res1
            if self.index < 15 and self.index >= 13:
                return txt_res2
            if self.index < 13 and self.index >= 11:
                return txt_res3
            if self.index < 11 and self.index >= 9:
                return txt_res4
            if self.index < 9 and self.index >= 7:
                return txt_res5
            if self.index < 7:
               self.index = 0
               return "нет данных для такого возраста."

    def initUI(self):
        ''' создаёт графические элементы '''
        self.work_text = QLabel(txt_workheart + str(self.results())) #добавляем текст 'Работоспособность сердца: ' снизу
        self.index_text = QLabel(txt_index + str(self.index)) #добавляем текст "индекс Руфие" по центру

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
