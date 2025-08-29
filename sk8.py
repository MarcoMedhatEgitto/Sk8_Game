# sk8_app.py
# A simple Kivy mobile application with a stylish UI and screen management.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400, 700)

KV_DESIGN = """
# ScreenManager is the root widget, managing multiple screens
ScreenManager:
    # Define the main menu screen
    Screen:
        name: 'main_menu'
        # The actual content of the main menu is within this BoxLayout
        BoxLayout:
            orientation: 'vertical'
            padding: [20, 50, 20, 50]  # Add padding around the entire layout
            spacing: 30  # Space between elements
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.1, 1  # Dark background
                Rectangle:
                    size: self.size
                    pos: self.pos

            # The main title label
            Label:
                text: 'SK8 Game'
                font_size: '50sp'
                color: (1, 1, 1, 1)  # White text color
                bold: True
                size_hint_y: 0.2  # Takes up 20% of vertical space
                text_size: self.size
                halign: 'center'
                valign: 'middle'

            # The image of the skateboard, placed between the title and buttons
            Image:
                source: 'sk.png'  # You need to provide this image file in the same directory
                allow_stretch: True
                keep_ratio: True
                size_hint_y: 0.5 # Takes up 50% of vertical space

            # A container for the buttons to ensure proper alignment
            BoxLayout:
                orientation: 'vertical'
                spacing: 20
                size_hint_y: 0.3 # Takes up the remaining vertical space
                padding: [30, 0]  # Add horizontal padding to make buttons narrower
                pos_hint: {'center_x': 0.5}

                # Stylish button for "Single" player mode
                Button:
                    text: 'Single Game'
                    font_size: '20sp'
                    size_hint_y: None
                    height: '60dp'
                    background_color: (0, 0, 0, 0)  # Transparent background
                    background_normal: ''  # No default background image
                    color: (1, 1, 1, 1) # White text color
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.6, 0.86, 1  # A nice blue color
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15]
                    on_press: app.root.transition.direction = 'left'
                    on_press: app.root.current = 'difficulty_screen'

                # Stylish button for "Multiplayer" player mode
                Button:
                    text: 'Multiplayer'
                    font_size: '20sp'
                    size_hint_y: None
                    height: '60dp'
                    background_color: (0, 0, 0, 0)
                    background_normal: ''
                    color: (1, 1, 1, 1)
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.6, 0.86, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15]

                # Stylish button for "Progress"
                Button:
                    text: 'Progress'
                    font_size: '20sp'
                    size_hint_y: None
                    height: '60dp'
                    background_color: (0, 0, 0, 0)
                    background_normal: ''
                    color: (1, 1, 1, 1)
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.6, 0.86, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15]

    # Define the difficulty selection screen
    Screen:
        name: 'difficulty_screen'
        BoxLayout:
            orientation: 'vertical'
            padding: [20, 50, 20, 50]
            spacing: 30
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.1, 1
                Rectangle:
                    size: self.size
                    pos: self.pos

            Label:
                text: 'Difficulty'
                font_size: '50sp'
                color: (1, 1, 1, 1)
                bold: True
                size_hint_y: 0.2
                text_size: self.size
                halign: 'center'
                valign: 'middle'

            Image:
                source: 'sk.png'  # You need to provide this image file in the same directory
                allow_stretch: True
                keep_ratio: True
                size_hint_y: 0.5 # Takes up 50% of vertical space


            BoxLayout:
                orientation: 'vertical'
                spacing: 20
                size_hint_y: 0.3
                padding: [30, 0]
                pos_hint: {'center_x': 0.5}

                Button:
                    text: 'Easy'
                    font_size: '20sp'
                    size_hint_y: None
                    height: '60dp'
                    background_color: (0, 0, 0, 0)
                    background_normal: ''
                    color: (1, 1, 1, 1)
                    canvas.before:
                        Color:
                            rgba: 0.1, 0.8, 0.1, 1  # Green color
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15]
                    on_press: app.root.transition.direction = 'right'
                    on_press: app.root.current = 'main_menu'

                Button:
                    text: 'Medium'
                    font_size: '20sp'
                    size_hint_y: None
                    height: '60dp'
                    background_color: (0, 0, 0, 0)
                    background_normal: ''
                    color: (1, 1, 1, 1)
                    canvas.before:
                        Color:
                            rgba: 0.9, 0.8, 0.1, 1  # Yellow color
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15]
                    on_press: app.root.transition.direction = 'right'
                    on_press: app.root.current = 'main_menu'

                Button:
                    text: 'Hard'
                    font_size: '20sp'
                    size_hint_y: None
                    height: '60dp'
                    background_color: (0, 0, 0, 0)
                    background_normal: ''
                    color: (1, 1, 1, 1)
                    canvas.before:
                        Color:
                            rgba: 0.8, 0.1, 0.1, 1  # Red color
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15]
                    on_press: app.root.transition.direction = 'right'
                    on_press: app.root.current = 'main_menu'
"""


class SK8GameApp(App):
    def build(self):
        return Builder.load_string(KV_DESIGN)


if __name__ == '__main__':
    SK8GameApp().run()