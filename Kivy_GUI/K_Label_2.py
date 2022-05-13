'''
- text – текст, выводимый в видимую часть виджета (текстовое содержимое метки, надпись на кнопке и т.п.);
– font_size – размер шрифта;
– color – цвет шрифта;
– font_name – имя файла с пользовательским шрифтом (.ttf).
'''

from kivy.app import App
from kivy.lang import Builder

KV = '''
Label:
    text: 'Это текст'
    font_size: 50
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
