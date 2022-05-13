#Листинг 5.74. Демонстрации работы класса MDTextField(модуль MDTextField.py)
# модуль MDTextField1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
BoxLayout:
    orientation: 'vertical'
    MDTextField:
        hint_text: 'Введите текст'
    MDTextField:
        hint_text: 'Дата рождения'
        helper_text: 'дд/мм/гггг'
        helper_text_mode: 'on_focus'
    MDTextField:
        hint_text: 'Введите ФИО'
        helper_text: 'Фамилия Имя Отчество'
        helper_text_mode: 'persistent'
    MDTextField:
        hint_text: 'Max. символов- 5'
        max_text_length: 5
    MDTextField:
        hint_text: 'Прямоугольный режим'
        mode: 'rectangle'
    MDTextField:
        multiline: True
        hint_text: 'Это многострочный текст'
    MDTextField:
        hint_text: 'Режим заполнения'
        mode: 'fill'
        fill_color: 0, 0, 0,.1
    MDTextField:
        hint_text: 'Задать цвет линии'
        line_color_normal: app.theme_cls.accent_color
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()