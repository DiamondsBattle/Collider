from ursina import *


class Weapon(Entity):

    def __init__(self, name, **kwargs):
        self._scales = {'sniper': Vec3(.05, .05, .03),
                        'pistol': Vec3(.1, .1, .1),
                        'smg': Vec3(1, 1, 1),
                        'assault_rifle': Vec3(1, 1, 1),
                        'minigun': Vec3(1, 1, 1)}

        self._fire_rates = {'sniper': 2,
                            'pistol': .25,
                            'smg': .20,
                            'assault_rifle': .50,
                            'minigun': .10}

        self._ammo_types = {'sniper': 'heavy',
                            'pistol': 'light',
                            'smg': 'light',
                            'assault_rifle': 'normal',
                            'minigun': 'heavy'}

        self._charger_capacities = {'sniper': 4,
                                    'pistol': 15,
                                    'smg': 32,
                                    'assault_rifle': 25,
                                    'minigun': 9999}

        self._prices = {'sniper': 6789,
                        'pistol': 500,
                        'smg': 1230,
                        'assault_rifle': 2000,
                        'minigun': 5000}

        self._bullet_models = {'light': 'bullet_light',
                               'normal': 'bullet_normal',
                               'heavy': 'bullet_heavy'}

        self._bullet_speeds = {'light': 10,
                               'normal': 8,
                               'heavy': 7}

        self._max_ammos = {'sniper': 120,
                           'pistol': 4,
                           'smg': 4,
                           'assault_rifle': 4,
                           'minigun': 4}

        self._models = {'sniper': 'gun_sniper',
                        'pistol': 'gun_pistol',
                        'smg': 'gun_smg',
                        'assault_rifle': 'gun_assault_rifle',
                        'minigun': 'gun_minigun'}

        self._fire_rate = self._fire_rates[name]
        self._ammo_type = self._ammo_types[name]
        self._charger_capacity = self._charger_capacities[name]
        self._price = self._prices[name]
        self._bullet_model = self._bullet_models[self._ammo_type]
        self._bullet_speed = self._bullet_speeds[self._ammo_type]
        self._max_ammo = self._max_ammos[name]

        super().__init__(**kwargs, scale=self._scales[name], model=self._models[name], collider=self._models[name])

    def getFireRate(self):
        return self._fire_rate

    def getAmmoType(self):
        return self._ammo_type

    def getChargerCapacity(self):
        return self._charger_capacity

    def getPrice(self):
        return self._price

    def getBulletModel(self):
        return self._bullet_model

    def getBulletSpeed(self):
        return self._bullet_speed

    def getMaxAmmo(self):
        return self._max_ammo

    def interact(self):
        if mouse.hovered_entity == self:
            if distance(self, a):
                Text(text='[{}] to pick-up'.format(keybinds['interact']), position=Vec3(self.x, (self.y + 1), self.z))