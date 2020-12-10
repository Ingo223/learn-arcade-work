'''
- die wichtigsten Änderungen von Version 008 zu 009:

- class Enemie
- class Explosion
- next Level wenn alle enemies abgeschossen sind


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

starfield_speed = 0.02
amount_of_stars = 150

torpedo_speed = 5
torpedo_scale = 0.1
shoot_delay = 1.5

enemie_scale = .20
enemie_speed = 0.2

volume_battlemusic = 0.1  # skala von 0 bis 1
framedivisor = 50  #  intro enterprise beschleunigung (frameabhängig)


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


class LevelReadyScreen(arcade.View):
    def __init__(self, game_view, level):
        super().__init__()
        self.level = level
        self.game_view = game_view

    def on_draw(self):
        #arcade.start_render()  # wenn die letzte View "übermalt" werden soll, dann start_render
        arcade.draw_text(f"Level {self.level}", WIDTH / 2, 800, arcade.color.BLUE_VIOLET, 120, anchor_x="center")
        arcade.draw_text("< S > to Start..", WIDTH / 2, 200, arcade.color.BLUE_VIOLET, 40, anchor_x="center")

    def on_key_release(self, key, modifier):
        # Game startet (View wechselt) bei taste < S >
        if key == arcade.key.S:
            self.window.show_view(self.game_view)



    def on_show_view(self):
        pass


class Backgroundstar(arcade.Sprite):
    backgroundstar_list = []   # ...um "unressolved attribute reference" zu vermeiden
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.hit_box_algorithm = "none"  # keine Ahnung, ob das was bringt!?

    def setup(self):
        # random Sternenfeld für rollenden Hintergrund erzeugen
        for i in range(amount_of_stars):
            star = Backgroundstar("container/star1_5x5.png", random.randrange(3, 9) / 5)
            star.center_x = random.randrange(WIDTH/2-500, WIDTH/2 + 500)
            star.center_y = random.randrange(HEIGHT)
            star.change_y = random.randrange(2, 8) * starfield_speed
            self.backgroundstar_list.append(star)

    def update(self):
        # Bewegung nach unten, um Vorwärtsflug zu simulieren
        self.center_y -= self.change_y
        if self.center_y < 0:
            self.center_y = HEIGHT


class Torpedo(arcade.Sprite):
    torpedosound = arcade.sound.load_sound("container/Laser_1.wav"); print("load_sound torpedosound")
    def __init__(self, filename, sprite_scaling, start_x, start_y, target_x, target_y):
        super().__init__(filename, sprite_scaling)
        #self.torpedosound = arcade.sound.load_sound("container/Laser_1.wav") ; print("load sound")
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

    def setup(self):
        pass

    def fire_torpedo(self):
        # fire-speed
        now = time.time()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now

            target_x = self.aim_crosshair.center_x
            target_y = self.aim_crosshair.center_y
            start_x = self.player_sprite.center_x
            start_y = self.player_sprite.center_y + 40
            torpedo_1 = Torpedo("container/laser-1k.png", torpedo_scale, start_x, start_y, target_x, target_y)
            self.torpedo_list.append(torpedo_1)

    def update(self):
        self.center_x += self.move_x * torpedo_speed
        self.center_y += self.move_y * torpedo_speed
        if self.center_x < WIDTH/2-500 or self.center_x > WIDTH/2+500 or self.center_y < 0 or self.center_y > HEIGHT:
            self.remove_from_sprite_lists()

class Enemie(arcade.Sprite):
    def __init__(self, filename, enemie_scale, center_x, center_y, change_x, change_y):
        super().__init__(filename, enemie_scale)
        self.enemie_scale = enemie_scale
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x * enemie_speed
        self.change_y = change_y * enemie_speed
        self.left_border = random.randrange(WIDTH/2 - 500, WIDTH/2 - 50)
        self.right_border = self.left_border + 550
        self.top_border = random.randrange(HEIGHT - 250, HEIGHT-50)
        self.bottom_border = self.top_border - 500

    def setup(self, level):
        for i in range(level + 1):
            dx, sdx = random.randrange(1, 6), random.randrange(-1, 2, 2)
            dy, sdy = random.randrange(1, 6), random.randrange(-1, 2, 2)
            enemie = Enemie("container/th.png", enemie_scale, WIDTH/2, HEIGHT/2, dx * sdx, dy * sdy)
            self.enemie_list.append(enemie)


    def update(self):

        self.center_x += self.change_x
        if self.center_x < self.left_border:
            self.change_x *= -1
            self.center_x = self.left_border
        elif self.center_x > self.right_border:
            self.change_x *= -1
            self.center_x = self.right_border
        self.center_y += self.change_y
        if self.center_y > self.top_border:
            self.change_y *= -1
            self.center_y = self.top_border
        elif self.center_y < self.bottom_border:
            self.change_y *= -1
            self.center_y = self.bottom_border


class ScrollFog():
    def __init__(self, filename, flipped, center_y, speed_dy, alpha):
        self.fog_picture = filename
        self.flipped = flipped
        self.center_y = center_y
        self.scrollfog_speed = speed_dy
        self.scrollfog_alpha = alpha
        self.fog_texture = arcade.load_texture(filename, flipped_vertically=flipped)
        self.height = self.fog_texture.height
        self.width = self.fog_texture.width
        self.scrollfog_speed = speed_dy

    def setup(self):
        # scrollfog_data: dateiname, scrollgeschwindigkeit, alpha
        self.scrollfog_data = [["container/1000_0b_gimp.png", .0025, 70],
                               ["container/1000_2m_gauss.png", .0125, 50],
                               ["container/1000_2_gauss.png", .25, 50],
                               ["container/1000_0_gimp.png", 1.25, 70]
                               ]
        anzahl = (len(self.scrollfog_data))
# TODO mir endlich merken das ich die Listenelemente nur wie geplant zuweisen kann, wenn vorher...
        # leere 2-dim Liste erstellen, geht auch anders!?
        self.scrollfoglist = [[[]for i in range(2)] for j in range(anzahl)]
# TODO ... zB. eine Füllfunktion wie oben allen Feldern einmal "egal was" oder auch garnix  zuweist!?
        for i, field in enumerate(self.scrollfog_data):
            self.fog_file = field[0]  # ort und name der bilddatei
            self.scrollfog_speed = field[1]  # scrollgeschwindigkeit
            self.scrollfog_alpha = field[2]  # transparenz alphawert
            self.scroll_fog_1 = ScrollFog(self.fog_file, False, HEIGHT / 2, self.scrollfog_speed, self.scrollfog_alpha)
            self.scroll_fog_2 = ScrollFog(self.fog_file, True, HEIGHT / 2 + arcade.load_texture(self.fog_file).height, self.scrollfog_speed, self.scrollfog_alpha)
            self.scrollfoglist[i][0]=(self.scroll_fog_1)
            self.scrollfoglist[i][1]=(self.scroll_fog_2)

    def update(self):
        self.center_y -= self.scrollfog_speed
        if self.center_y < HEIGHT/2 - self.height:
            self.center_y += 2 * self.height

    def draw_scroll_fog(self):
        arcade.draw_texture_rectangle(WIDTH/2, self.center_y, 1000, self.height, self.fog_texture, 0, self.scrollfog_alpha)


class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()
        self.cur_texture_index = 0  #neue instanz wird immer mit der ersten frame gestartet
        self.textures = texture_list

    def update(self):  # goto next frame, what to do after last frame
        self.cur_texture_index += 1
        if self.cur_texture_index < len(self.textures):
            self.set_texture(self.cur_texture_index)
        else:
            self.remove_from_sprite_lists()






class MyGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.battlemusic = arcade.Sound("container/warrior_rising.mp3")
        self.enemy_destroyed_sound = arcade.Sound("container/GExplo.mp3")
        self.aim_crosshair = arcade.Sprite("container/crosshair1.png", crosshair_scale)
        self.player_sprite = arcade.Sprite("container/playership-0.png", player_scale)
        self.enemie_sprite = arcade.Sprite("container/aliensh.png", enemie_scale)
        self.shoot_delay = shoot_delay
        self.last_shot = time.time()
        self.level = 0
        self.ready_for_next_level = True
        self.enemie_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.backgroundstar_list = arcade.SpriteList()
        self.torpedo_list = arcade.SpriteList()
        self.fire_expl_list = None  # liste in der die Explosionen von zerstörten enemies sind
        self.fire_expl_tx_list = []  ## liste mit den verschiedenen texturen für die animation

        self.scrollfog_data = []
        self.scrollfoglist = []
        self.player_list.append(self.player_sprite)
        self.player_list.append(self.aim_crosshair)
        self.delta_x = 0
        self.player_move_speed = 3
        self.counter = 1500  # y-Wert für scrollendes bild
        self.play_battlemusic()


    def show_levelstart_screen(self):
        level_ready_view = LevelReadyScreen(self, self.level)
        self.window.show_view(level_ready_view)


    def setup(self):
        # alles was das Spiel braucht wird hier bereitgestellt
        self.fire_expl_list = arcade.SpriteList()  # liste in der die Explosionen von zerstörten enemies sind
        self.fire_expl_tx_list = arcade.load_spritesheet("container/expl_0100_0100_0006_0012.png", 100, 100, 6, 13)

        # fadenkreuz startposition
        self.aim_crosshair.center_x = WIDTH / 2
        self.aim_crosshair.center_y = HEIGHT / 2
        self.player_sprite.center_x = WIDTH / 2
        self.player_sprite.center_y = 150

        # playerschiff startwinkel (vorwärstflug)
        self.player_sprite.angle = 0

        Backgroundstar.setup(self)

        ScrollFog.setup(self)

        Torpedo.setup(self)





    def play_battlemusic(self):
        # time.sleep(0.1)
        try:
            position = self.battlemusic.get_stream_position()
            if position == 0.0:
                arcade.sound.play_sound(self.battlemusic, volume_battlemusic)
        except TypeError:
            arcade.sound.play_sound(self.battlemusic, volume_battlemusic)


    def on_draw(self):

        # Spielfeld zeichnen mit aktuellen Daten
        arcade.start_render()

        arcade.SpriteList.draw(self.backgroundstar_list)

        # scrollfog
        for k in range(len(self.scrollfoglist)):
            self.scrollfoglist[k][0].draw_scroll_fog()
            self.scrollfoglist[k][1].draw_scroll_fog()

        arcade.SpriteList.draw(self.player_list)
        arcade.SpriteList.draw(self.torpedo_list)
        arcade.SpriteList.draw(self.enemie_list)

        # hier kommt die Abfrage, ob zur Next-Level-Ansicht geschaltet wird!!
        # nachdem arcade.render alles gezeichnet hat, wird bei Spielbeginn der level von 0 auf 1 erhöht
        if self.ready_for_next_level == True:
            self.level += 1
            self.ready_for_next_level = False
            Enemie.setup(self, self.level)
            self.show_levelstart_screen()
        else:
            # Pause nicht möglich solange das Spiel nicht läuft, also nur "sonst" die Taste dafür anzeigen
            arcade.draw_text("<ESC> for Pause", 100, 900, arcade.color.ROSY_BROWN, 30)

        self.fire_expl_list.draw()



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

        # aufruf updatefunktion der scrollenden Hintergrundsprites(stars)
        self.backgroundstar_list.update()
        # update fliegender player-Torpedos
        self.torpedo_list.update()

        self.enemie_list.update()

        # battlemusic
        position = self.battlemusic.get_stream_position()
        if position == 0.0:
            self.play_battlemusic()

        # scrollfog
        for k in range(len(self.scrollfoglist)):
            self.scrollfoglist[k][0].update()
            self.scrollfoglist[k][1].update()

        # getroffene enemies
        self.fire_expl_list.update()  # fire-explosionstexturen aktualisieren




        for torpedo in self.torpedo_list:
            hit_enemie_list = arcade.check_for_collision_with_list(torpedo, self.enemie_list)

            if len(hit_enemie_list):
                print("TREFFER!!!")
                explosion = Explosion(self.fire_expl_tx_list)

                explosion.center_x = hit_enemie_list[0].center_x
                explosion.center_y = hit_enemie_list[0].center_y
                explosion.update()  # start with first frame
                self.fire_expl_list.append(explosion)
                torpedo.remove_from_sprite_lists()

            for enemie in hit_enemie_list:
                arcade.sound.play_sound(self.enemy_destroyed_sound)
                enemie.remove_from_sprite_lists()
                # score + hier berechnen?
            if torpedo.bottom > HEIGHT or torpedo.top < 0:
                torpedo.remove_from_sprite_lists()

            if len(self.enemie_list) == 0:
                self.ready_for_next_level = True




    def on_show(self):
        pass






    def on_key_press(self, key, modifier):
        # torpedo feuern mit spacetaste
        if key == arcade.key.SPACE:
            Torpedo.fire_torpedo(self)
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

        if key == arcade.key.F9:
            pass




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
            Torpedo.fire_torpedo(self)




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
