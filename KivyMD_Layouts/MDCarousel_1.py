#Листинг 4.10.Демонстрация работы виджета MDCarousel
#(модуль – MDCarousel_1.py)
# модуль MDCarousel_1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDCarousel:
	direction: 'right'
	loop: True
	BoxLayout:
		Image:
			source: './Images/Margaritta.jpg'
	BoxLayout:
		Image:
			source: './Images/Crudo.jpg'
	BoxLayout:
		Image:
			source: './Images/Marinara.jpg'
	BoxLayout:
		Image:
			source: './Images/Carbonara.jpg'
'''
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()