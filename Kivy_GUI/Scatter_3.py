from kivy.app import App
from kivy.lang import Builder

KV = '''
RelativeLayout:
    canvas:
        Rectangle:
            source: './Images/Fon.jpg'
            size: self.size
            pos: self. pos
    Scatter:
        Image:
            source: './Images/forest.jpg'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()