# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\girisekrani_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# 2.sayfa için kaynak kod import edildi.
# Veritabanı ve Arayüz için gerekli importlar yapıldı.
from girisekrani_gui3 import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLineEdit
import mysql.connector

# Veritabanı bağlantısı için sql cümleciği oluşturuldu.
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="cilth_vt"
)
cursor = db.cursor()
class Ui_MainWindow(QMainWindow):
    # Kullanici adi veya şifre hatalı girildiğinde kullanılacak olan messagebox fonksiyonu
    def hata_mesaji(self):
        QMessageBox.warning(self,"Hata", "Kullanici Adi veya Parola Hatalı!!")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # Mesaj penceresinin başlık kısmındaki ikonu heartbeat olarak ayarlandı.
        QMessageBox.setWindowIcon(self,icon)
    #Giriş Ekrani Fonksiyonu
    # Girilen kullanici adı ve sifreyi veritabanından sorgular,
    # k_ad ve k_sifre doğru ise if bloğuna girerek 2.sayfanın açılmasını sağlar.
    # değilse else bloğundaki hata mesajını çağırır.
    def login(self):
      # k_ad/k_sfire lineedit'ten alınan verileri sorguya gönderir.
      k_ad=self.le_kad.text()
      k_sifre=self.le_ksifre.text()
      find_user = ("Select * From kullanici WHERE k_adsad=%s AND k_sifre=%s")
      cursor.execute(find_user,(k_ad, k_sifre))
      if (len(cursor.fetchall())> 0):
          self.ekran2()
      else:
           self.hata_mesaji()

    # 2.Sayfanın açılabilmesi için import edilen girisekrani_gui3.py dosyasını çalıştıran metot.
    # Ui_MainWindow1 import edilen ikinci sayfaki class ismi.
    def ekran2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()
    #Giriş Ekranını Çalıştıran temel fonksiyon.
    def kullaniciEklemeEkrani(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi3(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 303)
        # MainWindow.setStyleSheet("background-image: url(bg2.jpg);")
        # ekran başlık kısmındaki ikonun ayarlanması
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_giris = QtWidgets.QPushButton(self.centralwidget)
        self.btn_giris.setGeometry(QtCore.QRect(110, 150, 121, 31))
        # clicked.connect fonsiyonu ile giriş için oluşturulan login metodu çağırılır.
        self.btn_giris.clicked.connect(self.login)
        # butona ikon eklenmesi
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../avatar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_giris.setIcon(icon1)
        self.btn_giris.setObjectName("btn_giris")
        self.lbl_ksifre = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ksifre.setGeometry(QtCore.QRect(110, 110, 91, 21))
        self.lbl_ksifre.setObjectName("lbl_ksifre")
        self.lbl_kad = QtWidgets.QLabel(self.centralwidget)
        self.lbl_kad.setGeometry(QtCore.QRect(110, 70, 91, 31))
        self.lbl_kad.setObjectName("lbl_kad")
        self.le_kad = QtWidgets.QLineEdit(self.centralwidget)
        self.le_kad.setGeometry(QtCore.QRect(230, 80, 131, 22))
        self.le_kad.setObjectName("le_kad")
        self.le_ksifre = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ksifre.setGeometry(QtCore.QRect(230, 110, 131, 22))
        self.le_ksifre.setObjectName("le_ksifre")
        self.btn_adduser = QtWidgets.QPushButton(self.centralwidget)
        self.btn_adduser.setGeometry(QtCore.QRect(240, 150, 121, 31))
        self.btn_adduser.setObjectName("btn_adduser")
        self.btn_adduser.clicked.connect(self.kullaniciEklemeEkrani)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cilt Hastalıkları Tespit Uygulaması"))
        self.btn_giris.setText(_translate("MainWindow", "GİRİŞ"))
        self.lbl_ksifre.setText(_translate("MainWindow", "Şifre :"))
        self.lbl_kad.setText(_translate("MainWindow", "Kullanıcı Adı :"))
        self.btn_adduser.setText(_translate("MainWindow", "YENİ KULLANICI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

