# Листинг 5.76. Демонстрации работы класса MDTextFieldRound(модуль MDTextFieldRound.py)
# модуль MDTextFieldRound.py
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDTextFieldRound :
        hint_text: 'Введите текст'
        width: 300
        size_hint_x: None
        pos_hint: {'center_x': .5}
    MDTextFieldRound :
        hint_text: 'Поле с одной иконкой'
        icon_left: 'email'
        width: 300
        size_hint_x: None
        pos_hint: {'center_x': .5}
    MDTextFieldRound :
        hint_text: 'Поле с двумя иконками'
        icon_left: 'key-variant'
        icon_right: 'eye-off'
        width: 300
        size_hint_x: None
        pos_hint: {'center_x': .5}
    MDTextFieldRound :
        hint_text: 'Поле с указанием цвета'
        icon_left: 'key-variant'
        normal_color: app.theme_cls.accent_color
        width: 300
        size_hint_x: None
        pos_hint: {'center_x': .5}
    MDTextFieldRound :
        hint_text: 'Изменение активного цвета'
        icon_left: 'key-variant'
        color_active: 0, 1, 0, 1
        width: 300
        size_hint_x: None
        pos_hint: {'center_x': .5}
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()
