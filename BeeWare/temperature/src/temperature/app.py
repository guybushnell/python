"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

class Temperature(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """    
        c_box = toga.Box()
        f_box = toga.Box()
        box = toga.Box()

        c_input = toga.TextInput(readonly=True)
        f_input = toga.TextInput()

        c_label = toga.Label("Celsius", style=Pack(text_align=LEFT))
        f_label = toga.Label("Fahrenheit", style=Pack(text_align=LEFT))
        join_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

        def calculate(widget):
            try:
                c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0
            except ValueError:
                c_input.value = "???"

        button = toga.Button("Calculate", on_press=calculate)

        f_box.add(f_input)
        f_box.add(f_label)

        c_box.add(join_label)
        c_box.add(c_input)
        c_box.add(c_label)

        box.add(f_box)
        box.add(c_box)
        box.add(button)

        box.style.update(direction=COLUMN, padding=10)
        f_box.style.update(direction=ROW, padding=5)
        c_box.style.update(direction=ROW, padding=5)

        c_input.style.update(flex=1)
        f_input.style.update(flex=1, padding_left=210)
        c_label.style.update(width=100, padding_left=10)
        f_label.style.update(width=100, padding_left=10)
        join_label.style.update(width=200, padding_right=10)

        button.style.update(padding=15)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()


def main():
    return Temperature()
