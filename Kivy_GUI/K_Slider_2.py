'''
– min – минимальное значение (например – 0);
– max – максимальное значение (например – 500);
– value – текущее (начальное) значение (например – 50);
– step – шаг изменения значения (например – 1);
– value_track_color – цвет следа бегунка (в формате r, g, b, a);
– value_track – показывать след бегунка (True – да, False – нет)
– orientation – ориентация бегунка (’vertical’ – вертикальная,
’horizontal’ – горизонтальная);
– on_touch_down – событие (касание бегунка);
– on_touch_up – событие (бегунок отпущен);
– on_touch_move – событие (касание бегунка с перемещением)
'''
from kivy. app import App
from kivy.lang import Builder

KV = '''
Slider:
    orientation: 'horizontal'
    value_track: True
    value_track_color: 1, 0, 0, 1
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()