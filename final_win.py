from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
# проверка типов вводимых значений
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout, QVBoxLayout, QGridLayout,QGroupBox, QRadioButton,QPushButton, QLabel, QListWidget, QLineEdit
from insrt import *


class FinalWin(QWidget):
    def __init__(self,tresult):
        super().__init__()
        self.tresult = tresult
        self.initUI()
        self.set_appear()
        self.show()



        self.age = int(self.tresult.age)

    '''def tupoe_govo(self):
        if int(self.tresult.age) >= 15:
            if self.health_index2 >=15:
                self.health_stat = 'Низкий'
            elif self.health_index2 >=11 and self.health_index2 <=14.9:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index2 >=6 and self.health_index2 <=10.9:
                self.health_stat = 'Средний'
            elif self.health_index2 >= 0.5 and self.health_index2 <=5.9:
                self.health_stat = 'Выше среднего'
            elif self.health_index2 <0.4:
                self.health_stat = 'Высокий'

        elif int(self.tresult.age) >= 13 and int(self.tresult.age) <=14:
            if self.health_index2 >=16.5:
                self.health_stat = 'Низкий'
            elif self.health_index2 >=12.5 and self.health_index2 <=16.4:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index2 >=7.5 and self.health_index2 <=12.4:
                self.health_stat = 'Средний'
            elif self.health_index2 >= 2 and self.health_index2 <=7.4:
                self.health_stat = 'Выше среднего'
            elif self.health_index2 <1.9:
                self.health_stat = 'Высокий'

        elif int(self.tresult.age) >= 11 and int(self.tresult.age) <=12:
            if self.health_index2 >=18:
                self.health_stat = 'Низкий'
            elif self.health_index2 >=14 and self.health_index2 <=17.9:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index2 >=9 and self.health_index2 <=13.9:
                self.health_stat = 'Средний'
            elif self.health_index2 >= 3.5 and self.health_index2 <=8.9:
                self.health_stat = 'Выше среднего'
            elif self.health_index2 <3.4:
                self.health_stat = 'Высокий'

        elif int(self.tresult.age) >= 9 and int(self.tresult.age) <=10:
            if self.health_index2 >=19.5:
                self.health_stat = 'Низкий'
            elif self.health_index2 >=15.5 and self.health_index2 <=19.4:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index2 >=10.5 and self.health_index2 <=15.4:
                self.health_stat = 'Средний'
            elif self.health_index2 >= 5 and self.health_index2 <=10.4:
                self.health_stat = 'Выше среднего'
            elif self.health_index2 <4.9:
                self.health_stat = 'Высокий'

        elif int(self.tresult.age) >= 7 and int(self.tresult.age) <=8:
            if self.health_index2 >=21:
                self.health_stat = 'Низкий'
            elif self.health_index2 >=17 and self.health_index2 <=20.9:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index2 >=12 and self.health_index2 <=16.9:
                self.health_stat = 'Средний'
            elif self.health_index2 >= 6.5 and self.health_index2 <=11.9:
                self.health_stat = 'Выше среднего'
            elif self.health_index2 <6.4:
                self.health_stat = 'Высокий'
    '''
        
    def initUI(self):
        self.health_index = (4*(float(self.tresult.t1)+float(self.tresult.t2)+float(self.tresult.t3))-200)/10
        ''' создаёт графические элементы '''
        self.work_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index+str(self.health_index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
