from kivy. app import App
from kivy.lang import Builder
# создание текстовой строки
KV = «»»
GridLayout:
…… cols: 2
…… rows: 2
…… Button:
…… … … text: «Кнопка 1»
…… Button:
…… … … text: «Кнопка 2»
…… Button:
…….. … text: «Кнопка 3»
…… Button:
…… … … text: «Кнопка 4»
«»»
class MyApp (App):
    …… def build (self):
    …… … … return Builder. load_string (KV)
MyApp().run ()