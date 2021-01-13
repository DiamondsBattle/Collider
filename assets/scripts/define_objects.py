from ursina import *
from Boom.vehicle import Vehicle
from Boom.weapon import Weapon
from assets.shaders.basic_lightning import basic_lighting_shader


def defineObjects():
    crate = Entity(model='cube',
                   color=color.rgb(255, 255, 255),
                   scale=(2, 2, 2),
                   texture='crate_high',
                   collider='box',
                   position=Vec3(0, 0, 10),
                   shader=basic_lighting_shader)

    # car_turr = Vehicle(name='turr',
    #                    shader=basic_lighting_shader)
    # car_narrow = Vehicle(name='narrow',
    #                      shader=basic_lighting_shader)
    # # car_mustang = Vehicle(name='mustang',
    # # shader=basic_lighting_shader) # ERROR : 'ValueError: invalid literal for int() with base 10: '\n''
    # car_cabrot = Vehicle(name='cabrot',
    #                      shader=basic_lighting_shader)
    # car_blade = Vehicle(name='blade',
    #                     shader=basic_lighting_shader)

    gun_sniper = Weapon(name='sniper',
                        shader=basic_lighting_shader)
    gun_pistol = Weapon(name='pistol',
                        position=Vec3(2, 0, 0),
                        shader=basic_lighting_shader)
    gun_smg = Weapon(name='smg',
                     shader=basic_lighting_shader)
    gun_assault_rifle = Weapon(name='assault_rifle',
                               shader=basic_lighting_shader)
    gun_minigun = Weapon(name='minigun',
                         shader=basic_lighting_shader)

    ground = Entity(model='plane',
                    scale=32,
                    texture='grass',
                    texture_scale=(32, 32),
                    collider='box',
                    position=Vec3(0, 0, 0),
                    shader=basic_lighting_shader)

    sky = Sky(scale=100,
              collider='sky_dome',
              texture='sky_default')

    city = Entity(model='city_lp',
                  collider='dec_city',
                  scale=Vec3(0.25, 0.25, 0.25),
                  position=Vec3(0, 0, 0),
                  color=color.gray,
                  texture='palette',
                  shader=basic_lighting_shader)
