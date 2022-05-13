from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        Fl = FloatLayout()
        btn = Button(text='Кнопка', size_hint=(.3,.2), pos=(30, 30))
        Fl.add_widget (btn)
        return Fl

MyApp().run()