from kivy.app import App
from kivy.lang import Builder

KV = '''
<MyBut@Button>
	size_hint_y: None
	height: 40
ScrollView:
	do_scroll_x: False
	do_scroll_y: True
	GridLayout:
		cols: 1
		spacing: 10
		size_hint_y: None
		height: self. minimum_height
		MyBut:
            text: 'Кнопка 1'
		MyBut:
            text: 'Кнопка 2'
		MyBut:
		    text: 'Кнопка 3'
		MyBut:
		    text: 'Кнопка 4'
		MyBut:
		    text: 'Кнопка 5'
		MyBut:
		    text: 'Кнопка 6'
		MyBut:
		    text: 'Кнопка 7'
		MyBut:
		    text: 'Кнопка 8'
		MyBut:
		    text: 'Кнопка 9'
		MyBut:
		    text: 'Кнопка 10'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()