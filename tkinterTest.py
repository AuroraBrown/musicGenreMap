from tkinter import *

class App:

    def __init__(self, master):

        _width = master.winfo_reqwidth()
        _height = 400

        frame = Frame(master)
        frame.pack(fill=BOTH, expand=YES)
        
        #frame.minsize(master.winfo_reqwidth(), master.winfo_reqheight())
        
        def getWidth( self ):
            return master.winfo_reqwidth()

        def getHeight(self):
            return master.winfo_reqheight()

        self.w = Canvas(master, width = _width, height = _height, bg="blue")        
        self.w.pack(fill=BOTH, expand=YES)
        
        self.w.bg=("blue")
        self.w.create_line(0, 0, _width, _height)
        self.w.create_line(0, _height, _width, 0, fill="red", dash=(4, 4))

        self.w.create_rectangle(_height/2, _height/4, _height+_height/2, _height*(3/4), fill="blue")

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print ("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
