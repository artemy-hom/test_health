from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget , QApplication , QPushButton ,QLabel , QVBoxLayout
from insrt import  *




class MainWin(QWidget):
    def __init__(self):
        super().__init__()


        self.init_UI()
        #self.connects()
        self.set_apear()
        self.show()


    def set_apear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x,win_y)
        self.resize(win_width,win_height)

    def init_UI(self):
        self.hello_text = QLabel(hi_text)
        self.rules_text = QLabel(rule_text)

        self._next_button = QPushButton(nxt_button, self)

        self.line = QVBoxLayout()

        self.line.addLayout(self.hello_text, alignment = Qt.AlignCenter)
        self.line.addLayout(self.rules_text, alignment = Qt.AlignCenter)
        self.line.addLayout(self._next_button, alignment = Qt.AlignCenter)

#    def connects(self):
#        self._next_button.clicked.connect(self.next_click)

#    def next_click(self):



m_app  =  QApplication([])

mw = MainWin()


m_app.exec_()