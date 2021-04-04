from tkinter import *


#current x and y cords of the mouse
curX, curY = 0, 0
#all the colors to init
colors = ["black", "gray", "darkslategray", "slategray", "gray", "lightgrey", "blue", "royalblue", "dodgerblue", "deepskyblue1", "cyan2", "seagreen1", "green", "green2", "limegreen", "red", "orangered", "indianred1", "yellow", "gold", "orange"]
currColor = "black"

#get where the mouse currently is
def locXY(event):
    global curX, curY
    curX, curY = event.x, event.y

#draw the line when dragged
def addLine(event):
    global curX, curY
    canvas.create_line((curX, curY, event.x, event.y), fill=currColor)
    curX, curY = event.x, event.y

#make rectangles cordinating to the colors, and bind tags to the colors when clicked
def createRect():
    x, y, x1, y1 = 10, 10, 35, 35
    for color in colors:
        colorRect = canvas.create_rectangle((x, y, x1, y1), fill=color)
        bindTag(colorRect ,color)
        y+=30  
        y1+=30

#NOTE I tried to do this in the for loop ^ , but didnt really work...
def bindTag(rect, color):
    #bind the tag when clicked change the color
    canvas.tag_bind(rect, "<Button-1>", lambda x: changeColor(color))

#set the current color of the line to the coordinated color of the rectangle clicked on 
def changeColor(newColor):
    global currColor
    currColor = newColor

#init the main window
root = Tk()
root.title("Pain(t) Pog!")
#make it zoomed
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

#bind the buttons and drags
canvas.bind("<Button-1>", locXY)
canvas.bind("<B1-Motion>", addLine)

createRect()


root.mainloop()