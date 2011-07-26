from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.animation import Animation

class TestApp(App):
    def button_press(self, instance):
	# respond to button presses
        if (instance == self.b1):
            self.build_page(1)
        elif (instance == self.b2):
            self.build_page(2)
        elif (instance == self.b3):
            self.build_page(3)
        elif (instance == self.b4):
            self.build_page(4)

    def build_page(self, page):
	# update the content of a page 
        self.content.clear_widgets()
        
        if (page == 1):
            text = Label(text='1')
	    self.content.add_widget(text)	
        elif (page == 2):
            text = Label(text="2")
            self.content.add_widget(text)
        elif (page == 3):
            text = Label(text='3')
	    self.content.add_widget(text)	
        elif (page == 4):
            text = Label(text='4')
	    self.content.add_widget(text)	

    def build(self):
        # create the buttons in the bottom row
	self.b1 = Button(text="Page 1")
	self.b2 = Button(text="Page 2")
	self.b3 = Button(text="Page 3")  
	self.b4 = Button(text="Page 4")
        # bind the buttons to the callback function
	self.b1.bind(on_press=self.button_press) 
	self.b2.bind(on_press=self.button_press) 
	self.b3.bind(on_press=self.button_press) 
	self.b4.bind(on_press=self.button_press) 

        # create a layout to hold the buttons
	self.buttons = GridLayout(spacing=5, rows=1)
	self.buttons.add_widget(self.b1)
	self.buttons.add_widget(self.b2)
	self.buttons.add_widget(self.b3)
	self.buttons.add_widget(self.b4)
	self.buttons.size_hint = (1,0.1)

        # create a layout to hold page content
	self.content = BoxLayout()

        # create the main layout
	self.window = GridLayout(rows=2)
	self.window.add_widget(self.content)
	self.window.add_widget(self.buttons)
	
        # on startup, load the first page 
	self.build_page(1)	

	return self.window
if (__name__ == "__main__"):
    TestApp().run()
