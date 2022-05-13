'''
Ключевое слово args.
Это ключевое слово используется при обращении к функциям обратно вызова для передачи им аргументов.
Это относится к аргументам, переданным обратному вызову.
'''

from kivy. app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Кнопка 1'
        on_press: app.press_button(*args)
    TextInput:
        on_focus: self.insert_text('Фокус' if args[1] else 'Нет')
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def press_button(self, instance):
        print('Вы нажали на кнопку!')
        print(instance)

MainApp().run()