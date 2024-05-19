from PySide6 import QtWidgets
from form_weather import Ui_FormWeather
from a_threads import WeatherHandler


class WindowWeather(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_s = Ui_FormWeather()
        self.ui_s.setupUi(self)
        self.ui_s.radioButton3.setChecked(True)
        self.ui_s.radioButton3.clicked.connect(self.updateDelay)
        self.ui_s.radioButton5.clicked.connect(self.updateDelay)
        self.ui_s.radioButton10.clicked.connect(self.updateDelay)

        self.ui_s.pushButtonGetData.clicked.connect(self.getData)
        self.ui_s.pushButtonStopGetData.clicked.connect(self.stopGetData)

        self.ui_s.lineEditLatitude.setPlaceholderText("59.9386")
        self.ui_s.lineEditLongitude.setPlaceholderText("30.3141")

    def getData(self):
        WindowWeather.lat = float(self.ui_s.lineEditLatitude.text())
        WindowWeather.lon = float(self.ui_s.lineEditLongitude.text())
        self.WeatherHandler = WeatherHandler(WindowWeather.lat, WindowWeather.lon)
        self.WeatherHandler.setStatus(True)
        self.WeatherHandler.weatherInfoReceived.connect(self.upgradeWeatherInfo)
        self.WeatherHandler.started.connect(lambda: print("Старт потока"))
        self.WeatherHandler.finished.connect(lambda: print("Конец потока"))

        self.ui_s.textEditData.clear()
        self.ui_s.pushButtonGetData.setEnabled(False)
        self.ui_s.pushButtonStopGetData.setEnabled(True)
        self.ui_s.lineEditLatitude.setEnabled(False)
        self.ui_s.lineEditLongitude.setEnabled(False)
        self.ui_s.radioButton3.setEnabled(False)
        self.ui_s.radioButton5.setEnabled(False)
        self.ui_s.radioButton10.setEnabled(False)
        self.WeatherHandler.start()

    def updateDelay(self):
        if self.ui_s.radioButton3.isChecked():
            self.WeatherHandler.setDelay(3)
        elif self.ui_s.radioButton5.isChecked():
            self.WeatherHandler.setDelay(5)
        elif self.ui_s.radioButton10.isChecked():
            self.WeatherHandler.setDelay(10)

    def stopGetData(self):
        self.WeatherHandler.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)
        self.ui_s.lineEditLatitude.setEnabled(True)
        self.ui_s.lineEditLongitude.setEnabled(True)
        self.ui_s.radioButton3.setEnabled(True)
        self.ui_s.radioButton5.setEnabled(True)
        self.ui_s.radioButton10.setEnabled(True)

    def upgradeWeatherInfo(self, weather_data):
        latitude = weather_data['latitude']
        longitude = weather_data['longitude']
        currentTime = weather_data['current_weather']['time']
        temperature = weather_data['current_weather']['temperature']
        winddirection = weather_data['current_weather']['winddirection']
        windspeed = weather_data['current_weather']['windspeed']
        self.ui_s.textEditData.append(f"Широта: {latitude}, Долгота: {longitude}")
        self.ui_s.textEditData.append(f"Время: {currentTime}")
        self.ui_s.textEditData.append(f"Температура: {temperature}°C")
        self.ui_s.textEditData.append(f"Направление ветра: {winddirection}")
        self.ui_s.textEditData.append(f"Скорость ветра: {windspeed} м/c")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()
