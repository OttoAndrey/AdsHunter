# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(500, 610, 271, 51))
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.groupBox_OtherSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_OtherSettings.setGeometry(QtCore.QRect(680, 420, 231, 80))
        self.groupBox_OtherSettings.setObjectName("groupBox_OtherSettings")
        self.checkBox_AddTimeDateToScreen = QtWidgets.QCheckBox(self.groupBox_OtherSettings)
        self.checkBox_AddTimeDateToScreen.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.checkBox_AddTimeDateToScreen.setObjectName("checkBox_AddTimeDateToScreen")
        self.groupBox_Cutters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Cutters.setGeometry(QtCore.QRect(720, 280, 191, 131))
        self.groupBox_Cutters.setObjectName("groupBox_Cutters")
        self.checkBox_JustAd = QtWidgets.QCheckBox(self.groupBox_Cutters)
        self.checkBox_JustAd.setGeometry(QtCore.QRect(10, 90, 171, 20))
        self.checkBox_JustAd.setObjectName("checkBox_JustAd")
        self.checkBox_AllResults = QtWidgets.QCheckBox(self.groupBox_Cutters)
        self.checkBox_AllResults.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.checkBox_AllResults.setObjectName("checkBox_AllResults")
        self.checkBox_BlockOfAds = QtWidgets.QCheckBox(self.groupBox_Cutters)
        self.checkBox_BlockOfAds.setGeometry(QtCore.QRect(10, 60, 171, 20))
        self.checkBox_BlockOfAds.setObjectName("checkBox_BlockOfAds")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 551, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_SiteAddress = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_SiteAddress.setGeometry(QtCore.QRect(10, 20, 531, 31))
        self.lineEdit_SiteAddress.setText("")
        self.lineEdit_SiteAddress.setObjectName("lineEdit_SiteAddress")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 741))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_Requests = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Requests.setGeometry(QtCore.QRect(10, 20, 321, 711))
        self.textEdit_Requests.setObjectName("textEdit_Requests")
        self.groupBox_Searches = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Searches.setGeometry(QtCore.QRect(720, 80, 191, 80))
        self.groupBox_Searches.setObjectName("groupBox_Searches")
        self.checkBox_Google = QtWidgets.QCheckBox(self.groupBox_Searches)
        self.checkBox_Google.setGeometry(QtCore.QRect(10, 50, 131, 20))
        self.checkBox_Google.setObjectName("checkBox_Google")
        self.checkBox_Yandex = QtWidgets.QCheckBox(self.groupBox_Searches)
        self.checkBox_Yandex.setGeometry(QtCore.QRect(10, 20, 131, 20))
        self.checkBox_Yandex.setObjectName("checkBox_Yandex")
        self.groupBox_Browsers = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Browsers.setGeometry(QtCore.QRect(720, 160, 191, 111))
        self.groupBox_Browsers.setObjectName("groupBox_Browsers")
        self.radioButton_GoogleChrome = QtWidgets.QRadioButton(self.groupBox_Browsers)
        self.radioButton_GoogleChrome.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.radioButton_GoogleChrome.setObjectName("radioButton_GoogleChrome")
        self.radioButton_Firefox = QtWidgets.QRadioButton(self.groupBox_Browsers)
        self.radioButton_Firefox.setGeometry(QtCore.QRect(10, 70, 95, 20))
        self.radioButton_Firefox.setObjectName("radioButton_Firefox")
        self.groupBox_SavePath = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_SavePath.setGeometry(QtCore.QRect(360, 500, 551, 101))
        self.groupBox_SavePath.setObjectName("groupBox_SavePath")
        self.label_SavePath = QtWidgets.QLabel(self.groupBox_SavePath)
        self.label_SavePath.setGeometry(QtCore.QRect(10, 60, 531, 31))
        self.label_SavePath.setObjectName("label_SavePath")
        self.pushButton_SavePath = QtWidgets.QPushButton(self.groupBox_SavePath)
        self.pushButton_SavePath.setGeometry(QtCore.QRect(10, 20, 271, 31))
        self.pushButton_SavePath.setObjectName("pushButton_SavePath")
        self.label_WaitFinish = QtWidgets.QLabel(self.centralwidget)
        self.label_WaitFinish.setGeometry(QtCore.QRect(410, 700, 451, 20))
        self.label_WaitFinish.setText("")
        self.label_WaitFinish.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WaitFinish.setObjectName("label_WaitFinish")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdsHunter Alpha v0.2"))
        self.pushButton_Start.setText(_translate("MainWindow", "Начать"))
        self.groupBox_OtherSettings.setTitle(_translate("MainWindow", "Другие настройки"))
        self.checkBox_AddTimeDateToScreen.setText(_translate("MainWindow", "Добавить дату и время на скрин"))
        self.groupBox_Cutters.setTitle(_translate("MainWindow", "Варианты скриншотов"))
        self.checkBox_JustAd.setText(_translate("MainWindow", "Само объявление"))
        self.checkBox_AllResults.setText(_translate("MainWindow", "Все результаты запроса"))
        self.checkBox_BlockOfAds.setText(_translate("MainWindow", "Блок объявлений"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Сайт"))
        self.groupBox.setTitle(_translate("MainWindow", "Запросы"))
        self.groupBox_Searches.setTitle(_translate("MainWindow", "Системы"))
        self.checkBox_Google.setText(_translate("MainWindow", "Google Ads"))
        self.checkBox_Yandex.setText(_translate("MainWindow", "Яндекс Директ"))
        self.groupBox_Browsers.setTitle(_translate("MainWindow", "Браузеры"))
        self.radioButton_GoogleChrome.setText(_translate("MainWindow", "Google Chrome"))
        self.radioButton_Firefox.setText(_translate("MainWindow", "Firefox"))
        self.groupBox_SavePath.setTitle(_translate("MainWindow", "Путь для сохранения"))
        self.label_SavePath.setText(_translate("MainWindow", "Путь: "))
        self.pushButton_SavePath.setText(_translate("MainWindow", "Выбрать путь для сохранения"))
