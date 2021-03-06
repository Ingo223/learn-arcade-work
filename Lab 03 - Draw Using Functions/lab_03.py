import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
counter = 0
Angle_min = 0
Angle_max = 60
Animation_steps = 15
step_width = round(Angle_max - Angle_min)/Animation_steps
delta_x = 1



def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    # Draw a snow person

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60+y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140+y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200+y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x-15, 210+y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x+15, 210+y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    #draw everything
    arcade.start_render()

    draw_grass()
    draw_snow_person(150, 140)
    draw_snow_person(350, 140)


    # mytest
    global counter
    counter += 1
    step = counter % Animation_steps


    arcade.draw_arc_filled(200 + 3*counter, 500, 100, 100, arcade.csscolor.YELLOW, 0 + (step*step_width), 360 - (step*step_width))
    arcade.draw_circle_filled(185 + 3*counter, 525, 8, arcade.color.BLACK)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # call on_draw every 1/60 sec
    arcade.schedule(on_draw, 1/60)





    #  Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()