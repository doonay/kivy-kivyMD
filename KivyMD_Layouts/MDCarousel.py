#Листинг 4.9.Демонстрация работы виджета MDCarousel (модуль – MDCarousel.py)
# модуль MDCarousel.py
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.carousel import MDCarousel
class MainApp(MDApp):
    def build(self):
        # создать объект
        carousel = MDCarousel(direction='right')
        img = Image(source='./Images/Margaritta.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Crudo.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Marinara.jpg')
        carousel.add_widget(img)
        img = Image(source='./Images/Carbonara.jpg')
        carousel.add_widget(img)
        return carousel
MainApp().run()