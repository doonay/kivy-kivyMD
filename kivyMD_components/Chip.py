#Листинг 5.19. Демонстрации работы MDChip(модуль Chip.py)
# модуль Chip.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Примеры Chip'
            left_action_items: [['menu', lambda x: x]]
        ScrollView: # Начало секции скроллинга ------------
            MDGridLayout:
                padding: dp(10)
                spacing: dp(10)
                cols: 1
                adaptive_height: True
                MDLabel:
                    text: '… Варианты…'
                MDChip:
                    text: ' Без иконки'
                    #color: 1, 0, 0, 1
                    text_color: 1, 1, 1, 1
                    icon:''
                    on_release: app.press_chip1(self)
                MDChip:
                    text: ' Красный Chip'
                    color: 1, 0, 0, 1
                    text_color: 1, 1, 1, 1
                    icon:''
                    on_release: app.press_chip2(self)
                MDChip:
                    text: ' C иконкой'
                    color: 0, 1, 0, 1
                    icon: 'language-python'
                    on_release: app.press_chip2(self)
                MDChip:
                    text: 'С отметкой – v'
                    icon: 'city'
                    check: True
                MDSeparator: #####################
                    MDLabel:
                        text: 'Выбор из трех вариантов'
                    MDChooseChip:
                        MDChip:
                            text: 'Вариант 1'
                            icon: 'earth'
                            text_color: 1, 1, 1, 1
                            selected_chip_color:.21,.098, 1, 1
                        MDChip:
                            text: 'Вариант 2'
                            icon: 'face'
                            text_color: 1, 1, 1, 1
                            selected_chip_color:.21,.098, 1, 1
                        MDChip:
                            text: 'Вариант 3'
                            icon: 'facebook'
                            text_color: 1, 1, 1, 1
                            selected_chip_color:.21,.098, 1, 1
                    MDSeparator:
                        ######################
                        # Конец секции скроллинга ------------------------

'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def press_chip1(self, instance):
        print('Нажат Chip без иконки')
    def press_chip2(self, instance):
        print('Нажат красный Chip')
MainApp().run()