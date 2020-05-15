from ursina import *


class Weapon(Entity):

    def __init__(self, fire_rate, ammo_type, charger, price, **kwargs):
        super().__init__(**kwargs, scale=(0.25, 0.25, 0.25))
        self.fire_rate = fire_rate
        self.ammo_type = ammo_type
        self.charger = charger
        self.price = price
        self.ammo_in_clip = charger
        self.bullets_models = {'light': 'bullet_light',
                               'normal': 'bullet_normal',
                               'heavy': 'bullet_heavy'}
        self.bullets_speed = {'light': '10',
                              'normal': '8',
                              'heavy': '7'}

    def getFireRate(self):
        return self.fire_rate

    def getAmmoType(self):
        return self.ammo_type

    def getCharger(self):
        return self.charger

    def getPrice(self):
        return self.price

    def getBulletModel(self):
        return self.bullets_models[self.ammo_type]

    def getBulletSpeed(self):
        return self.bullet_speed[self.ammo_type]
