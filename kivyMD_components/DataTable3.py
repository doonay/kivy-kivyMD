#Листинг 5.21_2. Демонстрации работы MDDataTable (модуль DataTable3.py)
# модуль DataTable3
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd. uix. datatables import MDDataTable
class MainApp(MDApp):
    def build(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.8),
            check='True',
            use_pagination=True,
            column_data= [('No.', dp(30)), ('Столбец 1', dp(30),),('Столбец 2', dp(30)),('Столбец 3', dp(30)),('Столбец 4', dp(30)),('Столбец 5', dp(30)),],
        row_data= [(f' {i +1}', '1', '2', '3', '4', '5') for i in range(50)])
        layout.add_widget(data_tables)
        return layout
MainApp().run()