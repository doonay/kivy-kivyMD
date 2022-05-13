#Листинг 5.73. Демонстрации работы класса TapTargetView (модуль TapTargetView.py)
# модуль TapTargetView.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView
KV = '''
Screen:
    MDFloatingActionButton:
        id: button
        icon: 'plus'
        pos: 10, 10
        on_release: app. tap_target_start()
'''
class MainApp(MDApp):
    def build(self):
        screen = Builder. load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids. button,
            title_text='Открывающаяся панель',
            description_text='Здесь можно разместить текст', widget_position='left_bottom', )
        return screen
    def tap_target_start(self):
        if self.tap_target_view.state == 'close':
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()
MainApp().run()