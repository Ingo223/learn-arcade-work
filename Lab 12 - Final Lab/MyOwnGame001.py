import arcade
import random

width = 1000
height = 1000
title = "Mein erster eigener Shooter"




class My_shooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.startbildschirm = True
        self.hintergrundbild = None

    def setup(self):
        #alles was das Spiel braucht wird hier bereitgestellt
        self.hintergrundbild = arcade.load_texture("galaxy.png")


    def draw_background(self):
        if self.startbildschirm:
            arcade.set_background_color(arcade.color.SKY_BLUE)
            arcade.draw_text("Start", 100, 250, arcade.color.YELLOW, 300)
            arcade.draw_text("Bildschirm", 150, 180, arcade.color.ROSY_BROWN, 120)
        else:
            arcade.draw_texture_rectangle(500, 500, 1000, 1000, self.hintergrundbild)


    def on_draw(self):
        # Spielfeld zeichnen mit aktuellen Daten
        arcade.start_render()
        self.draw_background()



    def update(self, delta_time: float):
        # Spiellogik, Bewegungen, Collisionen feststellen, Variablen usw aktualisieren
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        # wird ausgeführt sobald eine Taste gedrückt wird
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # wird bei Mausbewegung ausgeführt
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Aufruf bei Maustastenbetätigung
        if button:
            if self.startbildschirm:
                self.startbildschirm = False
            else:
                self.startbildschirm = True
        pass


def main():
    game = My_shooter(width, height, title)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    # erst jetzt wird das Programm eigentlich gestartet

    main()
