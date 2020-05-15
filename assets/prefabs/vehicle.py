from ursina import *

class Vehicle(Entity):

    def __init__(self, armor, max_speed, acceleration, price, **kwargs):
        super().__init__(**kwargs)
        self.armor = armor
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.price = price

    def get_armor(self):
        return self.armor

    def get_max_speed(self):
        return self.max_speed

    def get_acceleration(self):
        return self.acceleration

    def get_price(self):
        return self.price