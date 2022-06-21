from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
# проверка типов вводимых значений
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout, QVBoxLayout, QGridLayout,QGroupBox, QRadioButton,QPushButton, QLabel, QListWidget, QLineEdit
from insrt import *


class FinalWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    #def results(self):

    def initUI(self):
        ''' создаёт графические элементы '''
        self.work_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
