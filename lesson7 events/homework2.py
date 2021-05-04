"""
На экране в любых местах стоят три спрайта.
Если мышь над спрайтом и нажата клавиша вверх или вниз, то его костюм меняется на следующий или предыдущий соответственно.

Если мышь над спрайтом и нажата клавиша вправо или влево, то он начинает вращаться вправо или влево,
  пока нажата клавиша и мышь находится над ним.

Если мышь над спрайтом и вращается колесико мыши, то размер спрайта увеличивается или
  уменьшается на 1 пиксель с сохранением пропорций (исп номер клавиши мыши wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN).
"""

import wrap
from wrap import world, sprite

world.create_world(400, 700, 900, 50)

sprite1 = sprite.add("battle_city_tanks", 100, 100)
sprite2 = sprite.add("pacman", 200, 200, "player2")
sprite3 = sprite.add("mario-2-small", 300, 300, "stand")


@wrap.on_key_down(wrap.K_UP, wrap.K_DOWN)
def change_costume(key, pos_x, pos_y):
    spr = "no sprite"
    if sprite.is_collide_point(sprite1, pos_x, pos_y):
        spr = sprite1
    elif sprite.is_collide_point(sprite2, pos_x, pos_y):
        spr = sprite2
    elif sprite.is_collide_point(sprite3, pos_x, pos_y):
        spr = sprite3

    if spr != "no sprite":
        if key == wrap.K_UP:
            sprite.set_costume_next(spr)
        else:
            sprite.set_costume_prev(spr)


@wrap.on_key_always(wrap.K_LEFT)
def change_costume(pos_x, pos_y):
    spr = "no sprite"
    if sprite.is_collide_point(sprite1, pos_x, pos_y):
        spr = sprite1
    elif sprite.is_collide_point(sprite2, pos_x, pos_y):
        spr = sprite2
    elif sprite.is_collide_point(sprite3, pos_x, pos_y):
        spr = sprite3

    if spr != "no sprite":
        sprite.set_angle(spr, sprite.get_angle(spr) - 5)


@wrap.on_key_always(wrap.K_RIGHT)
def change_costume(pos_x, pos_y):
    spr = "no sprite"
    if sprite.is_collide_point(sprite1, pos_x, pos_y):
        spr = sprite1
    elif sprite.is_collide_point(sprite2, pos_x, pos_y):
        spr = sprite2
    elif sprite.is_collide_point(sprite3, pos_x, pos_y):
        spr = sprite3

    if spr != "no sprite":
        sprite.set_angle(spr, sprite.get_angle(spr) + 5)


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN)
def change_size(button, pos_x, pos_y):
    spr = "no sprite"
    if sprite.is_collide_point(sprite1, pos_x, pos_y):
        spr = sprite1
    elif sprite.is_collide_point(sprite2, pos_x, pos_y):
        spr = sprite2
    elif sprite.is_collide_point(sprite3, pos_x, pos_y):
        spr = sprite3

    if spr != "no sprite":
        if button==wrap.BUTTON_WHEELUP:
            sprite.set_height_proportionally(spr, sprite.get_height(spr) + 1)
        else:
            sprite.set_height_proportionally(spr, sprite.get_height(spr) - 1)
