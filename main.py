from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(
            text="My First Android App",
            font_size=25
        )

MyApp().run()
