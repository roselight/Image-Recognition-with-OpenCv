# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\girisekrani_gui3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene,QFileDialog,QMainWindow,QMessageBox
from PyQt5.QtGui import QPixmap, QImage
import cv2
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

from hastakayit_gui import *
from kullanicikayit_gui import *
import mysql.connector
import scipy.misc
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="cilth_vt"
)
cursor = db.cursor()

class Ui_MainWindow1(QMainWindow):
    def hata_mesaji1(self,baslik,mesaj):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # Mesaj penceresinin başlık kısmındaki ikonu heartbeat olarak ayarlandı.
        QMessageBox.setWindowIcon(self,icon)
        QMessageBox.warning(self,baslik,mesaj)
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1495, 793)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../heartbeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grview_img = QtWidgets.QGraphicsView(self.centralwidget)
        self.grview_img.setGeometry(QtCore.QRect(20, 130, 771, 541))
        self.grview_img.setFrameShape(QtWidgets.QFrame.Box)
        self.grview_img.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grview_img.setObjectName("grview_img")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(800, 10, 681, 111))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 661, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lbl_hasta_ad = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_hasta_ad.setText("")
        self.lbl_hasta_ad.setObjectName("lbl_hasta_ad")
        self.horizontalLayout.addWidget(self.lbl_hasta_ad)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lbl_hasta_cinsiyet = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_hasta_cinsiyet.setText("")
        self.lbl_hasta_cinsiyet.setObjectName("lbl_hasta_cinsiyet")
        self.horizontalLayout.addWidget(self.lbl_hasta_cinsiyet)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setEnabled(True)
        self.label_4.setMinimumSize(QtCore.QSize(105, 69))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lbl_hasta_yas = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_hasta_yas.setText("")
        self.lbl_hasta_yas.setObjectName("lbl_hasta_yas")
        self.horizontalLayout.addWidget(self.lbl_hasta_yas)
        self.grpBDosyaslem = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBDosyaslem.setGeometry(QtCore.QRect(20, 10, 771, 111))
        self.grpBDosyaslem.setObjectName("grpBDosyaslem")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.grpBDosyaslem)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 751, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_hastaTC = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lb_hastaTC.setObjectName("lb_hastaTC")
        self.horizontalLayout_2.addWidget(self.lb_hastaTC)
        self.le_hastaTC = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.le_hastaTC.setObjectName("le_hastaTC")
        self.horizontalLayout_2.addWidget(self.le_hastaTC)
        self.lbl_dsySec = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbl_dsySec.setFont(font)
        self.lbl_dsySec.setObjectName("lbl_dsySec")
        self.horizontalLayout_2.addWidget(self.lbl_dsySec)
        self.btn_dsysec = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_dsysec.setObjectName("btn_dsysec")
        self.horizontalLayout_2.addWidget(self.btn_dsysec)
        self.lblhastalikad = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblhastalikad.setFont(font)
        self.lblhastalikad.setObjectName("lblhastalikad")
        self.horizontalLayout_2.addWidget(self.lblhastalikad)
        self.cmb_hastalik = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cmb_hastalik.setObjectName("cmb_hastalik")
        self.cmb_hastalik.addItem("")
        self.cmb_hastalik.addItem("")
        self.cmb_hastalik.addItem("")
        self.cmb_hastalik.addItem("")
        self.horizontalLayout_2.addWidget(self.cmb_hastalik)
        self.btn_calistir = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_calistir.setObjectName("btn_calistir")
        self.horizontalLayout_2.addWidget(self.btn_calistir)
        self.grpBoxcikti = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBoxcikti.setGeometry(QtCore.QRect(800, 130, 681, 111))
        self.grpBoxcikti.setObjectName("grpBoxcikti")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.grpBoxcikti)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 661, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_wpAd = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_wpAd.setObjectName("lbl_wpAd")
        self.horizontalLayout_3.addWidget(self.lbl_wpAd)
        self.lbl_whitepixels = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_whitepixels.setText("")
        self.lbl_whitepixels.setObjectName("lbl_whitepixels")
        self.horizontalLayout_3.addWidget(self.lbl_whitepixels)
        self.lbl_bpad = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_bpad.setObjectName("lbl_bpad")
        self.horizontalLayout_3.addWidget(self.lbl_bpad)
        self.lbl_blackpixels = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_blackpixels.setText("")
        self.lbl_blackpixels.setObjectName("lbl_blackpixels")
        self.horizontalLayout_3.addWidget(self.lbl_blackpixels)
        self.lbl_oranAd = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_oranAd.setObjectName("lbl_oranAd")
        self.horizontalLayout_3.addWidget(self.lbl_oranAd)
        self.lbl_oranmiktar = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_oranmiktar.setText("")
        self.lbl_oranmiktar.setObjectName("lbl_oranmiktar")
        self.horizontalLayout_3.addWidget(self.lbl_oranmiktar)
        self.btn_Kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Kaydet.setGeometry(QtCore.QRect(1300, 690, 181, 71))
        self.btn_Kaydet.setObjectName("btn_Kaydet")
        self.grpBox_aciklama = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBox_aciklama.setGeometry(QtCore.QRect(20, 680, 511, 80))
        self.grpBox_aciklama.setObjectName("grpBox_aciklama")
        self.te_aciklama = QtWidgets.QTextEdit(self.grpBox_aciklama)
        self.te_aciklama.setGeometry(QtCore.QRect(10, 20, 491, 51))
        self.te_aciklama.setObjectName("te_aciklama")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(800, 250, 681, 421))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.grpBox_hastalikdrumu = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBox_hastalikdrumu.setGeometry(QtCore.QRect(540, 680, 421, 81))
        self.grpBox_hastalikdrumu.setObjectName("grpBox_hastalikdrumu")
        self.lbl_hastalikDurumu = QtWidgets.QLabel(self.grpBox_hastalikdrumu)
        self.lbl_hastalikDurumu.setGeometry(QtCore.QRect(10, 29, 401, 31))
        self.lbl_hastalikDurumu.setText("")
        self.lbl_hastalikDurumu.setObjectName("lbl_hastalikDurumu")
        self.btn_iptal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iptal.setGeometry(QtCore.QRect(1110, 690, 181, 71))
        self.btn_iptal.setObjectName("btn_iptal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDosya_Se = QtWidgets.QAction(MainWindow)
        self.actionDosya_Se.setObjectName("actionDosya_Se")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_calistir.clicked.connect(self.calistirButonu)
        self.btn_dsysec.clicked.connect(self.showdialog)
        self.btn_Kaydet.clicked.connect(self.islemKayit)

        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap('bg.jpeg'))
        self.grview_img.setScene(self.scene)
        self.le_hastaTC.setText(" ")
        self.cmb_hastalik.setDisabled(True)
        self.btn_dsysec.setDisabled(True)
        self.btn_iptal.clicked.connect(self.hastalikGuncelDurum)
    def calculate_age(self,born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    def veriCek(self,tc,hastalik):
        cursor=db.cursor()
        vericek="Select h_tarih, hastalik_wp, hastalik_bp, hastalik_oran, h_aciklama From hastalik WHERE h_tc=%s AND hastalik_ad=%s"
        sonuc=cursor.execute(vericek, (tc,hastalik))
        sonuc=cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate (sonuc):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    def hastalikGuncelDurum(self):
        cursor=db.cursor()
        h_tc=self.le_hastaTC.text()
        hastalik_ad=self.cmb_hastalik.currentText()
        veri="Select hastalik_oran From hastalik Where h_tc=%s AND hastalik_ad=%s Order By h_tarih DESC "
        sonuc=cursor.execute(veri, (h_tc,hastalik_ad))
        sonuc=cursor.fetchall()
        print("alınan veri",sonuc)
        print(hastalik_ad)
        print(h_tc)
        sondurum =self.lbl_oranmiktar.text()
        oncekidurum=sonuc
        if(sondurum>oncekidurum):
            fark=sondurum-oncekidurum
            self.lbl_hastalikDurumu.setText("Hastalık Oranı %",fark,"lik Artış Gösterdi!")
        else:
            fark=oncekidurum-sondurum
            self.lbl_hastalikDurumu.setText("Hastalık Oranı %",fark,"lik Azalma Gösterdi!")

    def disableButton(self):
        if (len(self.le_hastaTC.text()) > 0):
            self.btn_calistir.setEnabled(True)
    def islemKayit(self):
        h_tc=self.le_hastaTC.text()
        hastalik_Ad=self.cmb_hastalik.currentText()
        hastalik_Resim=self.imgpt
        hastalik_WP=self.lbl_whitepixels.text()
        hastalik_BP=self.lbl_blackpixels.text()
        hastalik_oran=self.lbl_oranmiktar.text()
        hastalik_aciklama=self.te_aciklama.toPlainText()
        hastalik_tarih=date.today()
        cursor = db.cursor()
        try:
         insert = "INSERT INTO hastalik(h_tc,hastalik_ad,hastalik_resim,hastalik_wp,hastalik_bp,hastalik_oran,h_aciklama,h_tarih) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
         cursor.execute(insert, (h_tc,hastalik_Ad,hastalik_Resim,hastalik_WP,hastalik_BP,hastalik_oran,hastalik_aciklama,hastalik_tarih))
         db.commit()
         QMessageBox.information(self, 'BİLGİLENDİRME', "İşlem Başarılı.")
        except:
         QMessageBox.information(self, 'HATA', "İşlem Başarısız!.")
    def hastakayit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi2(self.window)
        self.window.show()
    def kullaniciKayit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi3(self.window)
        self.window.show()
    def calistir(self):

            hasta_tc=(self.le_hastaTC.text())
            sql = ("SELECT * FROM hasta WHERE h_tc=%s")
            cursor.execute(sql,(hasta_tc,))
            veri = cursor.fetchall()
            if (veri == []):
                 self.lbl_hasta_ad.setText("")
                 self.lbl_hasta_cinsiyet.setText("")
                 self.lbl_hasta_yas.setText(str(""))
                 self.hata_mesaji1("Hata!", "Kayıt Bulunamadı.")
                 btn_reply=QMessageBox.question(self, 'BİLGİLENDİRME', "Yeni hasta kaydı oluşturulsun mu?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                 if btn_reply==QMessageBox.Yes:
                     self.hastakayit()
                 else:
                     print("çıkış")
            else:
                for x in veri:
                 self.lbl_hasta_ad.setText(str(x[2]))
                 self.lbl_hasta_cinsiyet.setText(x[3])
                 self.lbl_hasta_yas.setText(str(self.calculate_age(x[4])))
                 self.btn_dsysec.setEnabled(True)

    def selectionchange(self, i):
        if(i=='Vitiligo'):
            try:
                self.vitiligo()
            except:
                self.hata_mesaji1('BİLGİLENDİRME',"Görüntü Dosyası Seçiniz.")
        elif(i=='Rozasea'):
             try:
                 self.rozasea()
             except:
                 self.hata_mesaji1('BİLGİLENDİRME', "Görüntü Dosyası Seçiniz.")

        elif(i=='Tinea Fasiyalis'):
            try:
                self.tineaF()
            except:
                self.hata_mesaji1('BİLGİLENDİRME', "Görüntü Dosyası Seçiniz.")
        else:
            self.hata_mesaji1('HATA',"Lütfen Bir İşlem Seçiniz...")
    def showdialog(self):
        fileName=QFileDialog.getOpenFileName(self,'Open File','C:\\Users\\gulnu\\Desktop\\GUI\\Resimler')
        self.imgpt=fileName[0]
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap(self.imgpt))
        self.grview_img.setScene(self.scene)
        self.cmb_hastalik.setEnabled(True)
        return self.imgpt
    def calistirButonu(self):

        if ((self.le_hastaTC.text()) == "" or self.le_hastaTC.text()==" "):
            self.hata_mesaji1("Hata", "Hasta TC Giriniz!!")

        else:
            self.calistir()
            self.cmb_hastalik.activated[str].connect(self.selectionchange)
            self.veriCek(self.le_hastaTC.text(),self.cmb_hastalik.currentText())
            # self.hastalikGuncelDurum()


    def vitiligo(self):
        self.image= cv2.imread(self.imgpt)
        img=cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img2 = cv2.medianBlur(img, 5)
        ret,th1= cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
        plt.imshow(th1,cmap='gray')
        plt.title('Vitiligo\'lu Alan')
        plt.show()

        n_white_pix = np.sum(th1 == 255)
        n_black_pix = np.sum(th1 == 0)
        n_oran=(n_white_pix*100)/n_black_pix
        n_oran=round(n_oran,4)
        self.lbl_whitepixels.setText(str(n_white_pix))
        self.lbl_blackpixels.setText(str(n_black_pix))
        self.lbl_oranmiktar.setText(str(n_oran))
    def rozasea(self):

        nemo = cv2.imread(self.imgpt)
        nemo1 = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
        hsv_nemo = cv2.cvtColor(nemo1, cv2.COLOR_RGB2HSV)

        lower_blue = np.array([0, 116, 227])
        upper_blue = np.array([174, 255, 255])
        mask = cv2.inRange(hsv_nemo, lower_blue, upper_blue)
        plt.imshow(mask, cmap='gray')
        plt.title('Rozasea\'lı Alan')
        plt.show()

        n_white_pix = np.sum(mask == 255)
        n_black_pix = np.sum(mask == 0)
        n_oran=(n_white_pix*100)/n_black_pix
        n_oran=round(n_oran,4)
        self.lbl_whitepixels.setText(str(n_white_pix))
        self.lbl_blackpixels.setText(str(n_black_pix))
        self.lbl_oranmiktar.setText(str(n_oran))
    def tineaF(self):

      dark = cv2.imread(self.imgpt)
      # dark=cv2.cvtColor(dark, cv2.COLOR_BGR2RGB)
      darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

      bgr = [177, 105, 109]
      thresh =90
      hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
      minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
      maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
      maskHSV = cv2.inRange(darkHSV, minHSV, maxHSV)
      resultHSV = cv2.bitwise_and(darkHSV, darkHSV, mask=maskHSV)
      plt.imshow(maskHSV, cmap='gray')
      plt.title('Tinea Fasiyalis\'li Alan')
      plt.show()

      n_white_pix = np.sum(maskHSV == 255)
      n_black_pix = np.sum(maskHSV == 0)
      n_oran=(n_white_pix*100)/n_black_pix
      n_oran=round(n_oran,4)
      self.lbl_whitepixels.setText(str(n_white_pix))
      self.lbl_blackpixels.setText(str(n_black_pix))
      self.lbl_oranmiktar.setText(str(n_oran))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cilt Hastalıkları Tespit Uygulaması"))
        self.groupBox.setTitle(_translate("MainWindow", "Hasta Bilgileri"))
        self.label_2.setText(_translate("MainWindow", " Ad Soyad :"))
        self.label_3.setText(_translate("MainWindow", "Cinsiyet :"))
        self.label_4.setText(_translate("MainWindow", "Yaş :"))
        self.grpBDosyaslem.setTitle(_translate("MainWindow", "Dosya İşlemleri"))
        self.lb_hastaTC.setText(_translate("MainWindow", "Hasta T.C :"))
        self.lbl_dsySec.setText(_translate("MainWindow", "Dosya Seçiniz :"))
        self.btn_dsysec.setText(_translate("MainWindow", "..."))
        self.lblhastalikad.setText(_translate("MainWindow", "Hastalık Seçiniz : "))
        self.cmb_hastalik.setItemText(0, _translate("MainWindow", "Seçiniz..."))
        self.cmb_hastalik.setItemText(1, _translate("MainWindow", "Vitiligo"))
        self.cmb_hastalik.setItemText(2, _translate("MainWindow", "Rozasea"))
        self.cmb_hastalik.setItemText(3, _translate("MainWindow", "Tinea Fasiyalis"))
        self.btn_calistir.setText(_translate("MainWindow", "Çalıştır"))
        self.grpBoxcikti.setTitle(_translate("MainWindow", "Çıktılar"))
        self.lbl_wpAd.setText(_translate("MainWindow", "WhiteP :"))
        self.lbl_bpad.setText(_translate("MainWindow", "BlackP :"))
        self.lbl_oranAd.setText(_translate("MainWindow", "Oran :"))
        self.btn_Kaydet.setText(_translate("MainWindow", "KAYDET"))
        self.grpBox_aciklama.setTitle(_translate("MainWindow", "Açıklama "))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "White_P"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Black_P"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Oran"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Açıklama"))
        self.grpBox_hastalikdrumu.setTitle(_translate("MainWindow", "Hastalık Durumu"))
        self.btn_iptal.setText(_translate("MainWindow", "İPTAL"))
        self.actionDosya_Se.setText(_translate("MainWindow", "Dosya Seç"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

