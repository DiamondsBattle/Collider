from ursina import *
from assets.prefabs.first_person_controller import FirstPersonController as FPS

class Player(Entity):
    __slots__ = ['hp', 'loadout', 'money']

    def __init__(self, hp, loadout, money, controller=FPS(), **kwargs):
        super().__init__(**kwargs, scale=(0.5, 0.5, 0.5))
        self.hp = hp
        self.loadout = loadout
        self.money = money
        # self.controller = controller

    def getHp(self):
        return self.hp

    def getLoadout(self):
        return self.loadout

    def getMoney(self):
        return self.money

    # def getController(self):
    #     return self.controller