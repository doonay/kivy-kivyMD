# модуль MDSlider1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDBoxLayout:
        MDSlider:
            id: slider
            min: 0
            max: 100
            step: 1
            #orientation: 'vertical'
        MDLabel:
            text: str(slider.value)
'''
class MainApp(MDApp):
    def build(self):
        self.root = Builder. load_string(KV)
MainApp().run()