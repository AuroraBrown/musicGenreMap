from tkinter import *
from math import *

_width = 1200
_height = 800

class Node:
    _size = 50
    def __init__(self, x, y, name):
        offset = self._size/2
        canvas.create_rectangle(x - offset, y - offset, x + offset, y + offset, fill="yellow")
        canvas_id = canvas.create_text(x, y)
        canvas.insert(canvas_id, 18, name)



def configure(event):
    _width, _height = event.width, event.height
    canvas.delete("all")

    dict = {"Folk":["Rock","Rap"], "Rock":["Rap"], "Rap":[]}
    
    cx = _width/2
    cy = _height/2
    r = 100
    a = (360/len(dict))* pi / 180
    Node(_width/2, _height/2, "TEST")
    angle = 0
    for key, value in dict.items():
        x = cx + r * cos(angle)
        y = cy + r * sin(angle)
        canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="yellow")
        canvas_id = canvas.create_text(x, y)
        canvas.insert(canvas_id, 12, key)
        #node = Node(x, y, key)
        angle = angle + a
    
    for key, value in dict.items():
        print(value)


root = Tk()
canvas = Canvas(root, width = _width, height = _height, bg="blue")
canvas.pack(fill=BOTH, expand=YES)
canvas.bind("<Configure>", configure)

root.mainloop()











































#
#
#
#BITMAP = """
#    #define im_width 32
#    #define im_height 32
#    static char im_bits[] = {
#    0xaf,0x6d,0xeb,0xd6,0x55,0xdb,0xb6,0x2f,
#    0xaf,0xaa,0x6a,0x6d,0x55,0x7b,0xd7,0x1b,
#    0xad,0xd6,0xb5,0xae,0xad,0x55,0x6f,0x05,
#    0xad,0xba,0xab,0xd6,0xaa,0xd5,0x5f,0x93,
#    0xad,0x76,0x7d,0x67,0x5a,0xd5,0xd7,0xa3,
#    0xad,0xbd,0xfe,0xea,0x5a,0xab,0x69,0xb3,
#    0xad,0x55,0xde,0xd8,0x2e,0x2b,0xb5,0x6a,
#    0x69,0x4b,0x3f,0xb4,0x9e,0x92,0xb5,0xed,
#    0xd5,0xca,0x9c,0xb4,0x5a,0xa1,0x2a,0x6d,
#    0xad,0x6c,0x5f,0xda,0x2c,0x91,0xbb,0xf6,
#    0xad,0xaa,0x96,0xaa,0x5a,0xca,0x9d,0xfe,
#    0x2c,0xa5,0x2a,0xd3,0x9a,0x8a,0x4f,0xfd,
#    0x2c,0x25,0x4a,0x6b,0x4d,0x45,0x9f,0xba,
#    0x1a,0xaa,0x7a,0xb5,0xaa,0x44,0x6b,0x5b,
#    0x1a,0x55,0xfd,0x5e,0x4e,0xa2,0x6b,0x59,
#    0x9a,0xa4,0xde,0x4a,0x4a,0xd2,0xf5,0xaa
#    };
#    """
#
#bitmap = BitmapImage(
#    data=BITMAP,
#    foreground="black",
#    background="yellow",
#                     #maskdata=MASK_BITMAP
#)
#
#bitmap.config(foreground="blue")
#bitmap["foreground"] = "red"
#print (bitmap["foreground"])



#import tkinter as tk
#
#root = tk.Tk()
#canvas = tk.Canvas(root)
#canvas.pack(expand=True, fill=tk.BOTH)
#line = canvas.create_line(0, 0, 0, 0, fill="blue")
#
#def resize(event):
#    canvas.coords(line, 0, 0, event.width, event.height)
#    canvas.bind("<Configure>")
#
#root.mainloop()



#
#from tkinter import *
#
## create a canvas with no internal border
#canvas = Canvas(bd=0, highlightthickness=0)
#canvas.pack(fill=BOTH, expand=1)
#
## track changes to the canvas size and draw
## a rectangle which fills the visible part of
## the canvas
#
#def configure(event):
#    canvas.delete("all")
#    
#    _width, _height = event.width, event.height
#    xy = 0, 0, w-1, h-1
#    canvas.create_rectangle(xy)
#    canvas.create_line(xy)
#    xy = w-1, 0, 0, h-1
#    canvas.create_line(xy)
#
#canvas.bind("<Configure>", configure)
#
#mainloop()



#############


#def drawScreen(c):
#    c.width = _width
#    c.height = _height
#    c.pack(fill=BOTH, expand=YES)
#    c.bind("<Configure>", configure)
#
#def configure(event):
#    _width, _height = event.width, event.height
#    #print(event.width, event.height)
#    canvas.delete("all")
#    canvas.create_rectangle(_height/2, _height/4, _height+_height/2, _height*(3/4), fill="green")
#    drawScreen(canvas)
#
#drawScreen(canvas)

#
#
#def key(event):
#    print ("pressed"), repr(event.char)
#
#def callback(event):
#    frame.focus_set()
#    print ("clicked at"), event.x, event.y
#
#frame = Frame(root, width=100, height=100)
#frame.bind("<Key>", key)
#frame.bind("<Button-1>", callback)
#frame.pack()
