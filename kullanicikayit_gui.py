# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kullanicikayit_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
import mysql.connector
# Veritabanı bağlantısı için sql cümleciği oluşturuldu.
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="cilth_vt"
)
cursor = db.cursor()
class Ui_MainWindow3(QtWidgets.QMainWindow):
    def setupUi3(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 216)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_kayit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kayit.setGeometry(QtCore.QRect(340, 160, 121, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../avatar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_kayit.setIcon(icon1)
        self.btn_kayit.setObjectName("btn_kayit")
        self.btn_kayit.clicked.connect(self.addUser)
        self.btn_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikis.setGeometry(QtCore.QRect(470, 160, 121, 31))
        self.btn_cikis.setObjectName("btn_cikis")
        self.btn_cikis.clicked.connect(QtWidgets.qApp.quit)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 581, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_hdt_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_hdt_2.setObjectName("lbl_hdt_2")
        self.gridLayout_3.addWidget(self.lbl_hdt_2, 4, 0, 1, 1)
        self.lbl_ktel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_ktel.setObjectName("lbl_ktel")
        self.gridLayout_3.addWidget(self.lbl_ktel, 3, 0, 1, 1)
        self.lbl_knick = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_knick.setObjectName("lbl_knick")
        self.gridLayout_3.addWidget(self.lbl_knick, 1, 0, 1, 1)
        self.le_knick = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_knick.setObjectName("le_knick")
        self.gridLayout_3.addWidget(self.le_knick, 1, 2, 1, 1)
        self.lbl_ksifre = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_ksifre.setObjectName("lbl_ksifre")
        self.gridLayout_3.addWidget(self.lbl_ksifre, 2, 0, 1, 1)
        self.le_kad = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_kad.setObjectName("le_kad")
        self.gridLayout_3.addWidget(self.le_kad, 0, 2, 1, 1)
        self.le_ksifre = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_ksifre.setObjectName("le_ksifre")
        self.gridLayout_3.addWidget(self.le_ksifre, 2, 2, 1, 1)
        self.lbl_kad = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_kad.setObjectName("lbl_kad")
        self.gridLayout_3.addWidget(self.lbl_kad, 0, 0, 1, 1)
        self.le_kmail = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_kmail.setObjectName("le_kmail")
        self.gridLayout_3.addWidget(self.le_kmail, 4, 2, 1, 1)
        self.le_ktel = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_ktel.setObjectName("le_ktel")
        self.gridLayout_3.addWidget(self.le_ktel, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addUser(self):
        kad=self.le_kad.text()
        ksifre=self.le_ksifre.text()
        knick=self.le_knick.text()
        kmail=self.le_kmail.text()
        ktel=self.le_ktel.text()
        cursor = db.cursor()
        find_user = ("Select * From kullanici WHERE k_nick=%s")
        cursor.execute(find_user,(knick, ))
        if (len(cursor.fetchall()) > 0):
            QMessageBox.information(self, 'Hata', "Kullanıcı Adı Alınmış!!")
        else:
            insert = "INSERT INTO kullanici(k_adsad,k_sifre,k_nick,k_mail,k_tel) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(insert, (kad, ksifre, knick, kmail, ktel))
            db.commit()
            QMessageBox.information(self, 'BİLGİLENDİRME', "İşlem Başarılı.")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CHTP-Kullanıcı Kayıt"))
        self.btn_kayit.setText(_translate("MainWindow", "ONAYLA"))
        self.btn_cikis.setText(_translate("MainWindow", "İPTAL"))
        self.lbl_hdt_2.setText(_translate("MainWindow", "Mail Adresi :"))
        self.lbl_ktel.setText(_translate("MainWindow", "Telefon :"))
        self.lbl_knick.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.lbl_ksifre.setText(_translate("MainWindow", "Şifre:"))
        self.lbl_kad.setText(_translate("MainWindow", "Ad Soyad"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi3(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

