'''
– source – источник (путь к файлу и имя видео файла)
– play – проигрывать (по умолчанию False, для запуска проигрывания установить -True);
– state – состояние (имеет три значения: play – проигрывать, pause – поставить на паузу, stop – остановить);
– volume – громкость звука, значение в диапазоне 0—1 (1 – полная громкость, 0 – отключение звука).
'''
from kivy.app import App
from kivy.lang import Builder

KV = '''
Video:
    source: './Video/My_video.mp4'
    play: True
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()