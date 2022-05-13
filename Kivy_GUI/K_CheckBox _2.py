'''
– color – цвет флажка (в формате r, g,b,a);
– active – состояние в виде логического значения (True – когда флажок поставлен, False – когда флажок снят)
'''

from kivy.app import App
from kivy.lang import Builder

KV = '''
CheckBox:
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()