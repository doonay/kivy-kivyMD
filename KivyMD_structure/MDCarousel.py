from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.carousel import MDCarousel

class MainApp(MDApp):
    def build(self):
        # создать объект
        carousel = MDCarousel(direction='right')
        img = Image(source='./Images/Gorox.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Ganna.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Flora.jpg')
        carousel.add_widget(img)
        img = Image(source='. /Images/Victoria.jpg')
        carousel.add_widget(img)
        return carousel

MainApp().run()