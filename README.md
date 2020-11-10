# AdsHunter
Десктопное приложение для автоматизации аудита рекламных кампаний.

Если вы хотите узнать показывается ли ваше объявление в системах поиска Яндекса или Google,
но для того чтобы не перебирать запросы вручную можно использовать данную программу.

## Интерфейс программы

Интерфейс программы сделан с помощью PyQt.

![interface](.gitbook/assets/interface.PNG)

## Результат

Пример скриншота.

![result](.gitbook/assets/result.png)

Пример файла со статистикой.

![statistics](.gitbook/assets/statistics.PNG)

## Запуск
* Скачать проект

* Установить необходимые пакеты командой `pip install -r requirements.txt`

* Запустить командой `python main.py`

## Используемые библиотеки

* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - парсинг результатов со страницы выдачи

* [openpyxl](https://pypi.org/project/openpyxl/) - работа с `.xlsx` файлами

* [Pillow](https://pypi.org/project/Pillow/) - работа с изображениями

* [PyQt5](https://pypi.org/project/PyQt5/) - работа с графическим интерфейсом

* [requests](https://pypi.org/project/requests/) - запросы

* [selenium](https://pypi.org/project/selenium/) - имитация браузера
