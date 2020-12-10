''' ingos comments:
why there was no enemy and how to fix:
1.: die enemie-instanz wird in der Game setup erzeugt, aber die Game setup wurde nirgends aufgerufen. Aufruf jetzt am ende der game-init.
2.: die super().__init__ der enemy-class interpretiert die 3. und 4 Variable nicht als startkoordinaten des sprites auf dem Screen,
    sondern als startkoordinaten der textur für den sprite innerhalb der angegebenen grafikdatei.
    wenn man die grafik komplett laden will, kann man das in der init (also in der super-init) weglassen, weil der standartwert ist 0, 0


'''



# Basic game window for my space shooter game, with moving player sprite
# Version 05: where is the enemy ? no enemy :-( 

import arcade

# Setting the game constants for the window and the player

TITLE = 'My Space Shooter Game'
WIDTH = 1920
HEIGHT = 1080
PLAYER_SCALE = 0.2
PL_START_POS_X = WIDTH/2
PL_START_POS_Y = 80
PLAYER_SPEED = 250
SPRITE_SCALING_LASER = 0.5
BULLET_SPEED = 5

ENEMY_SCALE = 1
ENEMY_SPEED = 0

class Enemy(arcade.Sprite):
    
    def __init__(self, filename, sprite_scaling, enemy_pos_x, enemy_pos_y):
        super().__init__(filename, sprite_scaling)
        
        self.filename = filename
        self.sprite_scaling = sprite_scaling
        self.center_x = enemy_pos_x
        self.center_y = enemy_pos_y

        





# Creating the arcade game window

class GameWindow (arcade.Window):
    def __init__(self, WIDTH, HEIGHT, TITLE):
        super().__init__(WIDTH, HEIGHT, TITLE)
        
        # Player
        self.player_sprite = arcade.Sprite("game_data/spaceship_5.png", PLAYER_SCALE)     # define the player sprite & assign a picture from the subfolder /game_data
        self.player_sprite.center_x = PL_START_POS_X                                      # x position of the player sprite
        self.player_sprite.center_y = PL_START_POS_Y                                      # y position of the player sprite
        self.player_speed = PLAYER_SPEED                                                  # setting the speed of the player sprite                                                                  
        self.right = False
        self.left = False
        
        # Sprite lists
        self.player_list = arcade.SpriteList()                                            # create the self.player_list as an instance of the SpriteList() class  
        self.bullet_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)                                       # append the player sprite to the new created SpriteList() instance 
        self.enemy_list = arcade.SpriteList()    
        
        # Background & Sound
        self.gun_sound = arcade.sound.load_sound("game_data/laser1.ogg")
        self.background = arcade.load_texture("game_data/cosmos.jpg")
        GameWindow.setup(self)
                
    def setup(self):
        
        enemy = Enemy("game_data/spaceship_6.png", ENEMY_SCALE, WIDTH/2, HEIGHT/2)
                                     
        self.enemy_list.append(enemy)
        
    def on_draw(self):
        arcade.start_render()                                                             # required to be called before drawing anything to the screen
        #arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        
        self.bullet_list.draw()
        self.player_list.draw()                                                           # method of the arcade SpriteList class used for drawing the sprite(s) in the list   
        self.enemy_list.draw()
                
        
        
    def update(self, delta_time: float):                                                         # method updates the screen with the default value of 60 FPS  
        if self.right:
            self.player_sprite.center_x += self.player_speed * delta_time
        if self.left:
            self.player_sprite.center_x -= self.player_speed * delta_time
            
        self.bullet_list.update()
        self.enemy_list.update()
        
    def on_key_press(self, key, modifier):                                                # method checks the key events  
        if key == arcade.key.D or key == arcade.key.RIGHT:                                # if D key is pressed...
            self.right = True                                         
        if key == arcade.key.A or key == arcade.key.LEFT:                                 # if A is pressed...  
            self.left = True                                       
        if key == arcade.key.SPACE or key == arcade.key.UP:
            arcade.sound.play_sound(self.gun_sound)
            bullet = arcade.Sprite("game_data/laserRed01.png", SPRITE_SCALING_LASER)
            self.bullet_list.append(bullet)
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            
            
    def on_key_release(self, key, modifier):                                              # when the keys are released the movements stops by setting delta_x to zero  
        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.right = False             
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left = False  
            

def main():
    g_win = GameWindow(WIDTH, HEIGHT, TITLE)                                              # create an instance of the GameWindow class
    g_win.center_window()                                                                 # center the window  
    arcade.run()


main()