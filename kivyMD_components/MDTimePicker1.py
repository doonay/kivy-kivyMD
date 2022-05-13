#Листинг 5.52. Демонстрации работы класса MDTimePicker (модуль MDTimePicker1.py)
# модуль MDTimePicker1.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. picker import MDTimePicker
from datetime import datetime
KV = '''
MDFloatLayout:
    MDRaisedButton:
        text: 'Открыть Time Picker'
        pos_hint: {'center_x':.5, 'center_y':.6}
        on_release: app.show_time_picker()
    MDLabel:
        id: time_label
        text: 'Итоги выбора времени!'
        halign: 'center'
'''
class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = 'Light'
        # self.theme_cls.primary_palette = 'BlueGray'
        return Builder. load_string(KV)
    # функция открытия диалогового окна
    def show_time_picker(self):
        # Задать время по умолчанию
        default_time = datetime.strptime('12:00:00',
                                         '%H:%M:%S').time()
        # создать объект time_dialog
        time_dialog = MDTimePicker()
        # Связать time_dialog с функциями обработки событий
        time_dialog.bind(on_cancel=self. on_cancel, time=self.get_time)
        # Задать время по умолчанию
        time_dialog.set_time(default_time)
        # открыть диалоговое окно
        time_dialog. open()
        # Получить время
    def get_time(self, instance, time):
        self.root.ids. time_label. text = str(time)
        # Нажато – Cancel
    def on_cancel(self, instance, time):
        self.root.ids. time_label. text = 'Вы Нажали Cancel!'
MainApp().run()