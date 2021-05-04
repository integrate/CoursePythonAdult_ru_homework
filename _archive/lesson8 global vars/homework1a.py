"""
Танк ездит по периметру поля.
Каждые 3 секунды на поле выпадает звезда.
"""

import random, time
from wrap import world, sprite, sprite_text


def collect_star():
    global stars_collected, tank_speed
    if not sprite.is_exist(star):
        return

    if not sprite.is_collide_sprite(tank, star):
        return

    costume = sprite.get_costume(star)
    if costume == "block_gift_star":
        stars_collected += 1
        sprite_text.set_text(stars_text, "Stars:" + str(stars_collected))
    elif costume == "block_gift_tank":
        sprite.set_size_percent_of(tank, 110)
        tank_speed += 3
    elif costume == "block_gift_bomb":
        sprite.set_size_percent_of(tank, 90)
        tank_speed += 3

    sprite.remove(star)


def go_up_down(place_y):
    sprite.set_angle_to_point(tank, sprite.get_x(tank), place_y)

    way = place_y - sprite.get_y(tank)
    speed = tank_speed
    if way < 0:
        speed = -speed

    steps = way / speed
    step_counter = 0
    while step_counter < steps:
        sprite.move(tank, 0, speed)
        collect_star()
        step_counter += 1


def go_left_right(place_x):
    sprite.set_angle_to_point(tank, place_x, sprite.get_y(tank))

    way = place_x - sprite.get_x(tank)
    speed = tank_speed
    if way < 0:
        speed = -speed

    steps = way / speed
    step_counter = 0
    while step_counter < steps:
        sprite.move(tank, speed, 0)
        collect_star()
        step_counter += 1


def make_star():
    global time_last_star, star, stars_collected

    now = time.time()
    if now - time_last_star < 3:
        return

    if sprite.is_exist(star):
        return

    side = random.choice(["left", "right", "top", "bottom"])
    if side == "left":
        x = 30
        y = random.randint(30, 470)
    elif side == "right":
        x = 470
        y = random.randint(30, 470)
    elif side == "top":
        x = random.randint(30, 470)
        y = 30
    elif side == "bottom":
        x = random.randint(30, 470)
        y = 470

    if sprite.is_exist(star):
        sprite.remove(star)

    if stars_collected >= 3:
        stars_collected -= 3
        sprite_text.set_text(stars_text, "Stars:" + str(stars_collected))

        costume = random.choice(["block_gift_bomb", "block_gift_tank"])
        star = sprite.add("battle_city_items", x, y, costume)
    else:
        star = sprite.add("battle_city_items", x, y, "block_gift_star")


world.create_world(500, 500)
world.set_back_color(100, 120, 150)

tank = sprite.add("battle_city_tanks", 30, 30, "tank_enemy_size1_green1")
tank_speed = 10

star = -1

stars_collected = 0
stars_text = sprite.add_text("Stars:0", 250, 250)

time_last_star = time.time()

while True:
    go_up_down(470)
    make_star()
    go_left_right(470)
    make_star()
    go_up_down(30)
    make_star()
    go_left_right(30)
    make_star()
