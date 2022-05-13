#Листинг 5.18. Демонстрации работы MDCardSwipe(модуль MDCardSwipe.py)
# модуль MDCardSwipe
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
KV = '''
<SwipeToDeleteItem>: # контейнер всех элементов
    size_hint_y: None
    height: content. height
    #anchor: 'right' # положение скрытого слоя на карточке
    #type_swipe: 'auto' # полное открытие скрытого слоя
    MDCardSwipeLayerBox: # Контейнер для элементов заднего(скрытого) слоя
        # открываемый элемент заднего(скрытого) слоя
        padding: '8dp' # отступ от края
        MDIconButton: # кнопка с иконкой
            icon: 'trash-can'
            pos_hint: {'center_y': .5}
            on_press: app.press_button(root) # обработка нажатия кнопки
        MDCardSwipeFrontBox: # Контейнер для элементов переднего (видимого) слоя
            OneLineListItem: # видимый элемент переднего (видимого) слоя
                id: content
                text: root. text # список строк из функции on_start
                _no_ripple_effect: True
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '10dp'
        MDToolbar:
            elevation: 10
            title: 'Класс MDCardSwipe'
        ScrollView:
            scroll_timeout: 100
            MDList:
                id: md_list
                padding: 0
'''
class SwipeToDeleteItem(MDCardSwipe): # класс создания карточки
    MDCardSwipe
    text = StringProperty()
class MainApp(MDApp): # Базовый класс приложения
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder. load_string(KV)
    def build(self):
        return self.screen
    def on_start(self): # функция создания списка карточек
        for i in range(15):
            self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem
                (text=f'Однострочный элемент – {i +1}'))
    def press_button(self, button):
        print('Нажата кнопка на скрытой панели')
MainApp().run()