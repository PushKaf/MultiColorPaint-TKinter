from tkinter import *
from tkinter import colorchooser

#current x and y cords of the mouse
curX, curY = 0, 0
#current color when first init
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

#open the color picker menu 
def colorPicker():
    global currColor

    color_code = colorchooser.askcolor(title ="Choose color")    
    currColor = color_code[1]


#init the main window
root = Tk()
root.title("Pain(t) Pog!")
#make it zoomed
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

#add the button to pick colors
colorPickBTN = Button(canvas, text="Pick Color", command=colorPicker)
colorPickBTN.grid(row=0, column=0)

#bind the buttons and drags
canvas.bind("<Button-1>", locXY)
canvas.bind("<B1-Motion>", addLine)

# createRect()


root.mainloop()