#Листинг 5.38. Демонстрации работы класса MDList(модуль ListText2.py)
# модуль ListText2.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
ScrollView:
    MDList:
        OneLineListItem:
            text: 'Однострочный элемент'
            on_release: print('Нажата строка 1')
        TwoLineListItem:
            text: 'Двухстрочный элемент'
            secondary_text: 'Это вторая строк'
            on_release: print('Нажата строка 2')
        ThreeLineListItem:
            text: 'Трехстрочный элемент'
            secondary_text: 'Это вторая строк'
            tertiary_text: 'Это третья строк'
            on_release: print('Нажата строка 3')
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()