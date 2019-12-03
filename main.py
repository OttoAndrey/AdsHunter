import os
import sys
from datetime import datetime
from functools import partial

from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QCompleter, QTableWidgetItem
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from selenium import webdriver

from interface import *


class SearchThread(QThread):
    def __init__(self, mainwindow):
        QThread.__init__(self)
        self.mainwindow = mainwindow

    def run(self):
        # Запуск функции поиска
        self.mainwindow.start_searching()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Экземпляр потока
        self.thread_instance = SearchThread(self)

        # Настройки таблицы
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(5)

        # Массив с регионами из эксель файла
        regions = self.get_regions()
        print(regions)

        # Настройки завершателя слов
        completer = QCompleter(regions)
        completer.setCaseSensitivity(False)

        # В ячейки таблицы первого столбца устанавливаем QLineEdit, в которые пользователь будет писать регионы
        line_edits = []
        for i in range(0, self.ui.tableWidget.rowCount()):
            line_edits.append(QtWidgets.QLineEdit())
            # Устанавливаем QLineEdit QCompleter, чтобы он завершал слова, которые пишет пользователь
            line_edits[i].setCompleter(completer)
            self.ui.tableWidget.setCellWidget(i, 0, line_edits[i])
            # Передаём частями в функцию данные о тексте, о номере строки и столбца, в которой находится QLineEdit
            line_edits[i].editingFinished.connect(partial(self.get_lr, cell=self.ui.tableWidget.cellWidget(i, 0), row=i, column=1))

        print(line_edits)
        print(self.ui.tableWidget.rowCount())

        # Переменные для
        self.searchers = []  # для хранения всех систем поиска
        self.methods_of_screen = []  # для методов нарезания скринов
        self.browser = None  # браузер
        self.options = None  # опции
        self.save_path = None  # путь для сохранения

        # Назначаем кнопке Старт функцию start_search, которая отвечает за запуск метода run() в классе потока
        self.ui.pushButton_Start.clicked.connect(self.start_search)
        self.ui.pushButton_SavePath.clicked.connect(self.get_save_path)

        # Назначаем на клик по чекбоксу функции, которые добавляют/убирают из списка поиск в системах
        self.ui.checkBox_Google.clicked.connect(self.settings_google)
        self.ui.checkBox_Yandex.clicked.connect(self.settings_yandex)

        # Назначаем на клик по радиобтн функцию, которая изменяет значение переменной browser в соответствии с значением
        self.ui.radioButton_GoogleChrome.clicked.connect(self.set_browser)
        self.ui.radioButton_Firefox.clicked.connect(self.set_browser)

        # Назначаем клик по чекбоксам при выборе методов нарезания скринов
        self.ui.checkBox_AllResults.clicked.connect(self.settings_all_results)
        self.ui.checkBox_BlockOfAds.clicked.connect(self.settings_block_of_ads)
        self.ui.checkBox_JustAd.clicked.connect(self.settings_just_ad)

        # Значения элементов интерфейса по умолчанию
        self.ui.label_WaitFinish.setText('Нажмите "Начать" для выполнения программы')
        self.ui.checkBox_Yandex.setChecked(True)
        self.ui.radioButton_GoogleChrome.setChecked(True)
        self.ui.checkBox_AllResults.setChecked(True)

        # Вызываем функции, чтобы значения по умолчанию добавились в массивы
        self.settings_all_results()
        self.set_browser()
        self.settings_yandex()

        # Заглушки, пока функционал не готов
        self.ui.checkBox_Yandex.setDisabled(True)
        self.ui.checkBox_AllResults.setDisabled(True)
        self.ui.radioButton_GoogleChrome.setDisabled(True)

        self.ui.checkBox_Google.setVisible(False)
        self.ui.radioButton_Firefox.setVisible(False)
        self.ui.checkBox_BlockOfAds.setVisible(False)
        self.ui.checkBox_JustAd.setVisible(False)
        self.ui.checkBox_Google.setDisabled(True)
        self.ui.radioButton_Firefox.setDisabled(True)
        self.ui.checkBox_BlockOfAds.setDisabled(True)
        self.ui.checkBox_JustAd.setDisabled(True)

        # Временный текст
#         self.ui.textEdit_Requests.setText("""смартфоны купить
# ноутбук красноярск
# купить ноутбук
# смартфон samsung""")
#         self.ui.textEdit_SitesAddresses.setText("""citilink.ru
# aldo-shop.ru""")

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
            self.searchers.append('https://yandex.ru/search/?text={0}&lr={1}')
        else:
            self.searchers.remove('https://yandex.ru/search/?text={0}&lr={1}')

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

    def get_sites_addresses(self):
        sites_addresses = self.ui.textEdit_SitesAddresses.toPlainText().split('\n')
        return sites_addresses

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

    # Функция для определения позиций в спец/seo/гарант
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

    # Функция возвращает скрин с нумерацией и рамками
    def edit_screen(self, screen_name, results, positions, block_of_ads):
        # Начинаем работу с изображением
        image = Image.open(screen_name)
        draw = ImageDraw.Draw(image)
        print('ща начну рисовать')
        # Настройки для ширфта
        font = ImageFont.truetype('Aegean.ttf', 25)

        # Рисуем дату и время
        if self.ui.checkBox_AddTimeDateToScreen.isChecked():
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
        image.save(screen_name)
        print('сохранил новый рисунок')

    # Функция возвращает значение lr для региона, который выбрал пользователь
    def get_lr(self, cell, row, column):
        print(cell.text())
        print(row)
        print(column)

        if cell.text() == '':
            return

        lr = 'None'
        region = cell.text()

        wb = load_workbook('regions.xlsx')
        sheet = wb.active

        column_regions = sheet['B']
        for index, cell_ex in enumerate(column_regions, start=1):
            if cell_ex.value == region:
                lr = sheet['A' + str(index)].value
                break
        wb.close()

        print(lr)

        self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(lr)))

    # Функция возвращает список с городами для пользовательского поиска
    def get_regions(self):

        # Сделать кортеж
        regions = []

        wb = load_workbook('regions.xlsx')
        sheet = wb.active

        column_regions = sheet['B']
        for cell in column_regions:
            regions.append(cell.value)

        print(regions)
        wb.close()
        return regions

    # Функция возвращает словарь регионов из виджета
    def get_regions_from_table(self):
        regions = {}
        for row in range(0, 5):
            try:
                # Пропускаем, если пользователь в таблице оставил пустые строки или города с None
                if self.ui.tableWidget.cellWidget(row, 0).text() == '' or self.ui.tableWidget.item(row, 1).text() == 'None':
                    continue

                city = self.ui.tableWidget.cellWidget(row, 0).text()
                lr = self.ui.tableWidget.item(row, 1).text()
                regions[city] = lr
            except:
                pass

        if len(regions.items()) == 0:
            regions['current'] = ''

        return regions

    # Функция для создания файла по экселю и записи в него статистики
    def edit_file_stat(self, statistics, folder_path):
        # Открываем шаблон файл экселя для записи статистики
        wb = load_workbook('template.xlsx')
        sheet = wb.active

        start = 'A3'
        end = 'G{0}'.format(len(statistics) + 3)

        for cellObj, stat in zip(sheet[start:end], statistics):
            for index, (cell, s) in enumerate(zip(cellObj, stat)):

                # 0 - Регион
                # 2 - Сайт
                if index == 0 or index == 2:
                    cell.value = s

                # 1 - Запрос. Если результатов нет, то красим ячейку в красный
                elif index == 1:
                    if stat[6] == 'Результатов нет':
                        cell.fill = PatternFill(start_color='da9694', fill_type='solid')
                    cell.value = s

                # 3, 4, 5 - Значения позиций на странице. Если объявления нет, то ставит прочерк
                elif index == 3 or index == 4 or index == 5:
                    if s[1] == 0:
                        cell.value = '-'
                    else:
                        cell.value = s[1]

                # 6 - Гиперссылка на скриншот
                elif index == 6:
                    cell.value = s
                    cell.hyperlink = s
                    cell.style = 'Hyperlink'

        wb.save('{0}\\statistics.xlsx'.format(folder_path))

    # Открывает папку, куда указал пользователь
    def open_folder(self, folder_path):
        folder_path = folder_path.replace('/', '\\')
        os.system('explorer "{0}"'.format(folder_path))

    # Открывает excel файл со статистикой
    def open_excel_file(self, folder_path):
        folder_path = folder_path.replace('/', '\\')
        os.system('explorer "{0}\\statistics.xlsx"'.format(folder_path))

    def start_search(self):
        self.thread_instance.start()

    # Функция срабатывает при нажатии на кнопку Старт
    def start_searching(self):
        self.ui.label_WaitFinish.setText('Программа выполняется. Подождите...')
        print('Текущие настройки:')
        print(self.searchers)
        print(self.browser)
        print(self.methods_of_screen)
        print(self.save_path)

        # Адрес сайта, который ввел пользователь
        # TODO отрезать лишнее: https, www, после ru/com тоже убирать
        # TODO ну или регулярное выражение, пока не напишет нормально
        sites_addresses = self.get_sites_addresses()
        print(sites_addresses)

        # Массив с запросами для поиска
        user_requests = self.get_requests()
        print(user_requests)

        #Словарь с регионами и кодами lr
        regions = self.get_regions_from_table()
        print(regions)

        print(len(user_requests))
        print(len(regions))

        # Проверка на большое кол-во обращений к яндексу
        if len(user_requests) * len(regions) > 20:
            self.ui.label_WaitFinish.setText("""Кол-во обращений (запросы * регионы) к яндексу превышает 20! 
Сделайте поменьше, пожалуйста""")
            return ''

        # Проверка ввел ли пользователь все данные
        if user_requests[0] == '' or sites_addresses[0] == '' or self.save_path == None or self.save_path == '':
            self.ui.label_WaitFinish.setText('Ошибка! Вы не указали запросы, сайт или путь для сохранения!')
            return ''

        # Путь для создания папки со скриншотами
        # TODO брать с путь с интерфейса, который указал пользователь
        # folder_path = 'C:\\Users\\{0}\\Desktop\\'.format(os.getlogin()) + site_address
        folder_path = '{0}\\AH {1}'.format(self.save_path, sites_addresses[0])
        self.ui.label_SavePath.setText('Путь: {0}'.format(folder_path))
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # Массив для сбора статистики (спец, сео, гарант)
        statistics = []

        '''Начинаем перебирать системы поиска, затем открываем бразуер, формируем запрос,
        на странцие ищем рекламу, и если находим перебираем список с методами нарезки скринов'''
        options = self.options

        # Перебор всех поисковых систем
        for url in self.searchers:
            # TODO продумать как изменять search. Когда ищет по яндексу должен быть yandex, когда по гуглу должен быть google
            search = 'yandex'

            # Открываем браузер с заданными настройками
            driver = self.browser(options=options)  # options=options

            # Перебор регионов, по которым ведётся поиск
            for region, lr in regions.items():
                print(region)
                print(lr)

                # Перебор всех поисковых запросов
                for request in user_requests:
                    current_url = url.format(request, lr)
                    print(current_url)
                    driver.get(current_url)

                    # TODO продумать этот момент для гугла
                    # Находим все элементы выдачи на странице
                    web_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')

                    for site_address in sites_addresses:

                        self.ui.label_WaitFinish.setText('Выполняю запрос: {0} - {1} - {2}'.format(region, request, site_address))
                        results = []

                        # Лист для позиций искомого сайта в выдаче
                        # Первое число позиция по всем запросам, второе относительно блока в котором находится
                        positions = [(0, 0), (0, 0), (0, 0)]
                        screen_name = 'Результатов нет'

                        # TODO в каждом результате много данных и в них программа ищет наличие сайта
                        # TODO для оптимищации следует собирать со страницы только адреса, сравнивать их с нашим сайтом (сделать потом)
                        # Перебор реузльтатов выдачи поиска
                        for result in web_results:

                            if site_address in result.text:
                                print()
                                print(result.text)

                                # Собираем всю инфу со страницы
                                for index, result in enumerate(web_results, start=1):
                                    results.append((index, result.text, result.location, result.size))

                                # Перебор методов нарезания скриншотов
                                # for screen_cut in self.methods_of_screen:
                                #     screen_cut(driver, folder_path, search, request, site_address)

                                # TODO тут с именем скриншота. Как его потом вытаскивать из функций
                                screen_name = '{0}\\{1}_{2}_{3}_{4}_{5}'.format(folder_path, search, region, request, site_address, 'all_results.png')
                                print(screen_name)

                                # Блок кода, чтобы делать скрин рабочего стола
                                # wr = driver.find_element_by_xpath('//li[@class="serp-item"][2]')
                                # driver.execute_script('arguments[0].scrollIntoView();', wr)
                                # sleep(3)
                                # bitmap = autopy.bitmap.capture_screen()
                                # bitmap.save('screen.png')

                                driver.save_screenshot(screen_name)

                                positions, block_of_ads = self.get_positions(results, site_address)

                                # Рисуем на скрине
                                self.ui.label_WaitFinish.setText('Выполняю запрос: {0} - {1} - {2}. Рисую на скрине'.format(region, request, site_address))
                                self.edit_screen(screen_name, results, positions, block_of_ads)
                                break

                        # Разбиваем массив с позициями на несколько массивов, так проще потом обрабатывать
                        spec = positions[0]
                        seo = positions[1]
                        garant = positions[2]

                        # Добавляем данные в один большой, чтобы потом записать всё в эксель файл
                        statistics.append((region, request, site_address, spec, seo, garant, screen_name))

            # Закрываем браузер
            driver.close()
            print('закрыл драйвер')

        # Вот тут желательно перебрать скрины и обработать их
        self.ui.label_WaitFinish.setText('Обрабатываю скриншоты')
        # "тут"

        # Записываем статистику в файл
        self.ui.label_WaitFinish.setText('Собираю статистику в файл')
        self.edit_file_stat(statistics, folder_path)
        print('записал стату в файл')

        # Закрывает процесс chromedriver
        os.system("TASKKILL /F /IM chromedriver.exe")
        print('закрыл chromedriver')

        self.ui.label_WaitFinish.setText('Готово! ( ͡° ͜ʖ ͡°)')

        # Проверка указал ли пользователь открывать папку
        if self.ui.checkBox_OpenFolder.isChecked():
            self.open_folder(folder_path)
            print('открыл папку')

        # Проверка указал ли пользователь открывать excel файл
        if self.ui.checkBox_OpenExcelFile.isChecked():
            self.open_excel_file(folder_path)
            print('открыл файл')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyWin()
    myApp.show()
    sys.exit(app.exec_())
