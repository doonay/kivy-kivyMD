#Листинг 5.16. Демонстрации работы MDFloatingActionButtonSpeedDial(модуль FABSpeedDial.py)
# модуль FABSpeedDial.py
from kivymd.app import MDApp
from kivy.lang import Builder
KV = '''
MDScreen:
    MDFloatingActionButtonSpeedDial:
        # Свойства кнопок
        data: app. data # иконки на кнопках стека
        root_button_anim: True #повернуть корневую кнопку при нажатии
        #icon: 'language-python' #иконка на корневой кнопке
        #color_icon_root_button: 0,1,0,1 #цвет иконки корневой кнопки
        #bg_color_root_button: 1,0,0,1 #цвета фона иконки корневой кнопки
        #color_icon_stack_button: 0,1,0,1 #цвет иконок кнопок стека
        #bg_color_stack_button: 1,0,0,1 #цвета фона иконок кнопок стека
        #label_text_color: 1,0,0,1 #цвета текста кнопок стека
        # вызов функций обработки событий нажатия кнопок
        on_open: app. open() #нажата корневая кнопка
        on_close: app.close() #отжата корневая кнопка
        callback: app.call #нажата стековая кнопка
'''
class MainApp(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp'}
    def build(self):
        return Builder. load_string(KV)
    def open(self):
        print('Корневая кнопка раскрыта')
    def close(self):
        print('Корневая кнопка закрыта')
    def call(self, button):
        print('Нажата кнопка раскрытого стека')
        if button. icon == 'language-python':
            print('Кнопка Python')
        elif button. icon == 'language-php':
            print('Кнопка php')
        elif button. icon == 'language-cpp':
            print('Кнопка C++')
MainApp().run()