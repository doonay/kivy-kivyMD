'''
Ключевое слово ids.
Ключевые слова ids (идентификаторы) и id (идентификатор) используются для идентификации виджетов.
С использованием ключевого слова id можно любому виджету назначить уникальное имя (идентификатор).
Это имя можно использовать для ссылок на виджет, то есть обратиться к нему в коде на языке KV.
'''

from kivy. app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        id: bt1
        text: 'Кнопка 1'
        on_press: lb1.text = bt1.text
    Button:
        id: bt2
        text: 'Кнопка 2'
        on_press: lb1.text = bt2.text
    Label:
        id: lb1
        text: 'Метка'
        on_touch_down: self.text = 'Метка'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()