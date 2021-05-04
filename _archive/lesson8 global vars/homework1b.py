"""
Танк ездит по периметру поля.
Каждые 3 секунды на поле выпадает звезда. При сборе звезды - увеличивается счетчик звезд.
Каждые 3 звезды обмениваются на случайный элемент: бомбу или танк.
При сборе бомбы размер танка уменьшается. При сборе танка - увеличивается.
"""

import random, time
from wrap import world, sprite


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
        step_counter += 1

def make_star():
    global time_last_star, star

    now = time.time()
    if now - time_last_star < 3:
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
    star = sprite.add("battle_city_items", x, y, "block_gift_star")


world.create_world(500, 500)
world.set_back_color(100, 120, 150)

tank = sprite.add("battle_city_tanks", 30, 30, "tank_enemy_size1_green1")
tank_speed = 5

star = -1

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
