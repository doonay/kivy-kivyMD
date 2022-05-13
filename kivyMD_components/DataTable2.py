#Листинг 5.21. Демонстрации работы MDDataTable(модуль DataTable2.py)
# модуль DataTable2
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd. uix. datatables import MDDataTable
class MainApp(MDApp):
    def build(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6), # положение таблицы
        # столбцы таблицы(задано 7 столбцов)
        column_data= [('N строки', dp(20)),
            ('Столбец 2', dp(30)),
            ('Столбец 3', dp(50), self.sort_on_col_3),
            ('Столбец 4', dp(30)),
            ('Столбец 5', dp(30)),
            ('Столбец 6', dp(30)),
            ('Столбец 7', dp(30), self.sort_on_col_7),],
        # строки таблицы(задано 5 строк)
        row_data=[('1', # столбцы строки 1
            ('alert', [255/256, 165/256, 0, 1], 'Внимание 1'), 'Текст 13', 'Текст 14', 'Текст 15', '1 января', '1.777', ),
            ('2', # столбцы строки 2
            ('alert-circle', [1, 0, 0, 1], 'Внимание 2'), 'Текст 23', 'Текст 24', 'Текст 25', '2 февраля', '2.777', ),
            ('3', # столбцы строки 3
            ('checkbox-marked-circle',
            [39/256, 174/256, 96/256, 1], 'Флажок 3', ), 'Текст 33', 'Текст 34', 'Текст 34', '3 марта', '3.777', ),
            ('4', # столбцы строки 4
            ('checkbox-marked-circle',
            [39/256, 174/256, 96/256, 1], 'Флажок 4', ), 'Текст 43', 'Текст 44', 'Текст 45', '4 апреля', '4.777', ),
            ('5', # столбцы строки 5
            ('checkbox-marked-circle',
            [39/ 56, 174/256, 96/ 56, 1], 'Флажок 5', ), 'Текст 53', 'Текст 54', 'Текст 55', '5 марта', '5.777', ),],)
        layout.add_widget(data_tables)
        return layout
    def sort_on_col_3(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l
        [1] [3]))
    def sort_on_col_7(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l
        [1] [-1]))
MainApp().run()