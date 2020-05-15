from ursina import *
from time import sleep

class Bullet(Entity):
    def __init__(self, **kwargs):
        super().__init__(model, **kwargs)

    def move(self, bullet_speed, position):
        per_second_speed = bullet_speed
        per_milisecond_speed = (per_second_speed / 1000)
        something = True # Until a raycast detects the bullet touches something
        while something:
            position = ((position[0] + per_milisecond_speed), position[1], position[2])
            time.sleep(0.001)