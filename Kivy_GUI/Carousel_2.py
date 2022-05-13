from kivy.lang import Builder
from kivy.app import App

KV = '''
Carousel:
    direction: 'right'
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: './Images/Margaritta.jpg'
    BoxLayout:
        Image:
            source: './Images/Marinara.jpg'
    BoxLayout:
        Image:
            source: './Images/Montanara.jpg'
    BoxLayout:
        Image:
            source: './Images/Napoletana.jpg'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()