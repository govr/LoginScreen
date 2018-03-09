#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'fullscreen', '0')

#Builder.load_file('myapp.kv')

class LoginScreen (GridLayout):
    def click(self,username,password):
        self.clear_widgets()

        self.success = Label(text='udane logowanie')
        self.failed = Label(text='nie udane logowanie')

        if username == 'radian' and password == 'haslo':
            self.add_widget(self.success)
        else:
            self.add_widget(self.failed)

class MyApp(App):
    def build(self):
        return LoginScreen()

MyApp().run()