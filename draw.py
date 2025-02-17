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
          'Red': (520, 560, 1300),
          'Green': (1200, 1400, 1450)}


#iterate through the dict by color to pull each starting point individually 
# this lmost works jsut cant figure out how to access the key iteratively to define the colors
# for x_coordinates in myDict.values():
#     for x in x_coordinates:
#         print(myDict.keys())
#         print(x)
#         print("")
#         context.set_line_width(5)
#         context.move_to(x,150)        #(x,y) START POINT
#         context.line_to(x, 50)       #END POINT
#         if myDict.keys() == 'Blue':
#             context.set_source_rgb(0,0,225)
        # elif myDict.keys() == 'Purple':
        #     context.set_source_rgb(160,32,240)
        # elif myDict.keys() == 'Pink':
        #     context.set_source_rgb(225,192,203)
        # context.stroke()


#iterate through the dictionary by the key (color val) and the value (x_coord)
for color_val, x_coord in myDict.items():
    #index the value toupke so that you can go through each coordinate and pplot it one by one
    for i, coord in enumerate(x_coord):
        # print(coord)
        # print(f"{color_val}: {x_coord[i]}")
        #set the line width and stuff which is consistent across every line
        context.set_line_width(5)
        context.move_to(x_coord[i],150)        #(x,y) START POINT
        context.line_to(x_coord[i], 50) 
        #change the color depending on the key value 
        if color_val == 'Red':
            context.set_source_rgb(255, 0, 0)
            print("PURPLE")
        if color_val == 'Blue':
            context.set_source_rgb(0,0,225)
            print("BLUE")
        elif color_val == 'Green':
            context.set_source_rgb(0, 255, 0)
            print("PINK")
        context.stroke()


    #print("")
    # for x_coordinates in myDict.values():
    #     for x in x_coordinates:
    #         # print(x)
    #         # print("")
            # context.set_line_width(5)
            # context.move_to(x,150)        #(x,y) START POINT
            # context.line_to(x, 50) 
    #         if color_val == 'Blue':
    #             context.set_source_rgb(0,0,225)
    #             print("BLUE")
    #         elif color_val == 'Pink':
    #             print("PINK")
    #             context.set_source_rgb(160,32,240)
    #         elif color_val == 'Purple':
    #             print("PURPLE")
    #             context.set_source_rgb(225,192,203)
