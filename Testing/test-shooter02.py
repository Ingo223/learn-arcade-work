"""
Sprite Explosion

Simple program to show basic sprite usage.

Artwork from http://kenney.nl
Explosion graphics from http://www.explosiongenerator.com/

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_explosion
"""
import random
import arcade
import os


SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ASTEROID= 0.8
SPRITE_SCALING_LASER = 0.8
ASTEROID_COUNT = 50

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Explosion Example"

BULLET_SPEED = 5

EXPLOSION_TEXTURE_COUNT = 60

# Class 1 for Explosions
#--------------------------------------------------------------------------------------------
class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    def __init__(self, texture_list):
        super().__init__()

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list
        

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()


# Class 2 asteroid Class
#--------------------------------------------------------------------------------------------------
class Asteroid(arcade.Sprite):
    """
    This class represents the asteroids on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the asteroid to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the asteroid
        self.center_y -= 1

        # See if the asteroid has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()




# Class 3 Main Game Class
#--------------------------------------------------------------------------------------------------

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.asteroid_list = None
        self.bullet_list = None
        self.explosions_list = []
        self.test = arcade.AnimatedTimeBasedSprite

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Pre-load the animation frames. We don't do this in the __init__
        # of the explosion sprite because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []

        for i in range(9):

            gatepic = arcade.Sprite(f"animated_circle_page_00{i + 1}.png", 0.3)

            self.explosion_texture_list.append_texture(gatepic)

        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")

        arcade.set_background_color(arcade.color.BLACK)


        """
        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = ":resources:images/spritesheets/explosion.png"

        # Load the explosions from a sprite sheet
        gself.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        # Load sounds. Sounds from kenney.nl
        gself.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        gself.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")

        arcade.set_background_color(arcade.color.BLACK)
        """


    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the asteroids
        for i in range(ASTEROID_COUNT):
            # Create the asteroid instance
            # asteroid image from kenney.nl
            asteroid = Asteroid(":resources:images/space_shooter/meteorGrey_small2.png", SPRITE_SCALING_ASTEROID)

            # Position the asteroid
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(300,SCREEN_HEIGHT)

            # Add the asteroid to the lists
            self.asteroid_list.append(asteroid)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.explosions_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Gunshot sound
        arcade.sound.play_sound(self.gun_sound)

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90

        # Give it a speed
        bullet.change_y = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()
        self.explosions_list.update()
        self.asteroid_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hits an asteroid
            hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

            # If it did...
            if len(hit_list) > 0:

                # Make an explosion
                explosion = Explosion(self.explosions_list)

                # Move it to the location of the coin
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y

                # Call update() because it sets which image we start on
                explosion.update()

                # Add to a list of sprites that are explosions
                self.explosions_list.append(explosion)

                # Get rid of the bullet
                bullet.remove_from_sprite_lists()

            # For every asteroid we hit, add to the score and remove the asteroid
            for asteroid in hit_list:
                asteroid.remove_from_sprite_lists()
                self.score += 1

                # Hit Sound
                arcade.sound.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()