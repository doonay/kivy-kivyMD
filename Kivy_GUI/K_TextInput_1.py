from kivy. app import App
from kivy. uix. textinput import TextInput
class MainApp (App):
    …… def build (self):
    …… … … my_text = TextInput (font_size=30)
…… … … return my_text
MainApp().run ()