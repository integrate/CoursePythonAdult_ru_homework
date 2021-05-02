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

    max_distance = sprite.get_left(tank_id)
    if distance > max_distance:
        distance = max_distance

    actions.move(tank_id, -distance, 0, distance * 1000 / speed_px_per_sec)


def move_right(tank_id, distance, speed_px_per_sec):
    max_distance = 400 - sprite.get_right(tank_id)
    if distance > max_distance:
        distance = max_distance

    sprite.set_angle(tank_id, 90)
    actions.move(tank_id, distance, 0, distance * 1000 / speed_px_per_sec)


def move_up(tank_id, distance, speed_px_per_sec):
    max_distance = sprite.get_top(tank_id)
    if distance > max_distance:
        distance = max_distance

    sprite.set_angle(tank_id, 0)
    actions.move(tank_id, 0, -distance, distance * 1000 / speed_px_per_sec)


def move_down(tank_id, distance, speed_px_per_sec):
    max_distance = 700 - sprite.get_bottom(tank_id)
    if distance > max_distance:
        distance = max_distance

    sprite.set_angle(tank_id, 180)
    actions.move(tank_id, 0, distance, distance * 1000 / speed_px_per_sec)


def fly_bullet(tank_id, distance):
    tank_angle = sprite.get_angle(tank_id)
    if tank_angle == 0:
        bullet = sprite.add("battle_city_items", sprite.get_x(tank_id), sprite.get_top(tank_id), "bullet")
    elif tank_angle == 180:
        bullet = sprite.add("battle_city_items", sprite.get_x(tank_id), sprite.get_bottom(tank_id), "bullet")
    elif tank_angle == -90:
        bullet = sprite.add("battle_city_items", sprite.get_left(tank_id), sprite.get_y(tank_id), "bullet")
    elif tank_angle == 90:
        bullet = sprite.add("battle_city_items", sprite.get_right(tank_id), sprite.get_y(tank_id), "bullet")

    sprite.set_angle(bullet, tank_angle)

    actions.move_at_angle_dir(bullet, distance, distance * 1000 / 200)
    sprite.remove(bullet)

def explosion(tank_id):
    sprite.hide(tank_id)

    x = sprite.get_x(tank_id)
    y = sprite.get_y(tank_id)

    effect = sprite.add("battle_city_items", x, y, "effect_explosion1")
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


world.create_world(400, 700, 900, 50)

tank1 = sprite.add("battle_city_tanks", 100, 100, "tank_player_size1_green1", False)
tank2 = sprite.add("battle_city_tanks", 200, 500, "tank_player_size1_yellow1", False)

appear(tank1)
appear(tank2)

move_right(tank1, 50, 100)
move_down(tank1, 20, 100)

move_left(tank2, 50, 100)
move_up(tank2, 50, 250)

fly_bullet(tank2, 100)
fly_bullet(tank1, 330)

explosion(tank2)
appear(tank2)
fly_bullet(tank2, 330)
explosion(tank1)