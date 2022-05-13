#Листинг 5.56. Демонстрации работы класса MDProgressBar (модуль MDProgressBar2.py)
# модуль MDProgressBar2
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    name: 'progress bar'
    MDToolbar:
        title: 'Компонента MDProgressBar'
        pos_hint: {'top': 1}
        elevation: 10
    MDBoxLayout:
        orientation: 'vertical'
        padding: '4dp'
        MDLabel:
            text: 'Смените положение Слайдера'
            halign: 'center'
        MDSlider:
            id: progress_slider
            min: 0
            max: 100
            value: 40
            hint: False
        MDProgressBar:
            reversed: True
            value: progress_slider.value
        BoxLayout:
            MDProgressBar:
                orientation: 'vertical'
                reversed: True
                value: progress_slider.value
            MDProgressBar:
                orientation: 'vertical'
                value: progress_slider.value
'''
class MainApp(MDApp):
    def build(self):
        self.root = Builder. load_string(KV)
MainApp().run()