# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(500, 650, 271, 51))
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.groupBox_OtherSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_OtherSettings.setGeometry(QtCore.QRect(580, 210, 331, 211))
        self.groupBox_OtherSettings.setObjectName("groupBox_OtherSettings")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_OtherSettings)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 292, 76))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_AddTimeDateToScreen = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_AddTimeDateToScreen.setObjectName("checkBox_AddTimeDateToScreen")
        self.verticalLayout.addWidget(self.checkBox_AddTimeDateToScreen)
        self.checkBox_OpenFolder = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_OpenFolder.setObjectName("checkBox_OpenFolder")
        self.verticalLayout.addWidget(self.checkBox_OpenFolder)
        self.checkBox_OpenExcelFile = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_OpenExcelFile.setObjectName("checkBox_OpenExcelFile")
        self.verticalLayout.addWidget(self.checkBox_OpenExcelFile)
        self.groupBox_Cutters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Cutters.setGeometry(QtCore.QRect(360, 300, 191, 121))
        self.groupBox_Cutters.setObjectName("groupBox_Cutters")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_Cutters)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 172, 76))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_AllResults = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_AllResults.setObjectName("checkBox_AllResults")
        self.verticalLayout_3.addWidget(self.checkBox_AllResults)
        self.checkBox_BlockOfAds = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_BlockOfAds.setObjectName("checkBox_BlockOfAds")
        self.verticalLayout_3.addWidget(self.checkBox_BlockOfAds)
        self.checkBox_JustAd = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_JustAd.setObjectName("checkBox_JustAd")
        self.verticalLayout_3.addWidget(self.checkBox_JustAd)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 551, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_SitesAddresses = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_SitesAddresses.setGeometry(QtCore.QRect(10, 20, 531, 171))
        self.textEdit_SitesAddresses.setObjectName("textEdit_SitesAddresses")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 741))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_Requests = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Requests.setGeometry(QtCore.QRect(10, 20, 321, 711))
        self.textEdit_Requests.setObjectName("textEdit_Requests")
        self.groupBox_Searches = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Searches.setGeometry(QtCore.QRect(360, 210, 191, 91))
        self.groupBox_Searches.setObjectName("groupBox_Searches")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_Searches)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 116, 49))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_Yandex = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_Yandex.setObjectName("checkBox_Yandex")
        self.verticalLayout_2.addWidget(self.checkBox_Yandex)
        self.checkBox_Google = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_Google.setObjectName("checkBox_Google")
        self.verticalLayout_2.addWidget(self.checkBox_Google)
        self.groupBox_Browsers = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Browsers.setGeometry(QtCore.QRect(360, 430, 191, 91))
        self.groupBox_Browsers.setObjectName("groupBox_Browsers")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_Browsers)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 117, 49))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_GoogleChrome = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_GoogleChrome.setObjectName("radioButton_GoogleChrome")
        self.verticalLayout_4.addWidget(self.radioButton_GoogleChrome)
        self.radioButton_Firefox = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_Firefox.setObjectName("radioButton_Firefox")
        self.verticalLayout_4.addWidget(self.radioButton_Firefox)
        self.groupBox_SavePath = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_SavePath.setGeometry(QtCore.QRect(360, 530, 551, 101))
        self.groupBox_SavePath.setObjectName("groupBox_SavePath")
        self.label_SavePath = QtWidgets.QLabel(self.groupBox_SavePath)
        self.label_SavePath.setGeometry(QtCore.QRect(10, 60, 531, 31))
        self.label_SavePath.setObjectName("label_SavePath")
        self.pushButton_SavePath = QtWidgets.QPushButton(self.groupBox_SavePath)
        self.pushButton_SavePath.setGeometry(QtCore.QRect(10, 20, 271, 31))
        self.pushButton_SavePath.setObjectName("pushButton_SavePath")
        self.label_WaitFinish = QtWidgets.QLabel(self.centralwidget)
        self.label_WaitFinish.setGeometry(QtCore.QRect(410, 730, 451, 20))
        self.label_WaitFinish.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WaitFinish.setObjectName("label_WaitFinish")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdsHunter Alpha v0.3"))
        self.pushButton_Start.setText(_translate("MainWindow", "Начать"))
        self.groupBox_OtherSettings.setTitle(_translate("MainWindow", "Другие настройки"))
        self.checkBox_AddTimeDateToScreen.setText(_translate("MainWindow", "Добавить дату и время на скрин"))
        self.checkBox_OpenFolder.setText(_translate("MainWindow", "Открыть папку при завершении поиска"))
        self.checkBox_OpenExcelFile.setText(_translate("MainWindow", "Открыть excel-файл при завершении поиска"))
        self.groupBox_Cutters.setTitle(_translate("MainWindow", "Варианты скриншотов"))
        self.checkBox_AllResults.setText(_translate("MainWindow", "Все результаты запроса"))
        self.checkBox_BlockOfAds.setText(_translate("MainWindow", "Блок объявлений"))
        self.checkBox_JustAd.setText(_translate("MainWindow", "Само объявление"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Сайты"))
        self.groupBox.setTitle(_translate("MainWindow", "Запросы"))
        self.groupBox_Searches.setTitle(_translate("MainWindow", "Системы"))
        self.checkBox_Yandex.setText(_translate("MainWindow", "Яндекс Директ"))
        self.checkBox_Google.setText(_translate("MainWindow", "Google Ads"))
        self.groupBox_Browsers.setTitle(_translate("MainWindow", "Браузеры"))
        self.radioButton_GoogleChrome.setText(_translate("MainWindow", "Google Chrome"))
        self.radioButton_Firefox.setText(_translate("MainWindow", "Firefox"))
        self.groupBox_SavePath.setTitle(_translate("MainWindow", "Путь для сохранения"))
        self.label_SavePath.setText(_translate("MainWindow", "Путь: "))
        self.pushButton_SavePath.setText(_translate("MainWindow", "Выбрать путь для сохранения"))
        self.label_WaitFinish.setText(_translate("MainWindow", "1111"))
