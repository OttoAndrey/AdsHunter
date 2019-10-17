import os
import sys
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from PyQt5 import QtWidgets
from selenium import webdriver
from openpyxl import load_workbook
from interface import *


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
        self.ui.radioButton_Firefox.setDisabled(True)
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
    def cut_all_results(self, driver, folder_path, search, request, site_address):
        driver.save_screenshot('{0}\\{1}_{2}_{3}_{4}'.format(folder_path, search, request, site_address, 'all_results.png'))

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

    # Функция вычисляет позицию сайта относительно блоков спец/сео/гарант
    def get_site_position(self, mas, site_address):
        count = 0
        for index, m in enumerate(mas, start=1):
            if site_address in m[1]:
                count = m[0]
                break
        if count == 0:
            index = 0

        return count, index

    #Функция для определения позиций в спец/seo/гарант
    def get_positions(self, results, site_address):
        special = []
        seo = []
        garant = []

        temp = False

        # Распределяем результаты по массивам
        for result in results:
            if 'реклама' in result[1]:
                if temp:
                    garant.append(result)
                else:
                    special.append(result)
            else:
                temp = True
                seo.append(result)

        special_position = self.get_site_position(special, site_address)
        seo_position = self.get_site_position(seo, site_address)
        garant_position = self.get_site_position(garant, site_address)

        positions = [special_position, seo_position, garant_position]
        block_of_ads = [special, seo, garant]
        return positions, block_of_ads

    #Функция возвращает скрин с нумерацией и рамками
    def edit_screen(self, site_address, screen_name, results, positions, block_of_ads):
        # Начинаем работу с изображением
        image = Image.open(screen_name)
        draw = ImageDraw.Draw(image)
        print('ща начну рисовать')
        # Настройки для ширфта
        font = ImageFont.truetype('Aegean.ttf', 25)

        # Рисуем дату и время
        date = datetime.now().strftime('%d.%m.%Y')
        time = datetime.now().strftime('%H:%M')
        draw.text((15, 60), time, fill=(255, 0, 0), font=font)
        draw.text((15, 95), date, fill=(255, 0, 0), font=font)
        print('нарисовал дату время')
        # Выделяем рамкой искомые запросы
        for position in positions:
            if position[0] != 0:
                element = results[position[0] - 1]
                print(element[2])
                print(element[3])
                draw.rectangle((element[2]['x'], element[2]['y'], element[2]['x'] + element[3]['width'],
                                element[2]['y'] + element[3]['height']), outline=(255, 0, 0, 255), width=3, )

        # Рисуем на скрине нумерацию
        for result in results:
            draw.text((result[2]['x'] - 100, result[2]['y']), str(result[0]), fill=(0, 0, 0), font=font)

        for index, spcl in enumerate(block_of_ads[0], start=1):
            draw.text((spcl[2]['x'] - 50, spcl[2]['y']), str(index), fill=(255, 0, 0), font=font)

        for index, s in enumerate(block_of_ads[1], start=1):
            draw.text((s[2]['x'] - 50, s[2]['y']), str(index), fill=(0, 128, 0), font=font)

        for index, g in enumerate(block_of_ads[2], start=1):
            draw.text((g[2]['x'] - 50, g[2]['y']), str(index), fill=(0, 0, 255), font=font)

        # Конец рисования
        del draw
        # image.save('{0}_{1}'.format(screen_name, 'new.png'))
        image.save(screen_name)
        print('сохранил нвоый рисунок')

    #Функция для создания файла по экселю и записи в него статистики
    def edit_file_stat(self, site_address, user_requests, statistics, folder_path):
        # Открываем шаблон файл экселя для записи статистики
        wb = load_workbook('template.xlsx')
        sheet = wb.active
        sheet['A3'].value = site_address

        start = 'B3'
        end = 'F{0}'.format(len(user_requests) + 3)

        for cellObj, stat in zip(sheet[start:end], statistics):
            for index, (cell, s) in enumerate(zip(cellObj, stat)):

                if index == 0:
                    cell.value = s

                elif index == 1 or index == 2 or index == 3:
                    cell.value = s[1]
                elif index == 4:
                    cell.value = s
                    cell.hyperlink = s
                    cell.style = 'Hyperlink'

        wb.save('{0}\\{1}.xlsx'.format(folder_path, site_address))


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
        # TODO ну или регулярное выражение, пока не напишет нормально
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

        #Массив для сбора статистики (спец, сео, гарант)
        statistics = []

        '''Начинаем перебирать системы поиска, затем открываем бразуер, формируем запрос,
        на странцие ищем рекламу, и если находим перебираем список с методами нарезки скринов'''
        options = self.options

        # Перебор всех поисковых систем
        for url in self.searchers:

            # TODO продумать как изменять search. Когда ищет по яндексу должен быть yandex, когда по гуглу должен быть google
            search = 'yandex'

            # Перебор всех поисковых запросов
            for request in user_requests:
                results = []
                positions = [(0, 0), (0, 0), (0, 0)]
                screen_name = 'Результатов нет'

                driver = self.browser(options=options)
                current_url = url + request
                driver.get(current_url)

                # TODO продумать этот момент для гугла
                # Находим все элементы выдачи на странице
                web_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')

                # TODO в каждом результате много данных и в них программа ищет наличие сайта
                # TODO для оптимищации следует собирать со страницы только адреса, сравнивать их с нашим сайтом (сделать потом)
                # Перебор реузльтатов выдачи поиска
                for result in web_results:
                    if 'реклама' in result.text and site_address in result.text:
                        print()
                        print(result.text)

                        #Собираем всю инфу со страницы
                        for index, result in enumerate(web_results, start=1):
                            results.append((index, result.text, result.location, result.size))

                        # Перебор методов нарезания скриншотов
                        # for screen_cut in self.methods_of_screen:
                        #     screen_cut(driver, folder_path, search, request, site_address)

                        #TODO тут с именем скриншота. Как его потом вытаскивать из функций
                        screen_name = '{0}\\{1}_{2}_{3}_{4}'.format(folder_path, search, request, site_address, 'all_results.png')
                        driver.save_screenshot(screen_name)
                        # Закрываем, так как для этого запроса браузер нам уже не понадобится
                        driver.close()

                        positions, block_of_ads = self.get_positions(results, site_address)

                        #Рисуем на скрине
                        self.edit_screen(site_address, screen_name, results, positions, block_of_ads)
                        break

                #Разбиваем массив с позициями на несколько массивов, так проще потом обрабатывать
                spec = positions[0]
                seo = positions[1]
                garant = positions[2]

                #Добавляем данные в один большой, чтобы потом записать всё в эксель файл
                statistics.append((request, spec, seo, garant, screen_name))

        #Записываем статистику в файл
        self.edit_file_stat(site_address, user_requests, statistics, folder_path)


        self.ui.label_WaitFinish.setText('Готово! ( ͡° ͜ʖ ͡°)')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyWin()
    myApp.show()
    sys.exit(app.exec_())
