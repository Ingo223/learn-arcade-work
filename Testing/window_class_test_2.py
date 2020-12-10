'''

import arcade


class MyGame(arcade.Window):
    def __init__(gself, WIDTH, HEIGHT, title, bg_color):
        super().__init__(WIDTH, HEIGHT, title)
        arcade.set_background_color(bg_color)
        gself.WIDTH = WIDTH
        gself.HEIGHT = HEIGHT
        gself.title = title
        gself.position = 0

    def on_draw(gself):
        arcade.start_render()
        y = gself.HEIGHT / 2
        message = gself.title + ': ' + str(gself.position)
        arcade.draw_text(message, gself.position, y, arcade.color.BLACK, 12)





    def update(gself, delta_time):
        gself.position += 1
        if gself.position > gself.WIDTH:
            gself.position = 0


def main():
    game1 = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game1.position = 100
    arcade.run()


if __name__ == '__main__':
    main()

_____________________________________________________________________________________________________________
_____________________________________________________________________________________________________________
import arcade


class MyGame(arcade.Window):
    def __init__(gself, WIDTH, HEIGHT, title, bg_color):
        super().__init__(WIDTH, HEIGHT, title)
        arcade.set_background_color(bg_color)
        gself.WIDTH = WIDTH
        gself.HEIGHT = HEIGHT
        gself.position = 0
        gself.velocity = 200
        gself.radius = 30

    def on_draw(gself):
        arcade.start_render()
        y = gself.HEIGHT / 2
        arcade.draw_circle_filled(gself.position, y, gself.radius, arcade.color.RED)

    def update(gself, delta_time):
        gself.position += gself.velocity * delta_time

        # Did the circle hit the right side of screen?

        if gself.position > gself.WIDTH - gself.radius or gself.position < gself.radius:
            gself.velocity *= -1


def main():
    game1 = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game1.position = game1.radius
    arcade.run()


if __name__ == '__main__':
    main()
'''

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.y = 100
        self.x = 0
        self.velocity = 1
        self.radius = 30

    def reverse(self):
        self.velocity *= -1

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.RED)

    def update(self, delta_time):
        self.x += self.velocity * delta_time

        # Did the circle hit the right/left side of screen?
        is_at_right = self.x > self.width - self.radius
        is_at_left = self.x < self.radius
        if is_at_right or is_at_left:
            self.reverse()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and self.velocity > 0  or key == arcade.key.RIGHT and self.velocity < 0:
            self.reverse()
        elif key == arcade.key.UP:
            self.y += 10
        elif key == arcade.key.DOWN:
            self.y -= 10
def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.x = game.radius
    game.velocity = 200
    arcade.run()


if __name__ == '__main__':
    main()