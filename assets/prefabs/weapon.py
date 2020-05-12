from ursina import *

class Weapon(Entity):

    def __init__(self, fire_rate, ammo_type, charger, price, **kwargs):
        super().__init__(**kwargs, scale=(0.25, 0.25, 0.25))
        self.fire_rate = fire_rate
        self.ammo_type = ammo_type
        self.charger = charger

    def get_fire_rate(self):
        return fire_rate

    def get_ammo_type(self):
        return ammo_type

    def get_charger(self):
        return charger

    def get_price(self):
        return price