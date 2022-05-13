from kivy. app import App
from kivy. uix. button import Button
from kivy.uix.gridlayout import GridLayout
class MyApp (App):
    …… def build (self):
    …… … … grid = GridLayout (cols=2, rows=2)
…… … … btn1 = Button (text=«Кнопка 1»)
…… … … btn2 = Button (text=«Кнопка 2»)
…… … … btn3 = Button (text=«Кнопка 3»)
…… … … btn4 = Button (text=«Кнопка 4»)
…… … … grid.add_widget (btn1)
…… … … grid.add_widget (btn2)
…… … … grid.add_widget (btn3)
…… … … grid.add_widget (btn4)
…… return grid
MyApp().run ()