from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


# class layout(BoxLayout):
#     def __init__(self):
#         super().__init__()
#         self.button = Button(text='Click me!')
#         self.button.bind(on_press=self.button_press)
#         self.add_widget(self.button)
#
#     def button_press(self, button):
#         self.label = Label(text="shit")
#         self.add_widget(self.label)
#         self.remove_widget(self.button)

class label(Label):
    def __init__(self, text):
        super().__init__()
        self.text = text

class myApp(App):
    def build(self):
        # layout = FloatLayout()
        # title = Label(text='Sk8 Game', size_hint=(0.9, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        # layout.add_widget(title)
        self.thisLabel = label("the label")
        return self.thisLabel


if __name__ == '__main__':
    myApp().run()
