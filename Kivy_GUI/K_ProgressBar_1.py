'''
– max=1000 – максимальное значение шкалы бегунка;
– value = 650 – текущее положение на шкале бегунка.
'''
from kivy. app import App
from kivy.uix.progressbar import ProgressBar
class MainApp (App):
    …… def build (self):
    …… …… Progress = ProgressBar (max=1000)
…… …… Progress.value = 650
…… …… return Progress
MainApp().run ()