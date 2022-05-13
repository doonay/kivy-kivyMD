from kivymd.app import MDApp
from kivy.lang import Builder
'''
Здесь мы выполнили импорт всего двух модулей(MDApp — из библиотеки KivyMD и Builder – из фреймворка Kivy).
Далее задали текстовую строку KV, в которую поместили две компоненты: заголовок (MDToolbar) и кнопку(MDRaisedButton).
В заголовке расположили иконку(меню) и текст с названием приложения.
В функции build базового класса приложения выполнили всего одно действие – с помощью метода Builder.
load_string загрузили содержание строки KV для выполнения.
Как видно из данного листинга, текст программы достаточно компактный и удобно читается.
'''

KV = '''
Screen:
    MDToolbar:
        title: 'Приложение на KivyMD'
        elevation: 10
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: x]]
        pos_hint: {'top': 1}
    MDRaisedButton:
        text: 'Кнопка KivyMD'
        pos_hint: {'center_x': .5, 'center_y': .5}
'''
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()