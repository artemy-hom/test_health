from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout, QVBoxLayout,QGroupBox, QRadioButton,QPushButton, QLabel, QListWidget, QLineEdit
from insrt import *
from final_win import *

class TestResults():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # создаём и настраиваем графические эелементы:
        self.initUI()
        # устанавливает связи между элементами
        self.connects()
        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        #self.questionnary = AllQuestions()
        #================
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        #================

        self.btn_test2.setStyleSheet("background-color : #017AFF; color : #FFFFFF")
        self.btn_test3.setStyleSheet("background-color : #017AFF; color : #FFFFFF")
        self.btn_test1.setStyleSheet("background-color : #017AFF; color : #FFFFFF")
        self.btn_next.setStyleSheet("background-color : #017AFF; color : #FFFFFF")

        #================

        self.btn_next.setFont(QFont('', 18))

        #================
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)

        self.space1 = QLabel('')
        self.space2 = QLabel('')
        self.space3 = QLabel('')

        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        #================

        #================
        self.line_name = QLineEdit(txt_hintname)

        self.line_age = QLineEdit(txt_hintage)

        self.line_test1 = QLineEdit(txt_hinttest1)

        self.line_test2 = QLineEdit(txt_hinttest2)

        self.line_test3 = QLineEdit(txt_hinttest3)
        #================

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.space3, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.space1, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.space2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)


        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)



        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)
        self.setLayout(self.l_line)
        self.setLayout(self.r_line)

    def next_click(self):
        self.hide()
        self.tresult = TestResults(self.line_age.text(),self.line_test1.text(),self.line_test2.text(),self.line_test3.text())
        self.fwin = FinalWin(self.tresult)


    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_test2)
        self.btn_test3.clicked.connect(self.timer_test3)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x,win_y)
        self.resize(win_width,win_height)
    
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test2(self):
            global time
            time = QTime(0,0,30)
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.timer2Event)
            self.timer2.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer2.stop()

    def timer_test3(self):
            global time
            time = QTime(0,1,0)
            self.timer3 = QTimer()
            self.timer3.timeout.connect(self.timer3Event)
            self.timer3.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer3.stop()
        elif time.toString('hh:mm:ss') >= '00:00:45':
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif time.toString('hh:mm:ss') <= '00:00:15':
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')

