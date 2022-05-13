'''
У данного класса есть встроенный объект canvas, который можно использовать для рисования на экране.
Данный объект может принимать события и реагировать на них.
Кроме того, у данного встроенного объекта есть две важные инструкции: Color (цвет) и Rectangle (прямоугольник, рамка).
С использованием данных инструкций для созданной поверхности можно задать цвет, или поместить на нее изображение.
'''

from kivy.app import App
from kivy.lang import Builder

KV = '''
Widget:
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self. pos
            size: self.size
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()