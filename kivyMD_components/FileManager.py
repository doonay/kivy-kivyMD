#Листинг 5.28. Демонстрации работы класса MDFileManager (модуль FileManager.py)
# модуль FileManager.py
from kivy.core. window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
KV = '''
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Пример MDFileManager'
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
    FloatLayout:
        MDRoundFlatIconButton:
            text: 'Открыть менеджер'
            icon: 'folder'
            pos_hint: {'center_x':.5, 'center_y':.6}
            on_release: app.file_manager_open()
'''
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self. events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self. exit_manager,
            select_path=self.select_path,
            preview=True,)
    def build(self):
        return Builder. load_string(KV)
    def file_manager_open(self):
        self.file_manager.show('/') # вывода менеджера на экран
        self.manager_open = True

    def select_path(self, path):
        '''Будет вызвана, когда вы нажмете на имя файла
        или кнопка выбора каталога.
        :type path: str;
        :param path: путь к выбранному каталогу или файлу;
        '''
        print('Выбран файл', path)
        self. exit_manager()
        toast(path)
    def exit_manager(self, *args):
        ''' Вызывается, когда пользователь достигает корня дерева каталогов.'''
        self.manager_open = False
        self.file_manager.close()
    def events(self, instance, keyboard, keycode, text, modifiers):
        ''' Вызывается при нажатии кнопок на мобильном устройстве.'''
        if keyboard in(1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
MainApp().run()