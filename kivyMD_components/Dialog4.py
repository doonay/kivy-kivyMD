#Листинг 5.25. Демонстрации работы класса MDDialog (модуль Dialog4.py)
# модуль Dialog4.py
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd. uix. button import MDFlatButton
from kivymd. uix. dialog import MDDialog
KV = '''
<Content>
    orientation: 'vertical'
    spacing: '12dp'
    size_hint_y: None
    height: '230dp'
    MDTextField:
        hint_text: 'Город'
    MDTextField:
        hint_text: 'Улица'
    MDTextField:
        hint_text: 'Дом'
    MDTextField:
        hint_text: 'Квартира'
MDFloatLayout:
    MDFlatButton:
        text: 'Вызов окна диалога'
        pos_hint: {'center_x':.5, 'center_y':.5}
        on_release: app.show_confirmation_dialog()
'''
class Content(BoxLayout):
    pass
class MainApp(MDApp):
    dialog = None
    def build(self):
        return Builder. load_string(KV)
    def show_confirmation_dialog(self):
        if not self. dialog:
            self. dialog = MDDialog(
                title='Введите адрес:',
                type='custom',
                size_hint_x=0.8,
                content_cls=Content(),
                buttons= [
                    MDFlatButton(text='Отменить', text_color=self.theme_cls.primary_color, on_release=self.closeDialog),
                    MDFlatButton(text='Принять', text_color=self.theme_cls.primary_color, on_release=self.ok_Dialog,),],)
            self. dialog. open()
    def ok_Dialog(self, inst):
        print('Нажата кнопка Принять')
        self. dialog. dismiss()
    def closeDialog(self, inst):
        self. dialog. dismiss()
MainApp().run()