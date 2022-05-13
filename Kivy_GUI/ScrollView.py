from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class MainApp(App):
    def build(self):
        # создание контейнера – таблица
        layout = GridLayout (cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        # размещение в таблице 20 кнопок
        for i in range (20):
            btn = Button (text=str (i), size_hint_y=None, height=40)
            layout.add_widget (btn)
        # Создание окна (контейнера) с областью прокрутки
        win_scrol = ScrollView (size_hint=(1, None), size=(Window.width, Window.height))
        # размещение в окне прокрутки таблицы с кнопками
        win_scrol.add_widget(layout)
        return win_scrol

MainApp().run()