#Листинг 5.20. Демонстрации работы MDDataTable(модуль DataTable.py)
# модуль DataTable
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd. uix. datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
class MainApp(MDApp):
    def build(self):
        layout = AnchorLayout()
        self. data_tables = MDDataTable(
            size_hint=(0.9, 0.8), use_pagination=True,
            check=True,
            column_data= [('N', dp(30)),
                ('Столбец 2', dp(30)),
                ('Столбец 3', dp(60)),
                ('Столбец 4', dp(30)),
                ('Столбец 5', dp(30)),
                ('Столбец 6', dp(30), lambda *args:
        print('Сортировка по столбцу 6')), ('Столбец 7', dp(30)),],)
        layout.add_widget(self. data_tables)
        return layout
MainApp().run()