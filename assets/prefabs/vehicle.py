from ursina import *


class Vehicle(Entity):

    def __init__(self, name, **kwargs):
        self.name = name
        self._models = {'turr': 'car_turr',
                        'narrow': 'car_narrow',
                        'mustang': 'car_mustang',
                        'cabrot': 'car_cabrot',
                        'blade': 'car_blade'}
        self._armors = {'turr': 0,
                        'narrow': 1,
                        'mustang': 2,
                        'cabrot': 3,
                        'blade': 5}
        self._max_speeds = {'turr': 100,
                            'narrow': 150,
                            'mustang': 170,
                            'cabrot': 210,
                            'blade': 260}
        self._times_to_100_kmph = {'turr': 8,
                                   'narrow': 5,
                                   'mustang': 6,
                                   'cabrot': 4,
                                   'blade': 3}
        self._prices = {'turr': 10000,
                        'narrow': 28500,
                        'mustang': 58900,
                        'cabrot': 105000,
                        'blade': 250000}
        self._scales = {'turr': Vec3(.01, .01, .01),
                        'narrow': 0,
                        'mustang': 0,
                        'cabrot': 0,
                        'blade': 0}

        self._armor = self._armors[name]
        self._max_speed = self._max_speeds[name]
        self._time_to_100_kmph = self._times_to_100_kmph[name]
        self._scale = self._scales[name]

        super().__init__(**kwargs, model=self._models[name], scale=self._scale)

    def get_armor(self):
        return self._armor

    def get_max_speed(self):
        return self._max_speed

    def get_acceleration(self):
        return self._time_to_100_kmph

    def get_price(self):
        return self._price
