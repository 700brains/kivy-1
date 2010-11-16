from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.core.text import Label as CoreLabel
from kivy.graphics import *

from random import random

class TestApp(App):
    def build(self):
        w = Widget()
        with w.canvas:
            Rectangle(pos=(25,50), size=(200,300))

        return w

TestApp().run()
