from tkinter import *

class Square:

    def __init__(self,canvas,startX,startY,size, start):
        self.size = 4 * size
        self.startX = startX
        self.startY = startY
        self.canvas = canvas
        self.id = canvas.create_rectangle(startX,startY,startX+self.size,startY+self.size)
        self.arc = self.canvas.create_arc(self.startX+(2*self.size),self.startY,self.startX,self.startY+(2*self.size), start = start, style = ARC)
    
    def moveArc(self, distanceX, distanceY):
         self.canvas.move(self.arc, distanceX,distanceY)

        


tk = Tk()
canvas = Canvas(tk, width = 1200,height = 800)
canvas.pack()

firstX = 300
firstY = 200
size = 4

square = Square(canvas, firstX, firstY, 1, 90)

square2 = Square(canvas, firstX+size,firstY, 1, 0)
square2.moveArc(-square2.size,0)

square3 = Square(canvas, firstX,firstY+size,2,270)
square3.moveArc(-square3.size,-square3.size)

square4 = Square(canvas, firstX - (3*size),firstY, 3, 180)
square4.moveArc(0,-square4.size)

square5 = Square(canvas, firstX - (3*size), firstY - (5*size), 5, 90)

square6 = Square(canvas, (firstX + 2*size),  firstY - (5*size), 8, 0)
square6.moveArc(-square6.size,0)

square7 = Square(canvas, firstX - (3*size), firstY + (3*size), 13,270)
square7.moveArc(-square7.size, -square7.size)

square8 = Square(canvas, firstX - (24*size), firstY - (5*size), 21, 180)
square8.moveArc(0, -square8.size)


square9 = Square(canvas, firstX - (24*size), firstY - (39*size), 34, 90)

square10 = Square(canvas, firstX + (10*size), firstY - (39*size), 55, 0)
square10.moveArc(-square10.size, 0)

square11 = Square(canvas, firstX - (24*size), firstY + (16*size), 89, 270)
square11.moveArc(-square11.size, -square11.size)
