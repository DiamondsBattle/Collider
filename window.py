# DONE : Add Ground
# DONE : Add Sky
# DONE : Add FirstPersonView
# DONE : Add Crate
# DONE : Add Crate Texture
# TODO : Add Car
# TODO : Add Gun
# TODO : Add Shooting
# TODO : Add Texture Packs
# TODO : Add Menu
# TODO : Add Pause
# TODO : Add loadouts and multiple hands
# TODO : Add Narrator
# TODO : Add Music Player
# TODO : Add SFX
# TODO : Add Game Saving
# TODO : Add Multi-Player

from ursina import *
from assets.prefabs.main_menu import MainMenu as MM
from assets.prefabs.player import Player
from assets.prefabs.vehicle import Vehicle
from assets.prefabs.weapon import Weapon

def getDistanciationTo(orig: object, to: object) -> int:
    if orig.position[0] >= to.position[0]:
        pos_X = orig.position[0] - to.position[0]
    else:
        pos_X = to.position[0] - orig.position[0]

    if orig.position[2] >= to.position[2]:
        pos_Z = orig.position[2] - to.position[2]
    else:
        pos_Z = orig.position[2] >= to.position[2]

    distanciation = (sqrt((pos_X * pos_X) + (pos_Z * pos_Z)))
    return int(distanciation)

def input(key):
    if key == "mouse_left":
        print("Shooted")

def update():
    if mouse.hovered_entity == "vehicle":
        if key == "f":
            print("f")
            distance: int = getDistanciationTo(orig=camera, to=vehicle)
            if distance <= 5:
                togo_X, togo_Y, togo_Z = vehicle.position[0], vehicle.position[1], vehicle.position[2]
                camera.position = Vec3(togo_X, togo_Y, togo_Z)
    if key == "escape":
        change_menu_all_visibility(conf=True)

def change_menu_all_visibility(conf):
    if conf:
        menu.enabled = not menu.enabled
        menu.btn_solo.enabled = not menu.btn_solo.enabled
        menu.btn_multi.enabled = not menu.btn_multi.enabled
        menu.btn_quit.enabled = not menu.btn_quit.enabled


app = Ursina()


crate = Entity(model='cube',
               color=color.rgb(255, 255, 255),
               scale=(2, 2, 2),
               texture='crate_high',
               collider='box',
               position=Vec3(0, 0, 10))


car_turr = Vehicle(model='car_turr',
               armor=0,
               max_speed=100,
               acceleration=8,
               price=1000)

car_narrow = Vehicle(model='car_narrow',
                 armor=1,
                 max_speed=150,
                 acceleration=5,
                 price=2850)

# car_mustang = Vehicle(model='car_mustang', # ERROR : 'ValueError: invalid literal for int() with base 10: '\n''
# armor=2,
# max_speed=170,
# acceleration=6,
# price=5890)

car_cabrot = Vehicle(model='car_cabrot',
                 armor=3,
                 max_speed=210,
                 acceleration=4,
                 price=10500)

car_blade = Vehicle(model='car_blade',
                armor=5,
                max_speed=260,
                acceleration=3,
                price=25000)


gun_sniper = Weapon(model='gun_sniper',
                    fire_rate=2,
                    ammo_type='heavy',
                    charger=4,
                    price=6789)

gun_pistol = Weapon(model='gun_pistol',
                    fire_rate=.25,
                    ammo_type='light',
                    charger=15,
                    price=500)

gun_smg = Weapon(model='gun_smg',
                 fire_rate=.20,
                 ammo_type='light',
                 charger=32,
                 price=1230)

gun_assault_rifle = Weapon(model='gun_assault_rifle',
                           fire_rate=.50,
                           ammo_type='normal',
                           charger=25,
                           price=2000)

gun_minigun = Weapon(model='gun_minigun',
                     fire_rate=.10,
                     ammo_type='heavy',
                     charger=9999,
                     price=5000)


ground = Entity(model='plane',
                scale=32,
                texture='grass',
                texture_scale=(32, 32),
                collider='box',
                position=Vec3(0, 0, 0))

sky = Sky(scale=100,
          collider='sky_dome',
          texture='default_sky')

# city = Entity(model='city_lp',
#               collider='city_lp',
#               scale=Vec3(0.25, 0.25, 0.25),
#               position=Vec3(0, 0, 0),
#               color=color.gray,
#               texture='palette')

menu = MM(model='quad', texture='background', scale=(15, 8.5))
app.run()