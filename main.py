from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from instructions import*
from ruffler import test
from kivy.clock import Clock
from second import Seconds

Window.size = (1000, 500)
Window.clearcolor = '#b88a0d'
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
        self.main_label = Label(text = txt_instruction)
        
        self.name_label = Label(text = 'Ім\'я')
        self.age_label = Label(text = 'age label')
        self.name_input = TextInput(multiline = False)
        self.age_input = TextInput(text = '7', multiline = False)
        self.btn = Button(text = '[color=#541010] + Почати[/color]', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5}, markup=True)
        self.btn.background_color = '#b08d4c'
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
        """
        Створити таймер через клас Seconds - 15 сек
        bind прив'язати новий метод до властивості done
        Створити next_screen =  False
        Створити новий метод sec_finished і в ньому перевірку


        """
        self.next_screen = False
        self.time_label = Seconds(15)
        self.time_label.bind(done=self.sec_finished)
        self.instruct_label = Label(text = txt_instruction)
        self.result_label = Label(text = 'result label')
        self.result_input = TextInput(text = '', multiline = False)
        self.btn = Button(text = 'Продовжити', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5, 'center_y':0.5})
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl1 = BoxLayout()
        hl2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        hl1.add_widget(self.instruct_label)
        hl1.add_widget(self.time_label)
        hl2.add_widget(self.result_label)
        hl2.add_widget(self.result_input)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.btn)
        self.add_widget(vl)
        self.btn.on_press = self.next
    def sec_finished(self, *args):
        if self.time_label.done:
            self.result_input.set_disabled(False)
            self.btn.text = "Продовжити"
            self.btn.set_disabled(False)
            self.next_screen = True



    def next(self):
        global pl
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.result_input.set_disabled(True)
            self.time_label.start()

        pl = int(self.result_input.text)
        self.manager.current = 'sits'
class Pulse2 (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.main_label = Label(text= txt_test3)
        self.result_before_label = Label(text='before_label')
        self.result_after_label = Label(text='after_label')
        self.result_before_input = TextInput(text='0')
        self.result_after_input = TextInput(text='0')
        self.btn = Button(text = 'Продовжити', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl1 = BoxLayout()
        hl2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        hl3 = BoxLayout(size_hint = (0.0, None), height = '30sp')
        hl1.add_widget(self.main_label)
        hl2.add_widget(self.result_before_label)
        hl2.add_widget(self.result_before_input)
        hl3.add_widget(self.result_after_label)
        hl3.add_widget(self.result_after_input)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(hl3)
        vl.add_widget(self.btn)
        self.add_widget(vl)
        self.btn.on_press = self.next
    def next(self):
        global p2, p3
        try:
            p2 = int(self.result_before_input.text)
            p3 = int(self.result_after_input.text)
            self.manager.current = 'result'
        except:
            self.main_label.text = 'Потрібно ввести числа у поля результатів'
            
class ScreenSits(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.instruct_label = Label(text=txt_sits)
        self.btn = Button(text='Продовжити', size_hint=(0.3,0.2), pos_hint={'center_x': 0.5})
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.time_label = Seconds(45)
        self.time_label.bind(done=self.sec_finished)
        self.next_screen = False

        vl.add_widget(self.instruct_label)
        vl.add_widget(self.time_label)
        vl.add_widget(self.btn)

        self.add_widget(vl)

        self.btn.on_press = self.next
    def sec_finished(self, *args):
        if self.time_label.done:
            self.next_screen = True
            self.btn.text = 'Продовжити'
            self.btn.set_disabled(False)

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.time_label.start()
        else:
            self.manager.current = 'pulse2'


class Result(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.label = Label(text= 'Результат')
        hl = BoxLayout()
        hl.add_widget(self.label)
        self.add_widget(hl)
    def result(self):
        self.label.text = test(p1, p2, p3, age)
    

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(Pulse1(name = 'pulse1'))
        sm.add_widget(ScreenSits(name = 'sits'))
        sm.add_widget(Pulse2(name = 'pulse2'))
        sm.add_widget(Result(name = 'result'))
        return sm
app = MyApp()
app.run()