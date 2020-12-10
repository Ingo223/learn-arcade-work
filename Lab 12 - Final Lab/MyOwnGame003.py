'''
die wichtigsten Änderungen von Version 002 zu 003:
- die Flugvektoren sind jetzt in einer Liste gself.flight_vectors zusammengefasst
    class MyStartscreen hat jetzt 5 Flugvektoren für die Intro-Enterprise
    funktion draw_enterprise entsprechend angepasst
'''


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
        self.intro_sprite_0 = arcade.Sprite("container/intro-playership.png")   # nicht geflippt
        self.intro_sprite_1 = arcade.Sprite("container/intro-playership.png", flipped_horizontally=True)   # flipped
        self.introframes = 0
        # spielt das Intro sobald der Screen aufgerufen wird
        self.play_intro_music()
        self.fscounter = 0  # flight_sector_counter
        self.direction = 0  # flugrichtung intro-sprite
        # vektoreinträge: startx, starty, startscale, scaleänderungsfaktor, start-delta-x, start-delta-y, drehungswinkel, flipsprite(0/1)
        self.flight_vectors = [[930, 900, 0.001, 0.003, -5, -0.5, 0, 0],
                               [-300, 700, 0.001, 0.005, 6, -0.5, 0, 1],
                               [1200, 400, 0.001, 0.005, -3, -0.5, 350, 0],
                               [-300, 900, 0.001, 0.005, 3, -0.5, 5, 1],
                               [600, 700, 0.001, 0.01, -4, -5, 10, 0]]
        self.load_flight_vectors()
        self.fsmax = len(self.flight_vectors) -1



    def load_flight_vectors(self):
        self.direction = (self.flight_vectors[self.fscounter][7])  # 0 für standart links, 1 für flipped rechts
        self.intro_sprite_0.center_x = (self.flight_vectors[self.fscounter][0])
        self.intro_sprite_0.center_y = (self.flight_vectors[self.fscounter][1])
        self.intro_sprite_0.scale = (self.flight_vectors[self.fscounter][2])
        self.intro_sprite_0.scalator = (self.flight_vectors[self.fscounter][3])
        self.intro_sprite_0.change_x = (self.flight_vectors[self.fscounter][4])
        self.intro_sprite_0.change_y = (self.flight_vectors[self.fscounter][5])
        self.intro_sprite_0.angle = (self.flight_vectors[self.fscounter][6])

        self.intro_sprite_1.center_x = (self.flight_vectors[self.fscounter][0])
        self.intro_sprite_1.center_y = (self.flight_vectors[self.fscounter][1])
        self.intro_sprite_1.scale = (self.flight_vectors[self.fscounter][2])
        self.intro_sprite_1.scalator = (self.flight_vectors[self.fscounter][3])
        self.intro_sprite_1.change_x = (self.flight_vectors[self.fscounter][4])
        self.intro_sprite_1.change_y = (self.flight_vectors[self.fscounter][5])
        self.intro_sprite_1.angle = (self.flight_vectors[self.fscounter][6])


        print(self.fscounter)

    def play_intro_music(self):
        self.intro = arcade.sound.load_sound("container/introtest1.mp3")
        arcade.sound.play_sound(self.intro)


    def draw_startscreen(self):
        arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.start_screen_image)
        arcade.draw_text("2066 A.D.", 300, 430, arcade.color.ROSY_BROWN, 80)
        arcade.draw_text("IngoSVaderS", 100, 700, arcade.color.ROSY_BROWN, 80)
        arcade.draw_text("vs. Enterprise", 300, 600, arcade.color.ROSY_BROWN, 80)
        arcade.draw_text("Press << N >> to start a new Game!", width/2, 300, arcade.color.YELLOW, 30, anchor_x="center")


    def draw_enterprise(self):
            if self.direction == 0:
                arcade.Sprite.draw(self.intro_sprite_0)
            elif self.direction == 1:
                arcade.Sprite.draw(self.intro_sprite_1)
            else:
                print("Fucking Error in the Datas :)")

    def on_draw(self):
        arcade.start_render()
        # Startbild zeichnen
        self.draw_startscreen()


        # einfliegende Enterprise
        self.draw_enterprise()

    def update(self, delta_time):
        self.introframes += 1
        f = self.introframes
        if f < 400:
            self.intro_sprite_0.center_x += self.intro_sprite_0.change_x * (f / 100)
            self.intro_sprite_0.center_y += self.intro_sprite_0.change_y * (f / 100)
            self.intro_sprite_0.scale += self.intro_sprite_0.scalator * (f / 100)
            self.intro_sprite_1.center_x += self.intro_sprite_1.change_x * (f / 100)
            self.intro_sprite_1.center_y += self.intro_sprite_1.change_y * (f / 100)
            self.intro_sprite_1.scale += self.intro_sprite_1.scalator * (f / 100)
        else:
            self.introframes = 0
            self.fscounter += 1
            if self.fscounter > self.fsmax:
                self.fscounter = 0
            self.load_flight_vectors()



    def on_key_press(self, key, modifier):
        # wird ausgeführt sobald eine Taste gedrückt wird
        if key == arcade.key.N:
            # neue Instanz game der Klasse Game_view erschaffen und die Ansicht dorthin umschalten
            game = My_game()

            # intro sound stoppen
            arcade.sound.stop_sound(self.intro)

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
        self.player_sprite.center_y = 100
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
