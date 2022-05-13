#Листинг 5.66. Демонстрации работы класса MDSlider (модуль MDSlider2.py)
# модуль MDSlider2.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: '8dp'
        MDSlider:
            id: slider1
            min: 0
            max: 100
            step: 1
            hint: False
            on_touch_up: app.slider_value(self)
        MDLabel:
            text: str(slider1.value)
        MDSlider:
            id: slider2
            min: 0
            max: 100
            on_touch_up: app.slider_value(self)
        MDLabel:
            text: str(slider2.value)
        MDSlider:
            id: slider3
            min: 0
            max: 100
            step: 1
            color: app.theme_cls.accent_color
            on_touch_up: app.slider_value(self)
        MDLabel:
            text: str(slider3.value)
'''
class MainApp(MDApp):
    def build(self):
        self.root = Builder. load_string(KV)
    def slider_value(self, instance):
        if instance.active:
            print('Значение -', instance.value)
MainApp().run()