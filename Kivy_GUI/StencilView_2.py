from kivy.app import App
from kivy.lang import Builder

KV = '''
StencilView:
	Scatter:
		Image:
		    source: './Images/Fon.jpg'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()