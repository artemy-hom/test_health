from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout, QVBoxLayout,QGroupBox, QRadioButton,QPushButton, QLabel, QListWidget, QLineEdit
from insrt import *


class FinalWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # создаём и настраиваем графические элелементы:
        self.init_UI()
        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_apear()
        # старт:
        self.show()


    def set_apear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x,win_y)
        self.resize(win_width,win_height)

    def init_UI(self):
        self.next_button = QPushButton(nxt_button, self)

        self.ello_text = QLabel(hi_text)
        self.ules_text = QLabel(rule_text)


        self.line1 = QVBoxLayout()
        self.line1.addWidget(self.ello_text, alignment = Qt.AlignCenter)    
        self.line1.addWidget(self.ules_text, alignment = Qt.AlignCenter)
        self.line1.addWidget(self.next_button, alignment = Qt.AlignCenter)
        self.setLayout(self.line)
