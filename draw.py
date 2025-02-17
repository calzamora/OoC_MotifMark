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

# TRY creating the motif lines w color coordination 
# key is color value is touple of start X-coordinates
#color_dict = dict([
#    ('red': (550, 560)),
#])

myDict = {'Blue': (550, 1000, 1100),
          'Purple': (520, 560, 1300),
          'Pink': (1200, 1400, 1450)}


#iterate through the dict by color to pull each starting point individually 
# this lmost works jsut cant figure out how to access the key iteratively to define the colors
for x_coordinates in myDict.values():
    for x in x_coordinates:
        print(myDict.keys())
        print(x)
        print("")
        context.set_line_width(5)
        context.move_to(x,150)        #(x,y) START POINT
        context.line_to(x, 50)       #END POINT
        if myDict.keys() == 'Blue':
            context.set_source_rgb(0,0,225)
        elif myDict.keys() == 'Purple':
            context.set_source_rgb(160,32,240)
        elif myDict.keys() == 'Pink':
            context.set_source_rgb(225,192,203)
        context.stroke()
