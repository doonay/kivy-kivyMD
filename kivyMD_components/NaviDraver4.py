#Листинг 5.49. Демонстрации работы класса MDNavigationDrawer(модуль NaviDrawer4.py)
# модуль NaviDraver4.py
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
KV = '''
# Пункты меню в выдвижной панели.
<ItemDrawer>:
    theme_text_color: 'Custom'
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root. icon
        theme_text_color: 'Custom'
        text_color: root.text_color
# Содержимое выдвижной панели
<ContentNavigationDrawer>:
    orientation: 'vertical'
    padding: '8dp'
    spacing: '8dp'
    AnchorLayout:
        anchor_x: 'left'
        size_hint_y: None
        height: avatar.height
        Image:
            id: avatar
            size_hint: None, None
            size: '56dp', '56dp'
            source: './Images/kivymd.jpg'
            #source: 'data/logo/kivy-icon-256.png'
    MDLabel:
        text: 'Библиотека KivyMD'
        #font_style: 'Button'
        adaptive_height: True
    MDLabel:
        text: 'https://kivymd.readthedocs.io/en/0.104.2/'
        font_style: 'Caption'
        adaptive_height: True
    ScrollView:
        DrawerList:
            id: md_list
# Содержимое главного экрана
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Выдвижная панель'
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                Widget:
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                id: content_drawer
'''
class ContentNavigationDrawer(MDBoxLayout):
    pass
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))
class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Вызывается при касании элемента панели'''
        # Задает цвет иконки и текста элемента панели
        for item in self.children:
            if item. text_color == self.theme_cls.primary_color:
                item. text_color = self.theme_cls. text_color
                break
        instance_item. text_color = self.theme_cls.primary_color

class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_start(self):
        icons_item = {'folder': 'Мои файлы',
                'music-box': 'Музыка',
                'phone-classic': 'Телефоны',
                'folder-image': 'Изображения',
                'email': 'Адреса',
                'folder-text': 'Документы', }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name,
                text=icons_item [icon_name]))
MainApp().run()