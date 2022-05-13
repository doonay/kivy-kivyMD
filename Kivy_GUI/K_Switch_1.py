'''
Виджет Switch действует как кнопка – выключатель.
При этом имитируется механический выключатель, который либо включается, либо выключается.
Виджет Switch имеет два положения включено (on) – выключено (off).
Когда пользователь касается кнопки, она переходит из одного положения в другое.
'''

from kivy.app import App
from kivy.uix.switch import Switch

class MainApp(App):
    def build(self):
        sw = Switch(active=True)
        return sw

MainApp().run()