#Листинг 5.53. Демонстрации работы класса MDDatePicker (модуль MDDatePicker1.py)
# модуль MDDatePicker1.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. picker import MDDatePicker
KV = '''
MDFloatLayout:
    MDToolbar:
        title: 'Компонента MDDatePicker'
        pos_hint: {'top': 1}
        elevation: 10
    MDRaisedButton:
        text: 'Открыть Date Picker'
        pos_hint: {'center_x':.5, 'center_y':.6}
        on_release: app.show_date_picker()
    MDLabel:
        id: date_label
        text: 'Итоги выбора даты!'
        halign: 'center'
'''
class Main(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_save(self, instance, value, date_range):
        self.root.ids. date_label. text = str(value)
        # self.root.ids. date_label. text = str(date_range)
    def on_cancel(self, instance, value):
        self.root.ids. date_label. text = 'Вы Нажали Cancel!'
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        # date_dialog = MDDatePicker(year=2016, month=4, day=12)
        # date_dialog = MDDatePicker(min_year=2015, max_year=2025)
        # date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=self. on_save, on_cancel=self. on_cancel)
        date_dialog. open()
Main().run()