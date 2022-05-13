'''
Кнопки ToggleButton могут быть сгруппированы для создания группы переключателей.
В этом случае только одна кнопка в группе может находиться в «нажатом» состоянии.
Имя группы может быть строкой с произвольным содержанием.

В этом модуле создано 3 кнопки, которые собраны в одну группу city.
Первая кнопка переведена в нажатое состояние – state: ’down’
В нажатом состоянии может находиться только одна кнопка из группы

– text – надпись на кнопке;
– font_size – размер шрифта;
– color – цвет шрифта;
– font_name – имя файла с пользовательским шрифтом (.ttf).
– on_press – событие, возникает, когда кнопка нажата;
– on_release – событие, возникает, когда кнопка отпущена;
– on_state – состояние (изменяется тогда, когда кнопка нажата или отпущена);
– group – задание имени группы (текстовая строка, например ’city’);
– state – задание состояние кнопки (’down’ – нажата)
'''
from kivy.app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    ToggleButton:
        text: 'Москва'
        group: 'city'
        state: 'down'
    ToggleButton:
        text: 'Воронеж'
        group: 'city'
    ToggleButton:
        text: 'Сочи'
        group: 'city'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()