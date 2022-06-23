from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
# проверка типов вводимых значений
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout, QVBoxLayout, QGridLayout,QGroupBox, QRadioButton,QPushButton, QLabel, QListWidget, QLineEdit
from insrt import *


class FinalWin(QWidget):
    def __init__(self,tresult):
        super().__init__()
        self.tresult = tresult
        self.age = int(self.tresult.age)
        self.health_index = (4*(float(self.tresult.t1)+float(self.tresult.t2)+float(self.tresult.t3))-200)/10
        self.tupoe_govno()
        self.initUI()
        self.set_appear()
        self.show()
        

    def  all_variables(self):
        print(self.age)



    def tupoe_govno(self):
        if self.age >= 15:
            if self.health_index >=15:
                self.health_stat = 'Низкий'
            elif self.health_index >=11 and self.health_index <=14.9:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index >=6 and self.health_index <=10.9:
                self.health_stat = 'Средний'
            elif self.health_index >= 0.5 and self.health_index <=5.9:
                self.health_stat = 'Выше среднего'
            elif self.health_index <0.4:
                self.health_stat = 'Высокий'

        elif self.age >= 13 and self.age <=14:
            if self.health_index >=16.5:
                self.health_stat = 'Низкий'
            elif self.health_index >=12.5 and self.health_index <=16.4:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index >=7.5 and self.health_index <=12.4:
                self.health_stat = 'Средний'
            elif self.health_index >= 2 and self.health_index <=7.4:
                self.health_stat = 'Выше среднего'
            elif self.health_index <1.9:
                self.health_stat = 'Высокий'

        elif self.age >= 11 and self.age <=12:
            if self.health_index >=18:
                self.health_stat = 'Низкий'
            elif self.health_index >=14 and self.health_index <=17.9:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index >=9 and self.health_index <=13.9:
                self.health_stat = 'Средний'
            elif self.health_index >= 3.5 and self.health_index <=8.9:
                self.health_stat = 'Выше среднего'
            elif self.health_index <3.4:
                self.health_stat = 'Высокий'

        elif self.age >= 9 and self.age <=10:
            if self.health_index >=19.5:
                self.health_stat = 'Низкий'
            elif self.health_index >=15.5 and self.health_index <=19.4:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index >=10.5 and self.health_index <=15.4:
                self.health_stat = 'Средний'
            elif self.health_index >= 5 and self.health_index <=10.4:
                self.health_stat = 'Выше среднего'
            elif self.health_index <4.9:
                self.health_stat = 'Высокий'

        elif self.age >= 7 and self.age <=8:
            if self.health_index >=21:
                self.health_stat = 'Низкий'
            elif self.health_index >=17 and self.health_index <=20.9:
                self.health_stat = 'Удовлетворительный'
            elif self.health_index >=12 and self.health_index <=16.9:
                self.health_stat = 'Средний'
            elif self.health_index >= 6.5 and self.health_index <=11.9:
                self.health_stat = 'Выше среднего'
            elif self.health_index <6.4:
                self.health_stat = 'Высокий'
    
        
    def initUI(self):
        
        ''' создаёт графические элементы '''
        self.work_text = QLabel(txt_workheart+self.health_stat)
        self.index_text = QLabel(txt_index+str(self.health_index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
