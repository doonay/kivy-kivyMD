from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(text='Привет от KivyMD!', halign='center')

app = MainApp()
app.run()