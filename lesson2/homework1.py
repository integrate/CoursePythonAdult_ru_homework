"""
Сделать погоню Марио за его добычей по определенной траектории.
Поменять значения переменных. Теперь какой-то персонаж бежит за марио по той-же траектории.
"""

import time, wrap

wrap.world.create_world(400, 600, 900, 60)
wrap.world.set_back_color(100, 50, 230)

#настройки
# hunter_sprite_type = "mario-1-big"
# hunter_costume = "stand"
# victim_sprite_type = "mario-enemies"
# victim_costume="mushroom"
# text1 = "Стой, ты мой ужин!!!"
# text2 = "Неет! Я ядовитый!!!"

hunter_sprite_type = "mario-enemies"
hunter_costume = "crab"
victim_sprite_type = "mario-2-big"
victim_costume="stand"
text1 = "Может поплаваем?"
text2 = "Спасибо, я пешком!"

#создаем игроков
wrap.sprite.add(hunter_sprite_type, 50, 100, hunter_costume)
wrap.sprite.add(victim_sprite_type, 150, 100, victim_costume)

time.sleep(1)
wrap.sprite.add_text(text1, 80, 60, True, "arial", 15)
time.sleep(1)
wrap.sprite.add_text(text2, 150, 40, True, "arial", 15)
time.sleep(1)

wrap.action.move_to_pos(1, 250, 100)
wrap.action.move_to_pos(0, 150, 100)

wrap.action.move_to_pos(1, 300, 150)
wrap.action.move_to_pos(0, 250, 100)

wrap.action.move_to_pos(1, 300, 250)
wrap.action.move_to_pos(0, 300, 150)