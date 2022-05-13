'''
Ключевое слово self. Ключевое слово self ссылается на «текущий
экземпляр виджета». С его помощью можно, например, получить
значения свойств текущего виджета.
'''

from kivy. app import App
from kivy.lang import Builder

KV = '''
Button:
    text: 'Состояние кнопки – %s'% self.state
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()