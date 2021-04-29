import wrap, time
from wrap import world

wrap.world.create_world(450, 600, 900, 60)
wrap.world.set_back_color(100, 100, 100)

time.sleep(1)
wrap.sprite.add("pacman", 100, 100, "enemy_pink_down1")
time.sleep(1)
wrap.sprite.add_text("Кто здесь?", 100, 70, True, "arial", 12)

time.sleep(1.5)

wrap.sprite.add("pacman", 300, 100, "enemy_red_down1")
wrap.sprite.add_text("Я здесь", 300, 70, True, "arial", 12)

time.sleep(1)

wrap.sprite.add_text("О, привет!", 100, 50, True, "arial", 12)

time.sleep(1)
wrap.sprite.add("pacman", 200, 300, "enemy_yellow_down1")
time.sleep(0.5)
wrap.sprite.add_text("Я тоже здесь!", 200, 270, True, "arial", 12)

time.sleep(1)
wrap.sprite.add("pacman", 200, 200, "player1")
time.sleep(0.5)
wrap.sprite.add_text("Всем привет!", 200, 170, True, "arial", 12)
time.sleep(2)
wrap.sprite.add_text("Ой! Я кажется комнатой ошибся..", 200, 150, True, "arial", 12)