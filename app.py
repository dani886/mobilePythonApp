import kivy
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput  #input
from kivy.uix.button import Button
from matplotlib.streamplot import Grid # bottoni

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        slice.add_widget(Label(text = 'Nome'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        
        slice.add_widget(Label(text = 'Voto'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        slice.add_widget(Label(text = 'Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp.run