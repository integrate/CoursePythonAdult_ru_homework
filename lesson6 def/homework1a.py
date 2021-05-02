import time
from wrap import world, sprite, actions

def appear(tank_id):
    x = sprite.get_x(tank_id)
    y = sprite.get_y(tank_id)

    effect = sprite.add("battle_city_items", x, y, "effect_appearance1")
    time.sleep(0.1)
    sprite.set_costume_next(effect)
    time.sleep(0.1)
    sprite.set_costume_next(effect)
    time.sleep(0.1)
    sprite.set_costume_next(effect)
    time.sleep(0.1)

    sprite.set_costume_prev(effect)
    time.sleep(0.1)
    sprite.set_costume_next(effect)
    time.sleep(0.1)
    sprite.set_costume_prev(effect)
    time.sleep(0.1)
    sprite.set_costume_next(effect)
    time.sleep(0.2)

    sprite.remove(effect)

    sprite.show(tank_id)

def move_left(tank_id, distance, speed_px_per_sec):
    sprite.set_angle(tank_id, -90)
    actions.move(tank_id, -distance, 0, distance*1000/speed_px_per_sec)

def move_right(tank_id, distance, speed_px_per_sec):
    sprite.set_angle(tank_id, 90)
    actions.move(tank_id, distance, 0, distance*1000/speed_px_per_sec)

def move_up(tank_id, distance, speed_px_per_sec):
    sprite.set_angle(tank_id, 0)
    actions.move(tank_id, 0, -distance, distance*1000/speed_px_per_sec)

def move_down(tank_id, distance, speed_px_per_sec):
    sprite.set_angle(tank_id, 180)
    actions.move(tank_id, 0, distance, distance*1000/speed_px_per_sec)

world.create_world(400, 700, 900, 50)

tank1 = sprite.add("battle_city_tanks", 100, 100, "tank_player_size1_green1", False)
tank2 = sprite.add("battle_city_tanks", 200, 300, "tank_player_size1_yellow1", False)
appear(tank1)
appear(tank2)

move_left(tank1, 100, 100)
move_down(tank1, 200, 100)

move_right(tank2, 50, 100)
move_up(tank2, 50, 25)