"""
На экране в фиксированном месте появляется Марио (спрайт mario-1-big или любой другой из этой серии).
На экране в случайном месте появляется утка (ищите в спрайте mario-enemies, название костюма начинается с duck_).
Марио перемещается к утке. Весь путь до утки он проходит за 3 шага. Т.е. за 3 перемещения. Для перемещения Марио в направлении утки подберите подходящую команду, начинающуюся со слова move_.
На каждом шагу теряет монетку (спрайт mario-items, костюм coin). Монетка появляется строго под марио.

Для расчета расстояния до утки используйте теорему пифагора. Для вычисления квадратного корня из числа используйте команду sqrt из модуля math.
Марио ловит утку. Она исчезает.
"""

import math
import random
from wrap import world, sprite, actions

world.create_world(400, 600, 900, 60)

#создаем марио
mario = sprite.add("mario-1-big", 40, 70, "stand")

# создаем утку
duck_x = random.randint(20, 350)
duck_y = random.randint(30, 550)
duck = sprite.add("mario-enemies", duck_x, duck_y, "duck_green_go")

#рассчитываем расстояние до утки
way = math.sqrt( (duck_x-40)**2 + (duck_y-70)**2 )

#делаем первый шаг в направлении точки, теряем монетку
actions.move_at_angle_point(mario, duck_x, duck_y, way/3)
coin = sprite.add("mario-items", 0, 0, "coin")
sprite.move_centerx_to(coin, sprite.get_centerx(mario))
sprite.move_top_to(coin, sprite.get_bottom(mario))

#второй шаг
actions.move_at_angle_point(mario, duck_x, duck_y, way/3)
coin = sprite.add("mario-items", 0, 0, "coin")
sprite.move_centerx_to(coin, sprite.get_centerx(mario))
sprite.move_top_to(coin, sprite.get_bottom(mario))

#третий шаг
actions.move_at_angle_point(mario, duck_x, duck_y, way/3)
coin = sprite.add("mario-items", 0, 0, "coin")
sprite.move_centerx_to(coin, sprite.get_centerx(mario))
sprite.move_top_to(coin, sprite.get_bottom(mario))

#убираем утку
sprite.hide(duck)