from ursina import *
from assets.prefabs.first_person_controller import FirstPersonController as FPS

class Player(Entity):
    __slots__ = ['hp', 'loadout', 'money', 'controller']

    def __init__(self, hp, loadout, money, controller=FPS(), **kwargs):
        super().__init__(**kwargs, scale=(0.5, 0.5, 0.5))
        self.hp = hp
        self.loadout = loadout
        self.money = money
        self.controller = controller
        self.status = {'is_walking': False,
                       'is_jumping': False,
                       'is_driving': False,
                       'is_swimming': False,
                       'is_shooting': False,
                       'is_in_car': False,
                       'is_paused': False,
                       'is_dead': False,
                       'is_falling': False,
                       }

    def getHp(self):
        return self.hp

    def getLoadout(self):
        return self.loadout

    def getMoney(self):
        return self.money

    def getController(self):
        return self.controller