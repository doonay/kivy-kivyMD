from kivy. app import App
from kivy.lang import Builder
# создание текстовой строки
KV = '''
FloatLayout:
    Button:
        text: 'Кнопка 1'
        size_hint:.2,.1
        pos_hint: {'center_x':.1, 'center_y':.1}
    Button:
        text: 'Кнопка2'
        size_hint:.3,.2
        pos_hint: {'center_x':.5, 'center_y':.15}
    Button:
        text: 'Кнопка 3'
        size_hint:.3,.2
        pos_hint: {'center_x':.5, 'center_y':.5}
    Button:
        text: 'Кнопка 4'
        size_hint:.2,.1
        pos_hint: {'center_x':.8, 'center_y':.8}
'''
class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()
