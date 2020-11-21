'''

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.title = title
        self.position = 0

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        message = self.title + ': ' + str(self.position)
        arcade.draw_text(message, self.position, y, arcade.color.BLACK, 12)





    def update(self, delta_time):
        self.position += 1
        if self.position > self.width:
            self.position = 0


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
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.width = width
        self.height = height
        self.position = 0
        self.velocity = 200
        self.radius = 30

    def on_draw(self):
        arcade.start_render()
        y = self.height / 2
        arcade.draw_circle_filled(self.position, y, self.radius, arcade.color.RED)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

        # Did the circle hit the right side of screen?

        if self.position > self.width - self.radius or self.position < self.radius:
            self.velocity *= -1


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