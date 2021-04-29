"""
Снеговик из монстров.
В правой части экрана выбирается случайная координата x, на которой будут создаваться монстры.
Например: если ширина экрана у вас 400 пикселей, то координата x должна быть равна от 200 до 400 пикселей.
Т.е. в правой половине экрана.

Спрашиваем у пользователя в консоли ввести высоту центрального монстра “Введите высоту центрального монстра”.
Создаем монстра.
Координата X этого первого монстра должна быть равна случайной координате, которую мы выбрали ранее.
Координата Y должна указывать на середину экрана по высоте.
Меняем высоту монстра на то число, которое указал пользователь.
Для того, чтобы вместе с высотой поменялась и ширина монстра пропорционально, используйте команду
sprite.set_height_proportionally().

Сверху на мостра ставим второго. Его высота должна быть в два раза меньше, чем у центрального.
Под первым монстром создаем еще одного монстра. Его высота должна быть в два раза больше первого.
Таким образом у нас получается снеговик из монстров.

В левой части экрана появляется пакмэн.
Его высота должна быть 20% от общей высоты всех трех монстров.
Его координата по Y должна совпадать с серединой всего снеговика.
Пакмэн говорит “Ааааа!!!”.
Все монстры поворачиваются в его направлении (исп команду set_angle_to_point() ).
Все по очереди монстры перемещаются на Пакмэна. Пакмэн исчезает.
"""

import random
from wrap import sprite, actions, world

world.create_world(400, 600, 900, 60)
world.set_back_color(100, 200, 10)

#определяем координаты монстра
monsterx = random.randint(200, 400)
monstery = 300

#узнаем высоту монстра
height1 = int(input("Введите высоту центрального монстра:"))

#создаем монстра и меняем его размер с сохранением пропорций
monster1 = sprite.add("pacman", monsterx, monstery, "enemy_blue_down1")
sprite.set_height_proportionally(monster1, height1)

#создаем верхнего монстра
monster2 = sprite.add("pacman", monsterx, monstery, costume="enemy_red_down1")
sprite.set_height_proportionally(monster2, height1/2)
sprite.move_bottom_to(monster2, sprite.get_top(monster1))

#создаем нижнего монстра
monster3 = sprite.add("pacman", monsterx, monstery, costume="enemy_yellow_down1")
sprite.set_height_proportionally(monster3, height1*2)
sprite.move_top_to(monster3, sprite.get_bottom(monster1))

#определяем высоту монстра
full_height=sprite.get_bottom(monster3) - sprite.get_top(monster2)
pacman_height = full_height*0.2

#определяем положение монстра по Y. От верхушки верхнего монстра идем вниз на половину полной высоты.
pacman_y = sprite.get_top(monster2) + full_height/2

#создаем пакмэна и ставим ему размер
pacman = sprite.add("pacman", 50, pacman_y, "player2")
sprite.set_height_proportionally(pacman, pacman_height)

#крик ужаса
sprite.add_text("Аaaaaaaa", 50, sprite.get_top(pacman) - 20)

#поворот монстров к цели
actions.set_angle_to_point(monster1,50,pacman_y)
actions.set_angle_to_point(monster2,50,pacman_y)
actions.set_angle_to_point(monster3,50,pacman_y)

#монстры идут к пакмэну
actions.move_to(monster2, 50, pacman_y)
actions.move_to(monster1, 50, pacman_y)
actions.move_to(monster3, 50, pacman_y)

#пакмэна съели
sprite.hide(pacman)