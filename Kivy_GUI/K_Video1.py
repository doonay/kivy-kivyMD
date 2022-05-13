from kivy.app import App
from kivy.uix.video import Video

class MainApp(App):
    def build(self):
        video = Video(source='./Video/My_video.mp4', play=True)
        return video

MainApp().run()