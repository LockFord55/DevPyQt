"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
import requests as requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # Экземпляр класса Signal с переданным ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:  # Переопределенный метод run
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()  # Загрузка CPU в %
            ram_value = psutil.virtual_memory().percent  # Загрузка RAM в %
            self.systemInfoReceived.emit([cpu_value, ram_value])  # С помощью метода .emit() передаем в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)


class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 3
        self.__status = None

    def setDelay(self, delay) -> None:
        self.__delay = delay

    def setStatus(self, val):
        self.__status = val


    def run(self) -> None:
        while self.__status:
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherInfoReceived.emit(data)
            time.sleep(self.__delay)
