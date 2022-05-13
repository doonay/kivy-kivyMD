#Листинг 5.50. Демонстрации работы класса MDNavigationRail(модуль NaviRail_1.py)
# модуль NaviRail_1.py
from kivy. factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. dialog import MDDialog
KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<MyTile@SmartTileWithStar>
    size_hint_y: None
    size_hint_x: None
    # height: '140dp'
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Навигационнная рейка'
        md_bg_color: rail.md_bg_color
    MDBoxLayout:
        #навигационная рейка
        MDNavigationRail:
            id: rail
            md_bg_color: get_color_from_hex('#344954')
            color_normal: get_color_from_hex('#718089')
            color_active: get_color_from_hex('#f3ab44')
            #элементы навигационной рейки
            MDNavigationRailItem:
                icon: 'language-cpp'
                text: 'C++'
                on_press: app.press_icon('C++')
            MDNavigationRailItem:
                icon: 'language-python'
                text: 'Python'
                on_press: app.press_icon('Python')
            MDNavigationRailItem:
                icon: 'language-swift'
                text: 'Swift'
                on_press: app.press_icon('Swift')
        MDBoxLayout:
            padding: '5dp'
            ScrollView:
                MDList:
                    id: box
                    cols: 2
                    spacing: '5dp'
'''


class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_start(self):
        for i in range(8):
            tile = Factory.MyTile(source='./Images/kivymd.jpg')
            tile.stars = 2
            self.root.ids.box.add_widget(tile)

    def press_icon(self, text_item):
        dialog = MDDialog(text='Выбрано ' + text_item)
        dialog. open()


MainApp().run()