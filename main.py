from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, ObjectProperty
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.filechooser import FileChooserListView
import os
import subprocess



path = 'uploader.json'
gcp_project = 'galerie-test'
command = subprocess.Popen(['gsutil', 'config', '-e'], stdin = subprocess.PIPE, universal_newlines = True )
command.stdin.write("{}\n".format(path))
command.communicate(input=gcp_project)

class LoadDialog(FloatLayout):

    def uploadProject(self):
        pass
    r, g, b, a = 0.99, 0.95, 0.99, 1

    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    backgroundColor = ListProperty([r, g, b, a])
    titleColor = ListProperty([r * 0.2, g * 0.2, b * 0.2, a])
    buttonColor = ListProperty([r * 0.8, g * 0.8, b * 0.8, a])
    buttonPressedColor = ListProperty([r * 0.7, g * 0.7, b * 0.7, a])
    textColor = ListProperty([r * 0.1, g * 0.1, b * 0.1, a])


class MainView(BoxLayout):

    Window.size = (800, 500)
    Window.set_title('Project Uploader')

    r, g, b, a = 0.99, 0.95, 0.99, 1
    projectPath = ''
    loadfile = ObjectProperty(None)
    label_small = ObjectProperty(None)
    thumb = ObjectProperty(None)

    backgroundColor = ListProperty([r, g, b, a])
    titleColor = ListProperty([r * 0.2, g * 0.2, b * 0.2, a])
    buttonColor = ListProperty([r * 0.8, g * 0.8, b * 0.8, a])
    buttonPressedColor = ListProperty([r * 0.7, g * 0.7, b * 0.7, a])
    textColor = ListProperty([r * 0.1, g * 0.1, b * 0.1, a])

    def uploadProject(self):
        if self.projectPath == '':
            pass
        os.system('gsutil cp -r ' + self.projectPath + ' gs://projects-bucket')

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path):
        self.label_small.text = path
        self.projectPath = path
        self.thumb.source = path + '\\img\\thumb.png'
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()


class BucketUploaderApp(App):
    pass


Factory.register('Root', cls=MainView)
Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
    BucketUploaderApp().run()
