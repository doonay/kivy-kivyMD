#Листинг 5.39. Демонстрации работы класса MDList(модуль ListText3.py)
# модуль ListText3.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. dialog import MDDialog
KV = '''
ScrollView:     
    MDList:
        OneLineAvatarListItem:
            text: 'Однострочный + аватар'
            on_release: app.dialog1()
            ImageLeftWidget:
                source: './Images/Alex.jpg'
        TwoLineAvatarListItem:
            text: 'Двухстрочный + аватар'
            secondary_text: 'Вторая строка'
            on_release: app.dialog2()
            ImageLeftWidget:
                source: './Images/Anna.jpg'
        ThreeLineAvatarListItem:
            text: 'Двухстрочный + аватар'
            secondary_text: 'Вторая строка'
            tertiary_text: 'Третья строка'
            ImageLeftWidget:
                source: './Images/Anna1.jpg'
        OneLineIconListItem:
            text: 'Однострочный + иконка'
            on_release: app.dialog3()
            IconLeftWidget:
                icon: 'language-python'
        TwoLineIconListItem:
            text: 'Двухстрочный + иконка'
            secondary_text: 'Вторая строка'
            IconLeftWidget:
                icon: 'language-php'
        ThreeLineIconListItem:
            text: 'Трехстрочный + иконка'
            secondary_text: 'Вторая строка'
            tertiary_text: 'Третья строка'
            IconLeftWidget:
                icon: 'language-csharp'
        OneLineAvatarIconListItem:
            text: '1 строка + 2 иконки'
            on_release: app.dialog4()
            IconLeftWidget:
                icon: 'plus'
                on_release: app.dialog5()
            IconRightWidget:
                icon: 'minus'
                on_release: app. dialog6()
        TwoLineAvatarIconListItem:
            text: '2 строки +2 иконки'
            secondary_text: 'Вторая строка'
            IconLeftWidget:
                icon: 'language-csharp'
            IconRightWidget:
                icon: 'language-cpp'
        ThreeLineAvatarIconListItem:
            text: '3 строки +2 иконки'
            secondary_text: 'Вторая строка'
            tertiary_text: 'Третья строка'
            IconLeftWidget:
                icon: 'library'
            IconRightWidget:
                icon: 'license'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def dialog1(self):
        dialog = MDDialog(text='Однострочный + аватар')
        dialog. open()
    def dialog2(self):
        dialog = MDDialog(text='Двухстрочный + аватар')
        dialog. open()
    def dialog3(self):
        dialog = MDDialog(text='Однострочный + иконка')
        dialog. open()
    def dialog4(self):
        dialog = MDDialog(text='Однострочный +2 иконки')
        dialog. open()
    def dialog5(self):
        dialog = MDDialog(text='Нажата левая иконка')
        dialog. open()
    def dialog6(self):
        dialog = MDDialog(text='Нажата правая иконка')
        dialog. open()

MainApp().run()