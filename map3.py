from tkinter import *
from collections import OrderedDict
from math import *

_width = 900
_height = 800
cx = _width/2
cy = _height/2
root = Tk()
dict = OrderedDict([("Classical", ["Rock", "Alternative", "Electronic", "Pop"]), ("Folk", ["Rock", "Rap", "Country"]), ("Rock", ["Rap", "Country", "Pop"]), ("Alternative", ["Country", "Pop"]), ("Pop", ["Rap", "Country"]), ("Electronic", []), ("Rap", []), ("Country", []) ])
addressBook = []


button = Button(root, text="QUIT", fg="red", command=root.quit)
button.pack(side=LEFT)

class Node:
    def __init__(self, x, y, name, size, color = "#110b38"):
        offset = size/2.5
        canvas.create_oval(x - offset, y - offset, x + offset, y + offset, fill=color)
        canvas.create_text(x, y, font=("", int(size/5.5)), text = name)

class Point:
    _x = None
    _y = None
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def getNodeX(self):
        return self._x
    def getNodeY(self):
        return self._y

def drawEdges(i, endName, addressBook, color = "#00ffac"):
    startX = addressBook[i].getNodeX()
    startY = addressBook[i].getNodeY()
    endIndex = list(dict.keys()).index(endName)
    endX = addressBook[endIndex].getNodeX()
    endY = addressBook[endIndex].getNodeY()
    canvas.create_line(startX, startY, endX, endY, fill=color)

def configure(event):
    # Recalculate variables and clear canvas
    _width, _height = event.width, event.height
    cx, cy = _width/2, _height/2
    canvas.delete("all")
    addressBook = []

    # Go through dict and calculate the positions of each node
    r = _height/8
    a = (360/(len(dict)- 2.5))* pi / 180
    angle = 0
    for key, value in dict.items():
        x = cx + r * cos(angle)
        y = cy + r * sin(angle)
        angle = angle + a
        r = (3/10 * _height)/len(dict) + r
        addressBook.append(Point(x, y-50))
    
    # Go through the dict and draw all the edges and nodes
    i = 0
    for key, value in dict.items():
        for j in range(0, len(value)):
            if len(value) > 0:
                drawEdges(i, value[j], addressBook)

        influence = len(value) * 20
        Node(addressBook[i].getNodeX(), addressBook[i].getNodeY(), key, _height/10 + influence)
        i += 1

canvas = Canvas(root, width = _width, height = _height, bg="black")
canvas.pack(fill=BOTH, expand=YES)
canvas.bind("<Configure>", configure)

root.mainloop()





