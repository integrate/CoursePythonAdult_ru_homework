"""
По центру экрана появляется броненосец в виде шара (спрайт mario-enemies, костюм armadillo_egg).

В случайном месте экрана появляется звезда из танков (спрайт battle_city_items, костюм block_gift_star).

Броненосец вращается и катится по направлению к звезде.
Когда он касается звезды, она исчезает. А в новом случайном месте появляется новая звезда.

После касания пятой звезды игра останавливается.
"""

import random
from wrap import world, sprite

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

goal_x = random.randint(30, 370)
goal_y = random.randint(30, 570)
goal = sprite.add("battle_city_items", goal_x, goal_y, "block_gift_star")
count_goal = 1

round = sprite.add("mario-enemies", 200, 300, "armadillo_egg")

while count_goal<=5:
    sprite.set_angle(round, sprite.get_angle(round)+10)
    sprite.move_at_angle_point(round, goal_x, goal_y, 3)

    if sprite.is_collide_sprite(round, goal):
        sprite.remove(goal)

        goal_x = random.randint(30, 370)
        goal_y = random.randint(30, 570)
        goal = sprite.add("battle_city_items", goal_x, goal_y, "block_gift_star")
        count_goal += 1

