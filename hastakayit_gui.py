# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\hastakayit_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox,QWidget,QMainWindow

from PyQt5.QtCore import  Qt, QDate, QDateTime

# Veritabanı bağlantısı için sql cümleciği oluşturuldu.
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="cilth_vt"
)
cursor = db.cursor()

class Ui_MainWindow2(QMainWindow):
    def setupUi2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 205)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_kayit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kayit.setGeometry(QtCore.QRect(180, 150, 121, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../avatar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_kayit.setIcon(icon1)
        self.btn_kayit.setObjectName("btn_kayit")
        self.btn_kayit.clicked.connect(self.kayitekle)
        self.btn_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikis.setGeometry(QtCore.QRect(310, 150, 121, 31))
        self.btn_cikis.setObjectName("btn_cikis")
        self.btn_cikis.clicked.connect(self.close)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 571, 128))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_htc = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_htc.setObjectName("lbl_htc")
        self.gridLayout_3.addWidget(self.lbl_htc, 0, 0, 1, 1)
        self.lbl_hadsoyad = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_hadsoyad.setObjectName("lbl_hadsoyad")
        self.gridLayout_3.addWidget(self.lbl_hadsoyad, 1, 0, 1, 1)
        self.lbl_hcinsiyet = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_hcinsiyet.setObjectName("lbl_hcinsiyet")
        self.gridLayout_3.addWidget(self.lbl_hcinsiyet, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lbl_hdt = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_hdt.setObjectName("lbl_hdt")
        self.gridLayout_3.addWidget(self.lbl_hdt, 3, 0, 1, 1)
        self.dt_hdt = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dt_hdt.setObjectName("dt_hdt")
        self.dt_hdt.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.gridLayout_3.addWidget(self.dt_hdt, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def kayitekle(self):
      # k_ad/k_sfire lineedit'ten alınan verileri sorguya gönderir.
      h_tc=self.lineEdit.text()
      h_ads=self.lineEdit_2.text()
      h_csyt=self.lineEdit_3.text()
      h_dt=self.dt_hdt.text()
      icon = QtGui.QIcon()
      icon.addPixmap(QtGui.QPixmap("heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
      QMessageBox.setWindowIcon(self, icon)


      try:
         hasta_ekle = ("INSERT INTO hasta(h_tc,h_ad_sad,h_cins,h_dt) VALUES (%s,%s,%s,%s)")
         cursor.execute(hasta_ekle,(h_tc,h_ads,h_csyt,h_dt))
         db.commit()
         veri = cursor.rowcount
      except:
         veri=2

      if (veri == 1):

         QMessageBox.information(self, 'BİLGİLENDİRME', "İşlem Başarılı.")
      else:
          QMessageBox.information(self, 'BİLGİLENDİRME', "İşlem Başarısız")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cilt Hastalıkları Tespit Uygulaması-Hasta Kayıt Ekranı"))
        self.btn_kayit.setText(_translate("MainWindow", "ONAYLA"))
        self.btn_cikis.setText(_translate("MainWindow", "İPTAL"))
        self.lbl_htc.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.lbl_hadsoyad.setText(_translate("MainWindow", "Hasta Adı Soyadı:"))
        self.lbl_hcinsiyet.setText(_translate("MainWindow", "Cinsiyet: "))
        self.lbl_hdt.setText(_translate("MainWindow", "Doğum Tarihi:"))
        self.dt_hdt.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

