from kivy.app import App
from kivy.lang import Builder

KV = '''
<MyBut@Button>
	font_size: 20
	size_hint:.5,.5
StackLayout:
	orientation: 'tb-rl'
	padding: 50, 100
	spacing: 10
	MyBut:
		text: 'B1'
	MyBut:
		text: 'B2'
	MyBut:
		text: 'B3'
	MyBut:
		text: 'B4'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()