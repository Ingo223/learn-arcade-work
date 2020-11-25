""" this is a draw program
multiline comments use 3 double-quotes sourrounding"""

import arcade

arcade.open_window(600,600,"drawing example")
#arcade.Window(800,600,"Drawing Excample")

arcade.set_background_color(arcade.csscolor.BLACK)


#get ready to draw
arcade.start_render()

#draw a rectangle

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)


#Tree trunk
# center of 100, 320
# width 29; height 60

#tree top
x = 100
y = 350
radius = 50
shield = 20


arcade.draw_circle_outline(x, y, radius + shield,arcade.csscolor.BLUE_VIOLET, shield)
arcade.draw_circle_outline(x, y, radius + shield/2,arcade.csscolor.TOMATO, shield/2)
arcade.draw_triangle_outline(x, y + 30, x - 20, y - 20, x + 20, y - 20, arcade.csscolor.YELLOW, 30)

#another tree
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200,350,40, 70,arcade.csscolor.DARK_GREEN)

#again another tree
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300,350,40,70, arcade.csscolor.DARK_GREEN, -20, 200)

#again another tree

arcade.draw_triangle_outline(400, 400, 360, 320, 440, 320, arcade.csscolor.DARK_GREEN, 25)

#again another tree
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                           (490, 360),
                           (470, 320),
                           (530, 320),
                           (510, 360),
                           ),
                           arcade.csscolor.DARK_GREEN)

# draw sun
arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.YELLOW)
# draw sunrays
arcade.draw_line(500, 550, 450, 550, arcade.color.YELLOW,3) # only 1 ray!!

#draw text
zahl = 66
testtext = f"Die Zahl lautet: {zahl}"
arcade.draw_text(testtext,100,250, arcade.color.YELLOW, 24)








# Drawing code goes here

#Finish drawing

arcade.finish_render()










arcade.run()