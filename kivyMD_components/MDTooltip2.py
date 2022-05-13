#Листинг 5.86. Демонстрации работы класса MDTooltip (модуль MDTooltip2.py)
# модуль MDTooltip2.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. button import MDIconButton
from kivymd.uix.tooltip import MDTooltip
KV = '''
Screen:
    TooltipMDIconButton:
        icon: 'language-python'
        tooltip_text: 'Язык программирования Python'
        pos_hint: {'center_x': .5, 'center_y': .5}
'''
class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()