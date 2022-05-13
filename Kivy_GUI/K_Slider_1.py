'''
– orientation=’vertical’ – вертикальная ориентация;
– value_track=True – показать след бегунка;
– value_track_color= (1, 0, 0, 1) – задан цвет следа бегунка (красный).
'''
from kivy. app import App
from kivy.uix.slider import Slider

class MainApp(App):
    def build(self):
        slide = Slider (orientation='vertical', value_track=True, value_track_color= (1, 0, 0, 1))
        return slide

MainApp().run()