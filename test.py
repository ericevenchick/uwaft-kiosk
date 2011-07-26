from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        b = Button(text="hello world")
	l = BoxLayout(orientation='vertical')
	l.add_widget(b)
	return l

TestApp().run()
