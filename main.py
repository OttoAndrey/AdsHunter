from selenium import webdriver
from PIL import Image
from time import sleep
from openpyxl import Workbook, load_workbook
import os
import sys
from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Для хранения систем, где будем производить поиск
        self.searchers = []
        self.methods_of_screen = []
        self.browser = None
        self.options = None
        self.save_path = None

        # Назначаем кнопке Старт функцию start
        self.ui.pushButton_Start.clicked.connect(self.start)
        self.ui.pushButton_SavePath.clicked.connect(self.get_save_path)

        # Назначаем на клик по чекбоксу функции, которые добавляют/убирают из списка поиск в системах
        self.ui.checkBox_Google.clicked.connect(self.settings_google)
        self.ui.checkBox_Yandex.clicked.connect(self.settings_yandex)

        # Назначаем на клик по радиобтн функцию, которая изменяет значение переменной browser в соответствии с значением
        self.ui.radioButton_GoogleChrome.clicked.connect(self.set_browser)
        self.ui.radioButton_Firefox.clicked.connect(self.set_browser)

        #
        self.ui.checkBox_AllResults.clicked.connect(self.settings_all_results)
        self.ui.checkBox_BlockOfAds.clicked.connect(self.settings_block_of_ads)
        self.ui.checkBox_JustAd.clicked.connect(self.settings_just_ad)

        # Значения элементов интерфейса по умолчанию
        self.ui.label_WaitFinish.setText('Нажмите "Начать" для выполнения программы, но придется подождать...')
        # self.ui.checkBox_Yandex.setChecked(True)
        # self.ui.radioButton_Firefox.setChecked(True)
        # self.ui.checkBox_AllResults.setChecked(True)

        # Заглушки, пока функционал не готов
        self.ui.checkBox_Google.setDisabled(True)
        # self.ui.radioButton_GoogleChrome.setDisabled(True)
        self.ui.checkBox_BlockOfAds.setDisabled(True)
        self.ui.checkBox_JustAd.setDisabled(True)
        self.ui.checkBox_AddTimeDateToScreen.setDisabled(True)

        # Временный текст
        self.ui.textEdit_Requests.setText("""смартфоны купить
ноутбук красноярск
купить ноутбук
смартфон samsung""")
        self.ui.lineEdit_SiteAddress.setText('citilink.ru')

    # Ф-ия присваивает переменным путь, который задаёт пользователь
    def get_save_path(self):
        self.save_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.label_SavePath.setText('Путь: {0}'.format(self.save_path))

    # Ф-ии нарезания скриншотов
    def cut_all_results(self, all_results, folder_path, search, request, site_address):
        all_results.screenshot('{0}\\{1}_{2}_{3}_{4}'.format(folder_path, search, request, site_address, 'all_results.png'))

    def cut_block_of_ads(self):
        pass

    def cut_just_ad(self):
        pass

    # Ф-ии добавляют/удаляют из списка способы нарезания скриншотов
    def settings_block_of_ads(self):
        if self.ui.checkBox_BlockOfAds.isChecked():
            self.methods_of_screen.append(self.cut_block_of_ads)
        else:
            self.methods_of_screen.remove(self.cut_block_of_ads)

    def settings_just_ad(self):
        if self.ui.checkBox_JustAd.isChecked():
            self.methods_of_screen.append(self.cut_just_ad)
        else:
            self.methods_of_screen.remove(self.cut_just_ad)

    def settings_all_results(self):
        if self.ui.checkBox_AllResults.isChecked():
            self.methods_of_screen.append(self.cut_all_results)
        else:
            self.methods_of_screen.remove(self.cut_all_results)

    # Функция изменяет значение browser
    def set_browser(self):
        if self.ui.radioButton_GoogleChrome.isChecked():
            self.browser = webdriver.Chrome
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('headless')
            self.options.add_argument('window-size=800x3800')
        else:
            self.browser = webdriver.Firefox

    # Функция добавляет/удаляет в/из списка url для поиска в яндексе
    def settings_yandex(self):
        if self.ui.checkBox_Yandex.isChecked():
            self.searchers.append('https://yandex.ru/search/?text=')
        else:
            self.searchers.remove('https://yandex.ru/search/?text=')

    # Функция добавляет/удаляет в/из списка url для поиска в гугле
    def settings_google(self):
        if self.ui.checkBox_Google.isChecked():
            self.searchers.append('https://www.google.com/search?q=')
        else:
            self.searchers.remove('https://www.google.com/search?q=')

    # Функция разбивает текст пользователя в поле Запросы на элементы массива и возвращает массив
    def get_requests(self):
        user_requests = self.ui.textEdit_Requests.toPlainText().split('\n')
        return user_requests

    # Функция срабатывает при нажатии на кнопку Старт
    def start(self):
        self.ui.label_WaitFinish.setText('Программа выполняется. Подождите...')
        print('Текущие настройки:')
        print(self.searchers)
        print(self.browser)
        print(self.methods_of_screen)
        print(self.save_path)

        # Адрес сайта, который ввел пользователь
        # TODO отрезать лишнее: https, www, после ru/com тоже убирать
        site_address = self.ui.lineEdit_SiteAddress.text()
        print(site_address)

        # Массив с запросами для поиска
        user_requests = self.get_requests()
        print(user_requests)

        # Путь для создания папки со скриншотами
        # TODO брать с путь с интерфейса, который указал пользователь
        # folder_path = 'C:\\Users\\{0}\\Desktop\\'.format(os.getlogin()) + site_address
        folder_path = '{0}\\{1}'.format(self.save_path, site_address)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        '''Начинаем перебирать системы поиска, затем открываем бразуер, формируем запрос,
        на странцие ищем рекламу, и если находим перебираем список с методами нарезки скринов'''

        for url in self.searchers:
            options = self.options
            driver = self.browser(options=options)

            # TODO продумать как изменять search. Когда ищет по яндексу должен быть yandex, когда по гуглу должен быть google
            search = 'yandex'

            for request in user_requests:
                current_url = url + request
                driver.get(current_url)

                # Находим все элементы выдачи на странице
                # TODO продумать этот момент для гугла
                results = driver.find_elements_by_xpath('//li[@class="serp-item"]')

                # Перебираем результаты и ищем с рекламой и с нашим сайтом
                for result in results:
                    if 'реклама' in result.text and site_address in result.text:
                        print()
                        print(result.text)
                        all_results = driver.find_element_by_class_name('main')
                        for screen_cut in self.methods_of_screen:
                            screen_cut(all_results, folder_path, search, request, site_address)
        driver.close()
        self.ui.label_WaitFinish.setText('Готово! ( ͡° ͜ʖ ͡°)')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyWin()
    myApp.show()
    sys.exit(app.exec_())
