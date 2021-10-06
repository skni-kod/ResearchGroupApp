import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder

kivy.require('2.0.0')
Builder.load_file("widgets/MainScreen.kv")

Window.clearcolor = (1, 1, 1, 1)


class MainScreen(Widget):
    pass


class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
