#Листинг 5.24. Демонстрации работы класса MDDialog (модуль Dialog3.py)
# модуль Dialog3.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. button import MDFlatButton
from kivymd. uix. dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
KV = '''
<ItemConfirm>
    on_release: root.set_icon(check)
    CheckboxLeftWidget:
        id: check
        group: 'check'
MDFloatLayout:
    MDFlatButton:
        text: 'Вызов окна диалога'
        pos_hint: {'center_x':.5, 'center_y':.5}
        on_release: app.show_confirmation_dialog()
'''
class ItemConfirm(OneLineAvatarIconListItem):
    divider = None
    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check!= instance_check:
                check.active = False
class MainApp(MDApp):
    dialog = None
    def build(self):
        return Builder. load_string(KV)
    def show_confirmation_dialog(self):
        if not self. dialog:
            self. dialog = MDDialog(
                title='Мелодия звонка',
                type='confirmation',
                size_hint_x=0.8,
                items= [
                    ItemConfirm(text='Callisto'),
                    ItemConfirm(text='Luna'),
                    ItemConfirm(text='Night'),
                    ItemConfirm(text='Solo'),
                    ItemConfirm(text='Phobos'),
                    ItemConfirm(text='Diamond'),
                    ItemConfirm(text='Sirena'),
                    ItemConfirm(text='Red music'),
                    ItemConfirm(text='Allergio'),
                    ItemConfirm(text='Magic'),
                    ItemConfirm(text='Tic-tac'),],
                buttons= [
                    MDFlatButton(text='Отменить', text_color=self.theme_cls.primary_color,on_release=self.closeDialog,),
                    MDFlatButton(text='Принять', text_color=self.theme_cls.primary_color, on_release=self.ok_Dialog,),],)
            self. dialog. open()
    def ok_Dialog(self, items):
        print('Нажата кнопка Принять')
        self. dialog. dismiss()
    def closeDialog(self, inst):
        print('Нажата кнопка Отменить')
        self. dialog. dismiss()
MainApp().run()