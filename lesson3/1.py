import wrap, random
from wrap import sprite, actions as sprite_actions, world
from random import randint
from time import sleep

world_x = 500
world_y = 500
world.create_world(world_x, world_y)

monsterx = randint(world_x / 2, world_x)
monstery = world_y / 2
monster1 = sprite.add("pacman", monsterx, monstery, costume="enemy_blue_down1")

x1 = int(input("Введите размер первого монстра(размер в процентах) ?"))
y1 = int(input("Введите размер первого монстра(размер в процентах) ?"))

sprite.set_size_percent(monster1, x1, y1)

monster2 = sprite.add("pacman", monsterx, monstery - 30, costume="enemy_red_down1")
sprite.set_size_percent(monster2, x1 / 2, y1 / 2)
sprite.move_to(monster2, monsterx, sprite.get_top(monster1) - (sprite.get_height(monster2) / 2))

monster3 = sprite.add("pacman", monsterx, monstery + 60, costume="enemy_yellow_down1")
sprite.set_size_percent(monster3, x1 * 2, y1 * 2)
sprite.move_to(monster3, monsterx, sprite.get_bottom(monster1) + (sprite.get_height(monster3) / 2))

packman = sprite.add("pacman", monsterx - 100,monstery,costume="player2")
x2=sprite.get_width(monster3)
y2=sprite.get_bottom(monster3) - sprite.get_top(monster2)
sprite.set_size(packman, x2 / 2, y2 / 5)
sprite.add_text("Аaaaaaaa", monsterx - 100, sprite.get_top(packman) - 20,
                text_color=(255, 252, 24))

# point = (monsterx - 100,monstery )
# sprite.calc_angle_by_point(monster1, point)
#
# sprite_actions.rotate_to_angle(monster1, 1000, sprite.set_final_angle)
sprite_actions.set_angle_to_point(monster1,monsterx-100,monstery)
sprite_actions.set_angle_to_point(monster2,monsterx-100,monstery)
sprite_actions.set_angle_to_point(monster3,monsterx-100,monstery)
