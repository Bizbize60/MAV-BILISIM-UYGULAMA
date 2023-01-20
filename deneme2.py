import mysql.connector
import dokuman
from islem1 import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from islem3 import Ui_Form3
from islem2 import Ui_Form2

class payments_debts:
    def __init__(self,company_name):
        self.company_name=company_name
        self.debt=input("Borç?")
        self.payment=input("ALINACAK?")
        sql="INSERT INTO MAVI (sirket, borc , alinacak) VALUES (%s, %s ,%s)"
        val=(self.company_name,self.debt,self.payment)
        mycursor.execute(sql,val)
        mydb.commit()

    def __str__(self):
        return f"Şirket Adı:{self.company_name} Tarih:{self.date} Borç:{self.debt} Alınacak:{self.payment}"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 170, 301, 61))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda:self.clicker())
        self.pushButton.setGeometry(QtCore.QRect(490, 170, 81, 61))
        self.pushButton.setObjectName("pushButton")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, -10, 261, 61))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../../../Downloads/2023-01-19 - 24-49-59 - Mavi İnşaat.png"))
        self.photo.setObjectName("photo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 0, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 130, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.comboBox.addItem("YENİ DOKUMAN")
        self.comboBox.addItem("TÜM İŞLEM GEÇMİŞİ")
        self.comboBox.addItem("TEK ŞİRKETE AİT GEÇMİŞ")
        self.comboBox.addItem("İŞLEM")
        
    def islem1(self): 
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
    def islem2(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.Form)
        self.Form.show()


    def islem3(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form3()
        self.ui.setupUi(self.Form)
        self.Form.show()
   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SEÇ"))
        self.label.setText(_translate("MainWindow", "                                      GÖKMEN ATICI"))
        self.label_2.setText(_translate("MainWindow", "                       MAVİ-MUHASEBE SİSTEMİ"))
        self.label_3.setText(_translate("MainWindow", "İŞLEM"))
    def clicker(self):
        self.label_3.setText(f"SON İŞLEM:{self.comboBox.currentText()}")
        if self.comboBox.currentText()=="YENİ DOKUMAN":
            
            (self.islem1())
        if self.comboBox.currentText()=="TÜM İŞLEM GEÇMİŞİ":
            self.islem2()
        if self.comboBox.currentText()=="TEK ŞİRKETE AİT GEÇMİŞ":
            self.islem3()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="mydatabase"
    )
    mycursor=mydb.cursor()
    mycursor.execute("SHOW TABLES")
    