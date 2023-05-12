import sys
from tkinter import W
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("FrisApple")
        self.setGeometry(200, 200, 400, 400)
        self.setWindowIcon(QIcon("code.png"))
        self.setToolTip('my tooltip')
        self.initGUI()
        
    def initGUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50,30)
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,70)
        
        self.lbl_Resut = QtWidgets.QLabel(self)
        self.lbl_Resut.setText("Sonuç")
        self.lbl_Resut.resize(300, 50)
        self.lbl_Resut.move(150, 130)
        
        
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)
        self.txt_name.resize(200,32)
        
        self.txt_suname = QtWidgets.QLineEdit(self)
        self.txt_suname.move(150, 70)
        self.txt_suname.resize(200,32)
        
        self.btn_Save = QtWidgets.QPushButton(self)
        self.btn_Save.setText("Kaydet")
        self.btn_Save.move(150, 110)
        self.btn_Save.clicked.connect(self.clicked) 
        
    def clicked(self):
        # print('Botuna Tıklandı: '+self.txt_name.text())
        # self.lbl_Resut.setText("ad: "+self.txt_name.text()+" Soyad: "+self.txt_suname.text())
        toplama = int(self.txt_name.text())
        toplama1 = int(self.txt_suname.text())
        self.lbl_Resut.setText(f"topladı: {toplama+toplama1}")
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()