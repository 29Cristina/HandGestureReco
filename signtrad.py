import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen #we import the libraries we'll need

kivy.require('1.9.0') #kivy toolkit version

class MainWindow(Screen):   #implementation of multiple interfaces of the app
    pass

class SecondWindow(Screen): #declaration of interface classes which inherits from Screen and ScreenManager Classes
    pass

class ThirddWindow(Screen):
    pass

class ForthWindow(Screen):
    pass

class WindowManager(ScreenManager): #class which manages navigation between interfaces
    pass

Builder.load_file('signtrad.kv') #allows us to directly load the .kv file into the program

class Aspect(Widget):
    pass


class signTrad(App):
    def __init__(self):    #we define the constructor for the signTrad class
        super(signTrad, self).__init__()

    def build(self):
        return Aspect()


if __name__ == "__main":
    signTrad = signTrad()  #we instantiate the object and we run it
    signTrad.run()
