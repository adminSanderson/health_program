from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *


class FinalWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # создаём и настраиваем графические элелементы:
        self.initUI()
        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()

    def initUI(self):
        ''' создает графические элементы '''

        pass

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_x)
        

app = QApplication([])
mw = QApp

