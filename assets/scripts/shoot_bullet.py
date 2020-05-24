from ursina import *
from time import sleep
from assets.prefabs.bullet import Bullet

def shoot(gun, gun_pos, facing):
    speed = gun.getBulletSpeed
    bullet_model = gun.getBulletModel
    origin = gun_pos
    facing = facing
    Bullet(speed=speed, model=bullet_model, position=origin)
    Bullet.move(self, bullet_speed=speed, position=Bullet.position)

def shoot_test():
    bullet = Entity(model='sphere')
    for i in range(20):
        time.sleep(2)
        bullet.position += 1