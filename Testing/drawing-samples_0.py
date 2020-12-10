""" this is a draw program
multiline comments use 3 double-quotes sourrounding"""

import arcade
from PIL import Image

arcade.open_window(600,600,"drawing example")
#arcade.Window(800,600,"Drawing Excample")

arcade.set_background_color(arcade.csscolor.BLACK)

gate_list = arcade.SpriteList()
frame = 0
# setup
for i in range(9):
    gatepic = arcade.Sprite(f"animated_circle_page_00{i+1}.png", 0.2, center_x= 200, center_y=200)
    gate_list.append(gatepic)

def show_gate():
    for frame in range(9):
        arcade.Sprite.draw(gate_list[frame])
        print(frame)




def main():

    #get ready to draw
    arcade.start_render()

    show_gate()


if 5:
    main()















arcade.finish_render()










arcade.run()