#Листинг 5.27. Демонстрации работы класса MDExpansionPanel(модуль ExpansionPanel.py)
# модуль ExpansionPanel.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd. uix. expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
KV = '''
<Content>
    adaptive_height: True
    TwoLineIconListItem:
        text: '+7 915-123-45-67'
        secondary_text: 'Мобильный тел.'
        IconLeftWidget:
            icon: 'phone'
ScrollView:
    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: True
'''
class Content(MDBoxLayout):
    '''# Здесь можно разместить пользовательский контент'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon='./Images/icon1.jpg',
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text='Заголовок панели',
                        secondary_text='Вторая строка панели',
                        tertiary_text='Третья строка панели', )))
MainApp().run()