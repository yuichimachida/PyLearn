'''
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

#Create the widgets
self.helloButton = tk.Button(self, text='Hello', command=self.Hello)
self.label = tk.Label(self, text='----')

#Add the widgets to the grid
self.helloButton.grid()
self.label.grid()
def hello(self):
    #Change the label text
    self.label.config(text='Good Bye')

#Create the form
form = Application()
#set the form title
form.master.title('tkinter1')
form.mainloop()
'''
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'Hello World\n(click me)'
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top')

        self.quit = tk.Button(self, text='QUIT', fg='red', command=root.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        print('hi there, everyone!')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
