from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
Window.size = (1000, 500)
name = ''
age = 7
p1, p2, p3 = 0, 0, 0
class MainScreen(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name = name)
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl1 = BoxLayout()
        hl2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        hl3 = BoxLayout(size_hint = (0.0, None), height = '30sp')
        self.main_label = Label(text = 'main label')
        self.name_label = Label(text = 'name label')
        self.age_label = Label(text = 'age label')
        self.name_input = TextInput(multiline = False)
        self.age_input = TextInput(text = '7', multiline = False)
        self.btn = Button(text = 'Почати', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5, 'center_y':0.5})
        hl1.add_widget(self.main_label)
        hl2.add_widget(self.name_label)
        hl2.add_widget(self.name_input)
        hl3.add_widget(self.age_label)
        hl3.add_widget(self.age_input)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(hl3)
        vl.add_widget(self.btn)
        self.add_widget(vl)
        self.btn.on_press = self.next
    def next(self):
        global name
        global age
        name = self.name_input.text
        try:
            age = int(self.age_input.text)
            self.manager.current = 'pulse1'
        except:
            self.main_label.text = 'Потрібно ввести число у вік'
class Pulse1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.instruction_label = Label(text = 'instruction label')
        self.result_label = Label(text = 'result label')
        self.result_input = TextInput(text = '', multiline = False)
        self.btn = Button(text = 'Продовжити', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5, 'center_y':0.5})
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl1 = BoxLayout()
        hl2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        hl1.add_widget(self.instruction_label)
        hl2.add_widget(self.result_label)
        hl2.add_widget(self.result_input)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.btn)
        self.add_widget(vl)
        self.btn.on_press = self.next
    def next(self):
        global pl
        pl = int(self.result_input.text)
        self.manager.current = 'sits'
class Pusle2 (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.task_label = Label(text = 'task label')
        self.btn = Button(text = 'Продовжити', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5, 'center_y':0.5})
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        vl.add_widget(self.task_label)
        vl.add_widget(self.btn)
        self.add_widget(vl)
        self.btn.on_press = self.next
    def next(self):
        self.manager.current = 'pulse2'


    

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(Pulse1(name = 'pulse1'))
        sm.add_widget(Pusle2(name = 'pulse2'))
        return sm
app = MyApp()
app.run()