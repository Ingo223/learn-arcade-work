'''
- die wichtigsten Änderungen von Version 005 zu 006:

- Pausescreen zugefügt

- battlemusic jetzt nur noch 1 instanz gleichzeitig (erstmalig try - except benutzt)

'''


import arcade
import random
import math
import time

WIDTH = 1920
HEIGHT = 1000
title = "Mein erster eigener Shooter"
player_scale = 0.15
crosshair_scale = .4

starfield_speed = 0.05
amount_of_stars = 80

torpedo_speed = 5
torpedo_scale = 0.1
spacefog_speed = .4
spacefog_alpha = 100
volume_battlemusic = 0.2  # skala von 0 bis 1
framedivisor = 50


class MyStartScreen(arcade.View):
    def __init__(self):
        super().__init__()

        self.start_screen_image = arcade.load_texture("container/galaxy.png")
        self.intro_sprite_0 = arcade.Sprite("container/intro-playership.png")  # nicht geflippt
        self.intro_sprite_1 = arcade.Sprite("container/intro-playership.png", flipped_horizontally=True)  # flipped
        #gself.intro = arcade.sound.load_sound("container/introtest1.mp3")
        self.intro = arcade.Sound("container/introtest1.mp3")
        self.introframes = 0


        self.fscounter = 0  # flight_sector_counter
        self.direction = 0  # flugrichtung intro-sprite
        # : startx, starty, startscale, scaleänderungsfaktor, start-delta-x, start-delta-y, drehungswinkel, flipsprite
        self.flight_vectors = [[430+WIDTH/2, 900, 0.001, 0.003, -5, -0.5, 0, 0],
                               [-300+WIDTH/2, 700, 0.001, 0.005, 6, -0.5, 0, 1],
                               [300+WIDTH/2, 400, 0.001, 0.005, -3, -0.5, 350, 0],
                               [-300+WIDTH/2, 900, 0.001, 0.005, 3, -0.5, 5, 1],
                               [100+WIDTH/2, 700, 0.001, 0.01, -8, -5, 15, 0],
                               [-500+WIDTH/2, 600, 0.001, 0.005, 3, -0.5, 5, 1]]
        self.load_flight_vectors()
        self.fsmax = len(self.flight_vectors) - 1
        # spielt das Intro sobald der Screen aufgerufen wird
        self.play_intro_music()

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

    def play_intro_music(self):
        #time.sleep(0.1)
        arcade.sound.play_sound(self.intro)

    def draw_startscreen(self):
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 1000, 1000, self.start_screen_image)
        arcade.draw_text("2066 A.D.", WIDTH / 2, 430, arcade.color.ROSY_BROWN, 80,  anchor_x="center")
        arcade.draw_text("IngoSVaderS", WIDTH / 2, 700, arcade.color.ROSY_BROWN, 80,  anchor_x="center")
        arcade.draw_text("vs. Enterprise", WIDTH / 2, 600, arcade.color.ROSY_BROWN, 80,  anchor_x="center")
        arcade.draw_text("Press < N > to start a new Game!", WIDTH / 2, 300, arcade.color.YELLOW, 30, anchor_x="center")

    def draw_enterprise(self):
        if self.direction == 0:
            arcade.Sprite.draw(self.intro_sprite_0)
        elif self.direction == 1:
            arcade.Sprite.draw(self.intro_sprite_1)

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
            self.intro_sprite_0.center_x += self.intro_sprite_0.change_x * (f / framedivisor)
            self.intro_sprite_0.center_y += self.intro_sprite_0.change_y * (f / framedivisor)
            self.intro_sprite_0.scale += self.intro_sprite_0.scalator * (f / framedivisor)
            self.intro_sprite_1.center_x += self.intro_sprite_1.change_x * (f / framedivisor)
            self.intro_sprite_1.center_y += self.intro_sprite_1.change_y * (f / framedivisor)
            self.intro_sprite_1.scale += self.intro_sprite_1.scalator * (f / framedivisor)
        else:
            self.introframes = 0
            self.fscounter += 1
            if self.fscounter > self.fsmax:
                self.fscounter = 0
            self.load_flight_vectors()

        # intro-music
        position = self.intro.get_stream_position()

        if position == 0:
            self.play_intro_music()

    def on_key_release(self, key, modifier):
        # wird ausgeführt sobald eine Taste gedrückt wird
        if key == arcade.key.N:
            # neue Instanz game der Klasse Game_view erschaffen und die Ansicht dorthin umschalten
            game = MyGame()
            game.setup()
            # intro sound stoppen
            arcade.sound.stop_sound(self.intro)
            # umschalten zu game View
            self.window.show_view(game)


class Backgroundstar(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.hit_box_algorithm = "none"  # keine Ahnung, ob das was bringt!?

    def update(self):
        # Bewegung nach unten, um Vorwärtsflug zu simulieren
        self.center_y -= self.change_y
        if self.center_y < 0:
            self.center_y = HEIGHT


class Torpedo(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, start_x, start_y, target_x, target_y):
        super().__init__(filename, sprite_scaling)
        self.torpedosound = arcade.sound.load_sound("container/Laser_1.wav")
        dx = target_x - start_x
        dy = target_y - start_y
        angle = (math.atan2(dy, dx))
        self.angle = math.degrees(angle) - 90
        self.move_x = math.cos(angle)
        self.move_y = math.sin(angle)
        self.center_x = start_x
        self.center_y = start_y
        # Wenn ein Torpedo erzeugt wird, dann wird auch sofort der Sound dazu abgespielt
        arcade.sound.play_sound(self.torpedosound, 0.1)

    def update(self):
        self.center_x += self.move_x * torpedo_speed
        self.center_y += self.move_y * torpedo_speed
        if self.center_x < WIDTH/2-500 or self.center_x > WIDTH/2+500 or self.center_y < 0 or self.center_y > HEIGHT:
            self.remove_from_sprite_lists()

class Alien(arcade.Sprite):
    pass

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_sprite = arcade.Sprite("container/playership-0.png", player_scale)
        self.battle_screen = arcade.load_texture("not_used/1000x3000.png")
        self.aim_crosshair = arcade.Sprite("container/crosshair1.png", crosshair_scale)
        self.battlemusic = arcade.Sound("container/warrior_rising.mp3")
        self.aim_crosshair.center_x = WIDTH / 2
        self.aim_crosshair.center_y = HEIGHT / 4 * 3
        self.player_sprite.center_x = WIDTH / 2
        self.player_sprite.center_y = 150
        self.player_sprite.angle = 0
        self.player_list = arcade.SpriteList()
        self.backgroundstar_list = arcade.SpriteList()
        self.torpedo_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.player_list.append(self.aim_crosshair)
        self.delta_x = 0
        self.player_move_speed = 3
        self.counter = 1500  # y-Wert für scrollendes bild
        self.play_battlemusic()

    def setup(self):
        # alles was das Spiel braucht wird hier bereitgestellt

        # random Sternenfeld für rollenden Hintergrund erzeugen
        for i in range(amount_of_stars):
            star = Backgroundstar("container/star1_5x5.png", random.randrange(3, 9) / 5)
            star.center_x = random.randrange(WIDTH/2-500, WIDTH/2 + 500)
            star.center_y = random.randrange(HEIGHT)
            star.change_y = random.randrange(2, 8) * starfield_speed
            self.backgroundstar_list.append(star)

    def play_battlemusic(self):
        time.sleep(0.1)
        try:
            position = self.battlemusic.get_stream_position()
            if position == 0.0:
                arcade.sound.play_sound(self.battlemusic, volume_battlemusic)
        except TypeError:
            arcade.sound.play_sound(self.battlemusic, volume_battlemusic)


    def on_draw(self):
        # Spielfeld zeichnen mit aktuellen Daten
        arcade.start_render()
        arcade.draw_text("<ESC> for Pause", 100, 900, arcade.color.ROSY_BROWN, 30)
        arcade.SpriteList.draw(self.backgroundstar_list)
        arcade.draw_texture_rectangle(WIDTH/2, self.counter, 1000, 3000, self.battle_screen, 0, spacefog_alpha)
        arcade.SpriteList.draw(self.player_list)
        arcade.SpriteList.draw(self.torpedo_list)

    def update(self, delta_time: float):
        # Spiellogik, Bewegungen, Collisionen feststellen, Variablen usw aktualisieren

        # playership bewegung, darstellungswinkel und grenzen links/rechts
        if self.player_sprite.center_x > WIDTH / 2 + 450:
            self.delta_x = 0
            self.player_sprite.angle = 0
            self.player_sprite.center_x = WIDTH / 2 + 450
        elif self.player_sprite.center_x < WIDTH/2 - 450:
            self.delta_x = 0
            self.player_sprite.angle = 0
            self.player_sprite.center_x = WIDTH / 2 - 450
        else:
            self.player_sprite.center_x += self.delta_x
        # counter für zeilenweises weiterscrollen des hintergrundes (spacefog)
        self.counter -= spacefog_speed
        if self.counter <= -500:
            self.counter = 1500
        # aufruf updatefunktion der scrollenden Hintergrundsprites(stars)
        self.backgroundstar_list.update()
        # update fliegender player-Torpedos
        self.torpedo_list.update()

        # battlemusic
        position = self.battlemusic.get_stream_position()
        print(position)
        if position == 0.0:
            self.play_battlemusic()

    def on_key_press(self, key, modifier):
        # wird ausgeführt sobald eine Taste gedrückt wird

        # A + D bewegen Player links + rechts bis +-450 von Bildschirmmitte
        if key == arcade.key.D:

                self.delta_x = self.player_move_speed
                self.player_sprite.angle = 330
        if key == arcade.key.A:

                self.delta_x = -self.player_move_speed
                self.player_sprite.angle = 30

    def on_key_release(self, key, modifier):
        # Escape führt zurück zum Pausescreen
        if key == arcade.key.ESCAPE:
            arcade.sound.stop_sound(self.battlemusic)
            pause_view = PauseScreen(self)   # das "gself" übergibt die Game-Instanz dem Pause-View als Variable.
            self.window.show_view(pause_view)
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
        if button == 1:
            target_x = self.aim_crosshair.center_x
            target_y = self.aim_crosshair.center_y
            start_x = self.player_sprite.center_x
            start_y = self.player_sprite.center_y + 40
            torpedo_1 = Torpedo("container/laser-1k.png", torpedo_scale, start_x, start_y, target_x, target_y)
            self.torpedo_list.append(torpedo_1)


class PauseScreen(arcade.View):
    def __init__(self, game_view):  # "game_view" ist das, was beim Aufruf mit "gself" gesendet wurde.
        super().__init__()
        self.game_view = game_view  # game_view vom pausescreen wird die vom Gamescreen gesendete Variable

        self.pause_deko_image = arcade.load_texture("container/intro-playership.png")
        self.pause_deko_circle = arcade.SpriteCircle(500, arcade.color.OLD_GOLD)
        self.pause_deko_circle.center_x, self.pause_deko_circle.center_y = WIDTH/2, HEIGHT/2



    def on_draw(self):
        #gself.pause_deko_circle.draw()
        #arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 800, 586, gself.pause_deko_image)
        arcade.draw_text("Game paused", WIDTH/2, 800, arcade.color.BLUE_VIOLET, 120, anchor_x="center")
        arcade.draw_text("< ESC > to continue..", WIDTH / 2, 200, arcade.color.BLUE_VIOLET, 40, anchor_x="center")
        arcade.draw_text("< F11 > to quit", WIDTH / 2, 100, arcade.color.BLUE_VIOLET, 40, anchor_x="center")


    def on_key_release(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
        elif key == arcade.key.F11:  # quit game and goto Startscreen
            view = MyStartScreen()
            self.window.show_view(view)



def main():
    window = arcade.Window(WIDTH, HEIGHT, title)
    start_view = MyStartScreen()
    window.show_view(start_view)
    window.set_mouse_visible(False)
    window.center_window()
    arcade.run()


if __name__ == "__main__":
    main()
