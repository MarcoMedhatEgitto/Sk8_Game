# sk8_app.py
# A simple Kivy mobile application with a stylish UI and screen management.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

Window.size = (400, 700)


class SK8GameApp(App):
    def build(self):
        return

    def save_progress(self, name):
        store = JsonStore("progress.json")  # creates a local file on phone/pc
        store.put("player", name=name)
        print(f"Saved Progress -> Name: {name}")

    def load_progress(self):
        """Load saved name into TextInput if it exists."""
        store = JsonStore("progress.json")
        if store.exists("player"):
            saved_name = store.get("player")["name"]
            print(f"Loaded Progress -> Name: {saved_name}")
            # Access the TextInput directly via the app's root ids dictionary
            self.root.ids.name_input.text = saved_name
            if saved_name != '':
                self.root.ids.name_view.text = saved_name
            else:
                self.root.ids.name_view.text = "Your name here"


if __name__ == '__main__':
    SK8GameApp().run()
