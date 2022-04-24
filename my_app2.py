from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout 
from random import randint
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Приложение')
main_win.move(900, 100)
main_win.resize(400, 200)

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

text1 = QLabel('Python')
text2 = QLabel('PHP')
text3 = QLabel('C')
text4 = QLabel('C++')
text5 = QLabel('C#')
text6 = QLabel('GODOT')

h_line1.addWidget(text1, alignment=Qt.AlignCenter)
h_line2.addWidget(text2, alignment=Qt.AlignCenter)
h_line3.addWidget(text3, alignment=Qt.AlignCenter)
h_line2.addWidget(text4, alignment=Qt.AlignCenter)
h_line1.addWidget(text5, alignment=Qt.AlignCenter)
h_line3.addWidget(text6, alignment=Qt.AlignCenter)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

main_win.setLayout(v_line)
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
main_win.show()
app.exec_()
