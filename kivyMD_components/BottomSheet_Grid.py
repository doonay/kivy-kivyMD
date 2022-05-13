#Листинг 5.5. Демонстрации работы BottomSheets(модуль BottomSheet_Grid.py)
# модуль BottomSheet_Grid.py
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.app import MDApp
KV = '''
Screen:
    MDToolbar:
        title: 'Пример BottomSheet'
        pos_hint: {'top': 1}
        elevation: 10
    MDRaisedButton:
        text: 'Открыть в виде таблицы'
        on_release: app.show_example_grid_bottom_sheet()
        pos_hint: {'center_x': .5, 'center_y': .5}
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def callback_for_menu_items(self, *args):
        toast(args [0])
    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {'Facebook': 'facebook', 'YouTube': 'youtube',
                'Twitter': 'twitter', 'Cloud': 'cloud-upload',
                'Камера': 'camera', }
        for item in data.items():
            bottom_sheet_menu.add_item(item [0],
                                       lambda x, y=item [0]:
                                       self.callback_for_menu_items(y),
                                       icon_src=item [1],)
            bottom_sheet_menu. open()
MainApp().run()