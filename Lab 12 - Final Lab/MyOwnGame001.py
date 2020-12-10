import arcade
import random

width = 1000
height = 1000
title = "Mein erster eigener Shooter"
Player_Grösse = 0.5



class My_shooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.startbildschirm = True
        self.start_screen = None
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", Player_Grösse)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 70
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.player_sprite.delta_x = 0
        self.player_sprite.delta_y = 0

    def setup(self):
        #alles was das Spiel braucht wird hier bereitgestellt
        self.start_screen = arcade.load_texture("container/galaxy.png")
        self.battle_screen = arcade.load_texture("not_used/starfield.png")

    def draw_startscreen(self):

            arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.start_screen)
            arcade.draw_text("2066", 100, 500, arcade.color.YELLOW, 300)
            arcade.draw_text("IngoSVaderS", 150, 430, arcade.color.ROSY_BROWN, 120)
            arcade.draw_text("Press << N >> to start Game!", 100, 300, arcade.color.YELLOW, 55)


    def on_draw(self):
        # Spielfeld zeichnen mit aktuellen Daten
        arcade.start_render()
        if self.startbildschirm:
            self.draw_startscreen()
        else:
            arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.battle_screen)
            arcade.SpriteList.draw(self.player_list)


    def update(self, delta_time: float):
        # Spiellogik, Bewegungen, Collisionen feststellen, Variablen usw aktualisieren
        self.player_sprite.center_x += self.player_sprite.delta_x


    def on_key_press(self, key, modifier):
        # wird ausgeführt sobald eine Taste gedrückt wird
        if self.startbildschirm:
            if key == arcade.key.N:
                self.startbildschirm = False
            else:
                self.draw_startscreen()
        if key == arcade.key.D:
            self.player_sprite.delta_x = 1
        if key == arcade.key.A:
            self.player_sprite.delta_x = -1

    def on_key_release(self, key, modifier):
        if key == arcade.key.D and self.player_sprite.delta_x == 1:
            self.player_sprite.delta_x = 0
        if key == arcade.key.A and self.player_sprite.delta_x == -1:
            self.player_sprite.delta_x = 0


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # wird bei Mausbewegung ausgeführt
        pass


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Aufruf bei Maustastenbetätigung
        if button:
            return



def main():
    game = My_shooter(width, height, title)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    # erst jetzt wird das Programm eigentlich gestartet

    main()
