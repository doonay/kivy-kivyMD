from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # создать объект
        carousel = Carousel(direction='right')
        img = Image(source='./Images/Angelika.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Elena.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Flora.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Fortuna.jpg')
        carousel.add_widget(img)
        return carousel

MainApp().run()