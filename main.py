
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty


class MainView(BoxLayout):

    r = 0.99
    g = 0.95
    b = 0.99
    a = 1

    backgroundColor = ListProperty([r, g, b, a])
    titleColor = ListProperty([r * 0.2, g * 0.2, b * 0.2, a])
    buttonColor = ListProperty([r * 0.8, g * 0.8, b * 0.8, a])
    buttonPressedColor = ListProperty([r * 0.7, g * 0.7, b * 0.7, a])
    textColor = ListProperty([r * 0.1, g * 0.1, b * 0.1, a])

    def browseProjects(self, *args):
        pass


class BucketUploaderApp(App):
    def build(self):
        return MainView()


if __name__ == '__main__':
    BucketUploaderApp().run()
