"""
Жмурки.
В верхнем левом углу появляется танк.
В нижнем правом, на координатах 300, 300, появляется база танков (спрайт battle_city_items, костюм base).

Определяется угол движения от танка к базе.
Выбирается случайный угол от -30 до +30 градусов от угла, который ведет от танка к базе.
Танк идет по выбранному углу к базе 100 пикселей.

Пользователь вводит координаты x и y. В направлении указанной точки база идет 100 пикселей.

После каждого движения (танка или базы) идет проверка,
поймал танк базу или нет (исп функцию sprite.is_collide_sprite() )

Если база поймана, то она плавно уменьшается до размера 1*1 пиксель, и игра прекращается (команда exit()).

Все повторяется до 5 ходов базы. Если база не была поймана за 5 ходов, значит игрок победил.
"""

import math
import random
from wrap import world, sprite, actions

world.create_world(400, 600, 900, 60)

#создаем танк
tank = sprite.add("battle_city_tanks", 40, 70, "tank_enemy_size1_green1")
base = sprite.add("battle_city_items", 300, 300, "base")

#ход танка
angle = sprite.calc_angle_by_point(tank, sprite.get_x(base), sprite.get_y(base))
go_to_angle = random.randint(int(angle)-30, int(angle)+30)
actions.set_angle(tank, go_to_angle)
actions.move_at_angle_dir(tank, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход базы
x = int(input("Введите X"))
y = int(input("Введите Y"))
actions.move_at_angle_point(base, x, y, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход танка
angle = sprite.calc_angle_by_point(tank, sprite.get_x(base), sprite.get_y(base))
go_to_angle = random.randint(int(angle)-30, int(angle)+30)
actions.set_angle(tank, go_to_angle)
actions.move_at_angle_dir(tank, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход базы
x = int(input("Введите X"))
y = int(input("Введите Y"))
actions.move_at_angle_point(base, x, y, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход танка
angle = sprite.calc_angle_by_point(tank, sprite.get_x(base), sprite.get_y(base))
go_to_angle = random.randint(int(angle)-30, int(angle)+30)
actions.set_angle(tank, go_to_angle)
actions.move_at_angle_dir(tank, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход базы
x = int(input("Введите X"))
y = int(input("Введите Y"))
actions.move_at_angle_point(base, x, y, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход танка
angle = sprite.calc_angle_by_point(tank, sprite.get_x(base), sprite.get_y(base))
go_to_angle = random.randint(int(angle)-30, int(angle)+30)
actions.set_angle(tank, go_to_angle)
actions.move_at_angle_dir(tank, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход базы
x = int(input("Введите X"))
y = int(input("Введите Y"))
actions.move_at_angle_point(base, x, y, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход танка
angle = sprite.calc_angle_by_point(tank, sprite.get_x(base), sprite.get_y(base))
go_to_angle = random.randint(int(angle)-30, int(angle)+30)
actions.set_angle(tank, go_to_angle)
actions.move_at_angle_dir(tank, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)

#ход базы
x = int(input("Введите X"))
y = int(input("Введите Y"))
actions.move_at_angle_point(base, x, y, 100)

if sprite.is_collide_sprite(tank, base):
    actions.set_size(base, 1, 1, 2000)