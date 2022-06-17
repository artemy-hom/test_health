'''from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget , QApplication , QPushButton ,QLabel , QVBoxLayout
from my_app import *

app = QApplication([])

window = MainWin()
window.show()


window = QWidget()

window.resize(700,400)

line1 = QVBoxLayout()

window.show()

button1 = QPushButton('начать')

text1 = QLabel('Добро пожаловать в программу по определению состояния здоровья.')
text2 = QLabel('Данное приложение позволит вам с помощью теста Руфие\n      провести первичную диагностикувашего здоровия.')


line1.addWidget(text1, alignment = Qt.AlignCenter)
line1.addWidget(text2, alignment = Qt.AlignCenter)

line1.addWidget(button1, alignment = Qt.AlignCenter)


window.setLayout(line1)


app.exec_()
'''