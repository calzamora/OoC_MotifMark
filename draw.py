import math
import cairo

#Define the width and height 
width = 2000
height = 200

#set the coordinates of the canvas
surface = cairo.PDFSurface("OoMotif_Mark_Practice.pdf",width, height)
#make the backgroud (i think)
context = cairo.Context(surface)

#DRAW A LINE IN THE MIDDLE OF THE CANVAS
context.set_line_width(10)      #Line density
context.move_to(500,100)        #(x,y) START POINT
context.line_to(1500,100)       #END POINT
context.stroke()                #DRAW

#DRAW A RECTANGLE IN THE MIDDLE
context.rectangle(750,75,500,50)        #(x0,y0,width,hieght)
context.fill()

#write out the drawing: 
surface.finish()