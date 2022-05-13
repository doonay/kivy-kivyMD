#Листинг 5.63. Демонстрации работы класса MDSelectionList (модуль MDSelectionList2.py)
# модуль MDSelectionList2.py
from kivy.animation import Animation
from kivy.lang import Builder
from kivy. utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.utils.fitimage import FitImage
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: app.theme_cls.bg_light
    MDToolbar:
        id: toolbar
        title: 'Изображения'
        left_action_items: [['menu']]
        right_action_items: [['magnify'], ['dots-vertical']]
        md_bg_color: app.theme_cls.bg_light
        specific_text_color: 0, 0, 0, 1

    MDBoxLayout:
        padding: '24dp', '4dp', 0, '4dp'
        adaptive_size: True
        MDLabel:
            text: 'Собачки'
            adaptive_size: True
    ScrollView:
        MDSelectionList:
            id: selection_list
            padding: '24dp', 0, '24dp', '24dp'
            cols: 3
            spacing: '12dp'
            overlay_color: app. overlay_color [:-1] + [.2]
            icon_bg_color: app. overlay_color
            progress_round_color:
                app.progress_round_color
            on_selected: app. on_selected(*args)
            on_unselected: app. on_unselected(*args)
            on_selected_mode: app.set_selection_mode(*args)
'''

class MainApp(MDApp):
    overlay_color = get_color_from_hex('#6042e4')
    progress_round_color = get_color_from_hex('#ef514b')
    def build(self):
        return Builder. load_string(KV)
    def on_start(self):
        for i in range(9):
            self.root.ids.selection_list.add_widget(
                FitImage(source='./Images/Dog.jpg', size_hint_y=None, height='140dp', ))
    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self. overlay_color
            left_action_items = [['close', lambda x:self.root.ids.selection_list.unselected_all(),]]
            right_action_items = [['trash-can'],['dots-vertical']]
        else:
            md_bg_color =(1, 1, 1, 1)
            left_action_items = [['menu']]
            right_action_items = [['magnify'], ['dots-vertical']]
        self.root.ids.toolbar. title = 'Изображения'
        Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
        self.root.ids.toolbar. left_action_items = left_action_items
        self.root.ids.toolbar. right_action_items = right_action_items
    def on_selected(self, instance_selection_list, instance_selection_item):
        self.root.ids.toolbar. title = str(len(instance_selection_list.get_selected_list_items()))
    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.root.ids.toolbar. title = str(len(instance_selection_list.get_selected_list_items()))
MainApp().run()