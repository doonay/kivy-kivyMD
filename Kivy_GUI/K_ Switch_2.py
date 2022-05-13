'''
По умолчанию виджет является статичным с минимальным размером 83x32 пикселя.
– active – состояние выключателя (по умолчанию имеет значение False)
– on_touch_down – событие (касание выключателя);
– on_touch_up – событие (выключатель отпущен);
– on_touch_move – событие (касание выключателя с перемещением).
К сожалению, данный элемент не имеет свойства text, поэтому для размещения поясняющих надписей нужно в паре использовать метку Label
'''

from kivy.app import App
from kivy.lang import Builder

KV = '''
Switch:
    active: True
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()