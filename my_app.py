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
        #устанавливает связи между элементами
        self.connects()
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()

    def initUI(self):
        ''' создает графические элементы '''
        pass
   
    def next_click(self):
        pass

    def connects(self):
        pass

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        pass

app = QApplication([])
mw = MainWin()

app.exec_()
