from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        btn = Button(text='Кнопка', size_hint=(.3, .2))
        layout.add_widget(btn)
        return layout

MyApp().run()
