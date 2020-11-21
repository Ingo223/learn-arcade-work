

import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Hintergrundfarbe
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


main()