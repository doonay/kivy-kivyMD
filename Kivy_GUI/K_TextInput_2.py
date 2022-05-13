'''
– text – текст (текстовое содержимое поля ввода.);
– font_size – размер шрифта;
– color – цвет шрифта;
– font_name – имя файла с пользовательским шрифтом (.ttf);
– password – скрывать вводимые символы (при значении свойства
True);
– password_mask – маска символа (символ, который скрывает
вводимый текст).
'''
# модуль K_TextInput_2.py
from kivy. app import App
from kivy.lang import Builder
KV = «»»
…… TextInput:
…… font_size: 30
«»»
class MainApp (App):
    …… def build (self):
    …… …… return Builder. load_string (KV)
MainApp().run ()