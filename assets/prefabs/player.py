from ursina import *
from assets.prefabs.first_person_controller import FirstPersonController as FPS

class Player(Entity):
    __slots__ = ['hp', 'loadout']

    def __init__(self, hp, loadout, **kwargs):
        super().__init__(**kwargs, scale=(0.5, 0.5, 0.5))
        self.player_controller = FPS()
        self.hp = hp
        self.loadout = loadout

    def get_hp(self):
        return self.hp

    def get_loadout(self):
        return self.loadout

class Bullet(Entity):

    def __init__(self, speed, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed

    def get_speed(self):
        return self.speed