'''
– source – источник (путь к файлу для загрузки изображения);
– color – цвет изображения (в формате r, g, b, a), можно использовать
для «подкрашивания» изображения.

Этот виджет имеет подкласс AsyncImage, который позволяет
загрузить изображение асинхронно (например, из интернета с вебсайта). Это может быть полезно, поскольку не блокирует приложение
в ожидании загрузки изображения (оно загружается в фоновом
потоке)
'''

from kivy. app import App
from kivy.lang import Builder

KV = '''
Image:
    source: './Images/Fon2.jpg'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()