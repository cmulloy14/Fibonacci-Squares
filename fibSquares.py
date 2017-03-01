from tkinter import *
import time

squareSize = 1
squares = []
class Square:

    def __init__(self,canvas,startX,startY,size, start):
        self.size = squareSize * size
        self.startX = startX
        self.startY = startY
        self.canvas = canvas
        self.id = canvas.create_rectangle(startX,startY,startX+self.size,startY+self.size)
        self.arc = self.canvas.create_arc(self.startX+(2*self.size),self.startY,self.startX,self.startY+(2*self.size), start = start, style = ARC)
    
    def moveArc(self, distanceX, distanceY):
         self.canvas.move(self.arc, distanceX,distanceY)

def draw():
    global theStartY
    global theStartX
    global tk
    
    
    for index, fibNum in enumerate(nums):
         size = squareSize * fibNum
         size = fibNum*squareSize
 #        time.sleep(0.5)
         tk.update();
         
         if index % 4 == 0:
             theStartY = theStartY - size
             square = Square(canvas, theStartX, theStartY, fibNum, 90)
             squares.append(square)
         elif index % 4 == 1:
             startX = theStartX + nums[index-1] * squareSize
             square = Square(canvas, startX, theStartY, fibNum, 0)
             square.moveArc(-size,0)
             squares.append(square)
         elif index %4 == 2:
             startY = theStartY + nums[index-1] * squareSize
             square = Square(canvas,theStartX, startY,fibNum , 270)
             square.moveArc(-size,-size)
             squares.append(square)
         else:
             theStartX = theStartX - size
             square = Square(canvas, theStartX,theStartY, fibNum, 180)
             square.moveArc(0, -size)
             squares.append(square)
            

def createFibSequenceUpToNum(n):
     result = []
     a, b = 0, 1
     while b < n:
         result.append(b)    # see below
         a, b = b, a+b
     return result

def mouseScroll(event):
     print("mouse Scroll")

def keyPress(event):
    global squareSize
    global canvas
    print("Key Press", event.char)
    if event.char == '+':
        print("+")
        squareSize = squareSize + 5
        canvas.delete("all")
        draw()
        
    if event.char == '-':
        print("-")
        squareSize = squareSize - 5
        canvas.delete("all")
        draw()

        


print("Gimme a big 'ol Number")
num = 100

tk = Tk()

frame=Frame(tk,width=1200,height=600)
frame.grid(row=0,column=0)

canvas = Canvas(frame, width = 1200,height = 600, scrollregion=(-10000,-10000,10000,10000))

hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(width=1200, height=600)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

canvas.bind_all("<MouseWheel>", mouseScroll)
canvas.bind_all("<KeyPress>",keyPress)

theStartX = 500
theStartY = 350


nums = createFibSequenceUpToNum(num)            

draw()
