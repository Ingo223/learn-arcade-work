import arcade
import random
import time

width = 1000
height = 1000
title = "Mein erster eigener Shooter"
Player_Grösse = 0.15
Crosshair_Grösse = 0.3

class My_startscreen(arcade.View):
    def __init__(self):
        super().__init__()

        self.start_screen_image = arcade.load_texture("container/galaxy.png")
        self.intro_playership = arcade.load_texture("container/intro-playership.png")
        self.intro_playership_f = arcade.load_texture("container/intro-playership.png", flipped_horizontally=True)
        self.enterprise_dx = -6
        self.enterprise_dy = -1
        self.introframes = 0
        # spielt das Intro sobald der Screen aufgerufen wird
        self.intro = arcade.sound.load_sound("container/introtest1.mp3")
        arcade.sound.play_sound(self.intro)


    def draw_startscreen(self):
        arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.start_screen_image)
        arcade.draw_text("2066 A.D.", 300, 430, arcade.color.ROSY_BROWN, 80)
        arcade.draw_text("IngoSVaderS", 100, 700, arcade.color.ROSY_BROWN, 80)
        arcade.draw_text("vs. Enterprise", 300, 600, arcade.color.ROSY_BROWN, 80)
        arcade.draw_text("Press << N >> to start a new Game!", width/2, 300, arcade.color.YELLOW, 30, anchor_x="center")


    def draw_enterprise(self):
        self.introframes += 1

        f = self.introframes
        if self.introframes < 400:

            arcade.draw_lrwh_rectangle_textured(930 - f**1.3, 900-f**1.2, int(f*1.6),int(f*1.2), self.intro_playership)
        elif self.introframes < 800:

            arcade.draw_lrwh_rectangle_textured(-300 + (f-400) ** 1.3, 700 - (f-400) ** 1.2, int((f-400) * 3.2), int((f-400) * 2.4),
                                                self.intro_playership_f)
        else:
            self.introframes = 1


    def on_draw(self):
        arcade.start_render()
        # Startbild zeichnen
        self.draw_startscreen()

        # einfliegende Enterprise
        self.draw_enterprise()



    def on_key_press(self, key, modifier):
        # wird ausgeführt sobald eine Taste gedrückt wird
        if key == arcade.key.N:
            # neue Instanz game der Klasse Game_view erschaffen und die Ansicht dorthin umschalten
            game = My_game()

            # intro stoppen ?
            # arcade.sound.stop_sound(gself.intro)

            # umschalten zu game View
            self.window.show_view(game)


class My_game(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_sprite = arcade.Sprite("container/playership-0.png", Player_Grösse)
        self.battle_screen = arcade.load_texture("not_used/starfield.png")
        self.aim_crosshair = arcade.Sprite("container/crosshair1.png", Crosshair_Grösse)
        self.aim_crosshair.center_x = width / 2
        self.aim_crosshair.center_y = height / 4*3

        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 70
        self.player_sprite.angle = 0
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.delta_x = 0
        self.player_move_speed = 3

    def setup(self):
        #alles was das Spiel braucht wird hier bereitgestellt
        pass

    def on_draw(self):
        # Spielfeld zeichnen mit aktuellen Daten
        arcade.start_render()

        arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.battle_screen)


    def on_draw(self):
        # Spielfeld zeichnen mit aktuellen Daten
        arcade.start_render()

        arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.battle_screen)
        arcade.SpriteList.draw(self.player_list)
        arcade.Sprite.draw(self.aim_crosshair)


    def update(self, delta_time: float):
        # Spiellogik, Bewegungen, Collisionen feststellen, Variablen usw aktualisieren
        self.player_sprite.center_x += self.delta_x
        #gself.player_sprite.


    def on_key_press(self, key, modifier):
        # wird ausgeführt sobald eine Taste gedrückt wird
        if key == arcade.key.ESCAPE:
            start_view = My_startscreen()
            self.window.show_view(start_view)
        if key == arcade.key.D:
            self.delta_x = self.player_move_speed
            self.player_sprite.angle = 330
        if key == arcade.key.A:
            self.delta_x = -self.player_move_speed
            self.player_sprite.angle = 30

    def on_key_release(self, key, modifier):
        if key == arcade.key.D and self.delta_x == self.player_move_speed:
            self.delta_x = 0
            self.player_sprite.angle = 0
        if key == arcade.key.A and self.delta_x == -self.player_move_speed:
            self.delta_x = 0
            self.player_sprite.angle = 0


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # wird bei Mausbewegung ausgeführt
        self.aim_crosshair.center_x = x
        self.aim_crosshair.center_y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Aufruf bei Maustastenbetätigung
        if button:
            return



def main():
    window = arcade.Window(width, height, title)
    window.set_mouse_visible(False)
    start_view = My_startscreen()
    window.show_view(start_view)

    arcade.run()

if __name__ == "__main__":
    # erst jetzt wird das Programm eigentlich gestartet

    main()
