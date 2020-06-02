from ursina import *


class Player(Entity):
    __slots__ = ['hp', 'loadout', 'money']

    def __init__(self, hp, loadout: object, money, **kwargs):
        super().__init__(**kwargs, scale=(0.5, 0.5, 0.5))
        self.hp = hp
        self.loadout = loadout
        self.money = money
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
        self.interactions_names = ['talk', 'report', 'add_as_friend', 'add_as_enemy', 'pay']
        self.interactions_actions = {'talk': None,
                                     'report': None,
                                     'add_as_friend': None,
                                     'add_as_enemy': None,
                                     'pay': None}
        self.controller = None

    def getHp(self):
        return self.hp

    def getLoadout(self):
        return self.loadout

    def getMoney(self):
        return self.money
