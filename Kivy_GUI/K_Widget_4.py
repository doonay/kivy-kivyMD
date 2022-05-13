'''
В этом модуле мы создали объект Widget, а для объекта canvas
в инструкцию Rectangle (рамка) загрузили изображение из файла
'./Images/Fon.jpg’. Инструкция Color (цвет) закомментирована, поэтому
изображение будет показано в оригинальном цвете. Если снять
комментарии с этих строк, то изображение пример красный оттенок.
– canvas – встроенный объект, имеющий инструкции (важно – пишется с маленькой буквы);
– Color – инструкция для задания цвета виджета (важно – пишется с большой буквы);
– rgba – свойство (цвет виджета), задается в формате r, g, b, a;
– Rectangle – инструкция для задания свойств рамки виджета (важно – пишется с большой буквы);
– source – источник (путь и имя файла с изображением, которое можно поместить в рамку);
– size – размер (указывается – self.size, иметь размер рамки, как у родительского виджета);
– pos – положение (указывается – self. pos, иметь положение рамки, как у родительского виджета).
'''

from kivy.app import App
from kivy.lang import Builder

KV = '''
Widget:
    canvas:
        #Color:
        #rgba: 1, 0, 0, 1
    Rectangle:
        source: './Images/Fon.jpg'
        pos: self. pos
        size: self.size
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()