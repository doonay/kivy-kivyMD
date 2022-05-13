#Листинг 5.51. Демонстрации работы класса MDNavigationRail(модуль NaviRail_2.py)
# модуль NaviRail_2.py
from kivy. factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    size_hint_x: None
    #height: '120dp'
    text:' [size=10] Шарик [/size]'
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Навигационнная рейка'
        md_bg_color: rail.md_bg_color
        left_action_items: [['menu', lambda x: app.rail_open()]]
        MDBoxLayout:
            MDNavigationRail:
                id: rail
                md_bg_color: get_color_from_hex('#344954')
                color_normal: get_color_from_hex('#718089')
                color_active: get_color_from_hex('#f3ab44')
                use_resizeable: True
            MDNavigationRailItem:
                icon: 'language-cpp'
                text: 'C++'
            MDNavigationRailItem:
                icon: 'language-java'
                text: 'Java'
            MDNavigationRailItem:
                icon: 'language-swift'
                text: 'Swift'
            MDBoxLayout:
                padding: '24dp'
                ScrollView:
                    MDList:
                        id: box
                        cols: 2
                        spacing: '12dp'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def rail_open(self):
        if self.root.ids. rail. rail_state == 'open':
            self.root.ids. rail. rail_state = 'close'
        else:
            self.root.ids. rail. rail_state = 'open'
    def on_start(self):
        for i in range(4):
            tile = Factory.MyTile(source='./Images/Dog.jpg')
            self.root.ids.box.add_widget(tile)
MainApp().run()