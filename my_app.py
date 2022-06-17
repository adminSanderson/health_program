from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()

        # создаём и настраиваем графические эелементы:
        self.initUI()
        # устанавливает связи между элементами

        self.connects()
        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()

    def initUI(self):
        ''' создает графические элементы '''
        self.btn_next = QPushButton(txt_next)
        self.hello_next = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_vertical = QVBoxLayout()
        self.layout_vertical.adWidget(self.btn_next, alignment=Qt.AligCenter)
        self.layout_vertical.adWidget(self.hello_next, alignment=Qt.AligLeft)
        self.layout_vertical.adWidget(self.instruction, alignment=Qt.AligLeft)

    def next_click(self):
        pass

    def connects(self):
        pass

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])

mw = MainWin()

app.exec_()
