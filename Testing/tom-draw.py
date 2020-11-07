# Drawing & movement in arcade using functions

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_ground():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_car(x, y):
    """ Draw a car """



    # car
    arcade.draw_lrtb_rectangle_filled(on_draw.car_l, on_draw.car_r, 100, 50, arcade.color.RED)
    arcade.draw_lrtb_rectangle_filled(on_draw.car_l+25, on_draw.car_r-25, 130, 100, arcade.color.RED)
    arcade.draw_circle_filled(on_draw.car_l+20, 50, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(on_draw.car_r-20, 50, 20, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_ground()
    draw_car(on_draw.car_l, on_draw.car_r)


    # Add one to the x value, making the car person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.car_l += 1
    on_draw.car_r += 1

# Create a value that our car will start at.
on_draw.car_l = 50
on_draw.car_r = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main() 