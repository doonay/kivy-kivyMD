from kivy.app import App
from kivy.uix.image import Image

class MainApp (App):
    def build (self):
        img = Image(source='./Images/Fon2.jpg')
        return img

MainApp().run ()