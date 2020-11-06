import arcade

arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599,
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.CHARTREUSE)


# House
# Center of 399, 150
# Width of 160
# Height of 200
arcade.draw_rectangle_filled(399, 150, 160, 200, arcade.csscolor.ORANGE_RED)
# Triangle is made of these points:
# (400,400), (320, 250), (480, 250)
arcade.draw_triangle_filled(400, 400, 320, 250, 480, 250, arcade.csscolor.BROWN)

# Windows

arcade.draw_lrtb_rectangle_filled(330, 370, 220, 180, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(420, 460, 220, 180, arcade.csscolor.BLACK)

# Door
arcade.draw_lrtb_rectangle_filled(400, 440, 120, 50, arcade.csscolor.BLACK)



# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()