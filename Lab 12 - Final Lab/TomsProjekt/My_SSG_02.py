# Basic game window for my space shooter game, with moving player sprite


import arcade

# Setting the game constants for the window and the player

TITLE = 'My Space Shooter Game 01'
WIDTH = 1920
HEIGHT = 1120
PLAYER_SCALE = 0.2
PL_START_POS_X = WIDTH/2
PL_START_POS_Y = 80
PLAYER_SPEED = 7

# Creating the arcade game window

class GameWindow (arcade.Window):
    def __init__(self, WIDTH, HEIGHT, TITLE):
        super().__init__(WIDTH, HEIGHT, TITLE)
    
        self.player_sprite = arcade.Sprite("game_data/spaceship_5.png", PLAYER_SCALE)     # define the player sprite & assign a picture from the subfolder /game_data
        self.player_sprite.center_x = PL_START_POS_X                                      # x position of the player sprite
        self.player_sprite.center_y = PL_START_POS_Y                                      # y position of the player sprite
        self.player_list = arcade.SpriteList()                                            # create the self.player_list as an instance of the SpriteList() class  
        self.player_list.append(self.player_sprite)                                       # append the player sprite to the new created SpriteList() instance   
        self.player_move_speed = PLAYER_SPEED                                             # setting the speed of the player sprite  
        self.delta_x = 0                                                                  # initialising the delta x player movement variable  
        arcade.set_background_color(arcade.color.BLACK)                                   # setting the background color  
        
    def setup(self):
    
        pass
    
    def on_draw(self):
        arcade.start_render()                                                             # required to be called before drawing anything to the screen
        self.player_list.draw()                                                           # method of the arcade SpriteList class used for drawing the sprite(s) in the list   

    def update(self, delta_time):                                                         # method updates the screen with the default value of 60 FPS  
        self.player_sprite.center_x += self.delta_x                                       # the center x value of the player sprite gets in(de)creased with the delta_x value  
        
    def on_key_press(self, key, modifier):                                                # method checks the key events  
        if key == arcade.key.D or key == arcade.key.RIGHT:                                # if D key is pressed...
            self.delta_x = self.player_move_speed                                         # ...delta_x is set to the player speed  
        if key == arcade.key.A or key == arcade.key.LEFT:                                 # if A is pressed...  
            self.delta_x = -self.player_move_speed                                        # ...delta_x is set to the negative player speed  
    
    def on_key_release(self, key, modifier):                                              # when the keys are released the movements stops by setting delta_x to zero  
        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.delta_x = 0           
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.delta_x = 0
            

def main():
    g_win = GameWindow(WIDTH, HEIGHT, TITLE)                                              # create an instance of the GameWindow class
    g_win.center_window()                                                                 # center the window  
    arcade.run()


main()