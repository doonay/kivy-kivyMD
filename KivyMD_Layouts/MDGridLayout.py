#Листинг 4.4.Демонстрации работы класса MDGridLayou (модуль MDGridLayou.py)
# модуль MDGridLayout.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDGridLayout:
	cols: 1
	rows: 3
	#padding: '10dp' # отступ контейнера от верхнего угла окна
	#pos_hint: {'center_x': 0.5, 'center_y':.5} # положение конт-ра
	#adaptive_height: True # разрешить адаптацию по высоте
	#adaptive_width: True # разрешить адаптацию по ширине
	#adaptive_size: True # разрешить адаптацию по ширине и выс.
	#spacing: '10dp' # расстояние между элементами контейнера
	MDRaisedButton:
		text: 'Это кнопка 1'
	MDRaisedButton:
		text: 'Это кнопка 2'
	MDRaisedButton:
		text: 'Это кнопка 3'
'''
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
MyApp().run()