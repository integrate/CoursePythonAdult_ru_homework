"""
Усложнение.
При сборе звезды высота броненосца вырастает на 5 пикселей.
Ширина вырастает пропорционально (исп команду set_height_proportionally()).

В игре должен быть таймер. Он показывает количество секунд, прошедших с момента старта игры.

Игра должна продолжаться ровно 15 секунд.
На экране должно рисоваться число, показывающее, сколько звезд собрал броненосец.
Через 15 секунд игра останавливается и счетчик собранных звезд показывает,
  сколько звезд успел собрать броненосец за 15 секунд.
"""

import random, time
from wrap import world, sprite, sprite_text

#создаем мир
world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

#ставим первую цель
goal_x = random.randint(30, 370)
goal_y = random.randint(30, 570)
goal = sprite.add("battle_city_items", goal_x, goal_y, "block_gift_star")
count_goal = 1

#создаем игрока
round = sprite.add("mario-enemies", 200, 300, "armadillo_egg")

#создаем надпись с таймером и засекаем время начала
timer = sprite.add_text("Time: --", 50, 30)
time_start = time.time()
time_end = time.time()

#создаем надпись для счетчика собранных звезд
count_text = sprite.add_text("Count: 0", 50, 60)

while time_end-time_start<20:
    #обновляем время на таймера
    time_end = time.time()
    sprite_text.set_text(timer, "Time: "+str(int(time_end-time_start)))

    #поворачиваем игрока, чтобы вращался
    sprite.set_angle(round, sprite.get_angle(round)+10)
    sprite.move_at_angle_point(round, goal_x, goal_y, 33)

    #если коснулись звезды
    if sprite.is_collide_sprite(round, goal):
        #удаляем старую звезду
        sprite.remove(goal)

        #добавляем новую звезду
        goal_x = random.randint(30, 370)
        goal_y = random.randint(30, 570)
        goal = sprite.add("battle_city_items", goal_x, goal_y, "block_gift_star")
        count_goal += 1

        #меняем надпись с количеством звезд
        sprite_text.set_text(count_text, "Count: "+str(count_goal-1))

        #увеличиваем размер игрока
        sprite.set_height_proportionally(round, sprite.get_height(round)+5)