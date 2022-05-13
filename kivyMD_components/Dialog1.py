#Листинг 5.22. Демонстрации работы класса MDDialog (модуль Dialog1.py)
# модуль Dialog1.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. button import MDFlatButton
from kivymd. uix. dialog import MDDialog
KV = '''
MDFloatLayout:
    MDFlatButton:
        text: 'Вызов окна диалога'
        pos_hint: {'center_x':.5, 'center_y':.5}
        on_release: app.show_alert_dialog()
'''
class MainApp(MDApp):
    dialog = None
    def build(self):
        return Builder. load_string(KV)
    def show_alert_dialog(self):
        if not self. dialog:
            self. dialog = MDDialog(
                title='Сбросить настройки?',
                text='Это приведет к сбросу настроек по умолчанию',
            buttons= [MDFlatButton(text='НЕТ',
            text_color=self.theme_cls.primary_color,
                       on_release=self.closeDialog),
            MDFlatButton(text='ДА',
            text_color=self.theme_cls.primary_color,
                       on_release=self. ok_Dialog,),],)
            self. dialog. open()
    def ok_Dialog(self, inst):
        print('Нажата кнопка ДА')
        self. dialog. dismiss()
    def closeDialog(self, inst):
        print('Нажата кнопка НЕТ')
        self. dialog. dismiss()
MainApp().run()