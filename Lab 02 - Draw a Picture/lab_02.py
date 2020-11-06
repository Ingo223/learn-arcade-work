import arcade

arcade.open_window(400, 400, "IngoArt 1")

arcade.set_background_color(arcade.csscolor.DARK_ORCHID)

arcade.start_render()
# kopf
arcade.draw_ellipse_filled(200, 200, 240, 320, arcade.csscolor.BLACK)
# nase
arcade.draw_triangle_filled(200, 200, 220, 180, 180, 180, arcade.csscolor.ROSY_BROWN)
# mund
arcade.draw_polygon_filled(((140, 140),
                           (260, 140),
                           (240, 120),
                           (160, 120),                                                      ),
                           arcade.csscolor.WHITE)

# augen
arcade.draw_circle_filled(160,220,30,arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(240,220,30,arcade.csscolor.GHOST_WHITE)
#zähne oben
for i in range(10):
    arcade.draw_triangle_filled(150+i*10, 140, 160+i*10, 140, 155+i*10, 130, arcade.csscolor.RED)
#zähne unten
for i in range(7):
    arcade.draw_triangle_filled(165+i*10, 120, 175+i*10, 120, 170+i*10, 130, arcade.csscolor.RED)


arcade.finish_render()

arcade.run()