"""
A simple weather app.
"""
from pprint import pprint
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT
import httpx

TOKEN = "" #Enter your weatherstack.com token here.

BASE_URL="http://api.weatherstack.com/current"

class weatherman(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        location_label = toga.Label("Location", style=Pack(padding=(0, 5)))
        self.location_input = toga.TextInput(style=Pack(flex=1))

        location_box = toga.Box(style=Pack(direction=ROW, padding=5))
        location_box.add(location_label)
        location_box.add(self.location_input)

        weather_box_label = toga.Label("Weather Results", style=Pack(padding=(0, 5)))
        self.weather_box_input = toga.TextInput(readonly=True, style=Pack(flex=1))
        weather_box = toga.Box(style=Pack(direction=ROW, padding=5))
        weather_box.add(weather_box_label)
        weather_box.add(self.weather_box_input)

        button = toga.Button("Fetch weather", on_press=self.weather, style=Pack(padding=5))

        main_box.add(location_box)
        main_box.add(button)
        main_box.add(weather_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def weather(self, widget):
        params = dict(access_key=TOKEN, query=self.location_input.value)
        resp = httpx.get(BASE_URL, params=params).json()
        try:
            self.weather_box_input.value = f'The weather report for  {resp["request"]["query"]} \
            {resp["current"]["temperature"]}  \
            {resp["current"]["weather_descriptions"][0]} \
            {resp["current"]["feelslike"]}'
        except ValueError:
            self.weather_box_input.value = "Location unknown!"



def main():
    return weatherman()