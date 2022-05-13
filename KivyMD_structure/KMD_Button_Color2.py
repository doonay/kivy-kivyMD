from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd. uix. button import MDRectangleFlatButton
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '100'
        # self.theme_cls.primary_hue = '500'
        # self.theme_cls.primary_hue = '900'
        screen = MDScreen()
        screen.add_widget(MDRectangleFlatButton(text='Яркость кнопки', pos_hint= {'center_x': 0.5, 'center_y': 0.5}))
        return screen
MainApp().run()