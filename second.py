from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **krwargs):
        self.total = total
        self.done = False
        self.current = 0
        my_text = 'Пройшло секунд:' +str(self.current)
        super().__init__(text=my_text)
    def restart(self, total, **krwargs):
        self.total = total
        self.done = False
        self.current = 0
        my_text = 'Прошло секунд:'

    def start(self):
        Clock.schedule_interval(self.change, 1)
    def change(self, dt):
        self.current += 1
        self.text = 'Пройшло секунд:' +str(self.current)
        self.done = True
        return False
