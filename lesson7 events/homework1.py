"""
Создается спрайт танк.
Каждую секнду он меняет свое положение на случайное.
Задача игрока - попасть по этому танку. Если попал - костюм танка меняется на следующий танк.

При нажатии клавиши Вверх за мышью начинает ходить маленький прицел (спрайт pacman, костюм player2, поворот 0гр).
Размер 50% от оригинального.
При повторном нажатии - прицел становится размером 100% от оригинального.
При повторном нажатии - прицел становится размером 150% от оригинального.
При повторном нажатии - прицел прицел исчезает.
При повторном нажатии опять появляется маленький прицел (50% от оригинального).

Если есть прицел, то попадание считается, если во время клика прицел касался танка.
Если нет прицела, то попаданием считается, если игрок кликнул точно по танку.
"""

import random

import wrap
from wrap import world, sprite

world.create_world(400, 700, 900, 50)

target = sprite.add("battle_city_tanks", 200, 350)
aim = sprite.add("pacman", 200, 350, "player2", False)
sprite.set_angle(aim, 0)


@wrap.always(1000)
def move_target():
    sprite.move_to(target, random.randint(30, 370), random.randint(30, 670))


@wrap.on_key_down(wrap.K_UP)
def change_aim():
    if not sprite.is_visible(aim):
        sprite.set_size_percent(aim, 50, 50)
        sprite.show(aim)
    elif sprite.is_visible(aim) and sprite.get_width_percent(aim) == 50:
        sprite.set_size_percent(aim, 100, 100)
    elif sprite.is_visible(aim) and sprite.get_width_percent(aim) == 100:
        sprite.set_size_percent(aim, 150, 150)
    else:
        sprite.hide(aim)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def on_mouse_button_down(pos_x, pos_y):
    if not sprite.is_visible(aim):
        popal = sprite.is_collide_point(target, pos_x, pos_y)
    else:
        popal = sprite.is_collide_sprite(target, aim)

    if popal:
        sprite.set_costume_next(target)
        sprite.set_costume_next(target)

@wrap.on_mouse_move
def on_mouse_move(pos_x, pos_y):
    sprite.move_to(aim,pos_x, pos_y)