import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
Draw_intervall = 1/60
counter = 0
Angle_min = 0
Angle_max = 60
Animation_steps = 30
pacradius = 8
step_width = round(Angle_max - Angle_min)/Animation_steps
delta_x = 1



def draw_ground():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)




def draw_everything(delta_time):
    arcade.start_render()
    draw_ground()
    # counter für Animation global verfügbar machen
    global counter
    # aktuellen Animationsschritt berechnen
    step = counter % Animation_steps
    # aktuellen Pacman mit Auge an aktueller Position zeichnen
    arcade.draw_arc_filled(-50 + delta_x*counter, 50 + SCREEN_HEIGHT/3, pacradius*2, pacradius*2, arcade.csscolor.YELLOW, 0 + (step*step_width), 360 - (step*step_width))
    arcade.draw_circle_filled(-50 - pacradius/3 + delta_x*counter, 50 + pacradius/2 + SCREEN_HEIGHT/3, pacradius/3, arcade.color.BLACK)
    # counter weiterzählen
    counter += 1
    if delta_x * counter > SCREEN_WIDTH + 100:
        counter = 0

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ingos Pacman Version 0.01")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # call on_draw every Draw_intervall
    arcade.schedule(draw_everything, Draw_intervall)





    #  Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()