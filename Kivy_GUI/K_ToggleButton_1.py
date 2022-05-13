'''
Виджет ToggleButton действует как кнопка с эффектом залипания.
Когда пользователь касается кнопки, она нажимается и остается в нажатом состоянии,
после второго касания кнопка возвращается в исходное состояние.
'''

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MainApp(App):
    def build(self):
        t_but = ToggleButton(text='Кнопка', font_size=50)
        return t_but

MainApp().run()