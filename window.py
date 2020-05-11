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
from assets.prefabs.first_person_controller import FirstPersonController

class Menu:

    def __init__(self):
        self.button_solo = Button(text='Solo',
                                  color=color.black,
                                  highlight_color=color.black33)

        self.button_multi = Button(text='Multiplayer',
                                   color=color.black,
                                   highlight_color=color.black33,
                                   on_click=play_multiplayer)

        self.button_quit = Button(text='Quit Game',
                                  color=color.black,
                                  highlight_color=color.red,
                                  on_click=self.quit_app,
                                  )

    def play(self):
        application.resume()

    def resume(self):
        application.resume()

    def quit_app(self):
        application.quit()

    def quit_mode(self):
        pass
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
        menu.enabled = not menu.enabled

class Player(Entity):
    __slots__ = ['hp', 'loadout']

    def __init__(self, hp, loadout, **kwargs):
        super().__init__(**kwargs)
        self.player_controller = FirstPersonController()
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

class Weapon(Entity):

    def __init__(self, fire_rate, ammo_type, charger, price, **kwargs):
        super().__init__(**kwargs)
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

class Car(Entity):

    def __init__(self, armor, max_speed, acceleration, price, **kwargs):
        super().__init__(**kwargs)
        self.armor = armor
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.price = price

    def get_armor(self):
        return armor

    def get_max_speed(self):
        return max_speed

    def get_acceleration(self):
        return acceleration

    def get_price(self):
        return price


app = Ursina()

player = Player(model='player',
                hp=1000,
                loadout="pistol")

crate = Entity(model='cube',
               color=color.rgb(255, 255, 255),
               scale=(2, 2, 2),
               texture='crate_high',
               collider='box',
               position=Vec3(0, 0, 10))


car_turr = Car(model='car_turr',
               armor=0,
               max_speed=100,
               acceleration=8,
               price=1000)

car_narrow = Car(model='car_narrow',
                 armor=1,
                 max_speed=150,
                 acceleration=5,
                 price=2850)

# car_mustang = Car(model='car_mustang', # ERROR : 'ValueError: invalid literal for int() with base 10: '\n''
# armor=2,
# max_speed=170,
# acceleration=6,
# price=5890)

car_cabrot = Car(model='car_cabrot',
                 armor=3,
                 max_speed=210,
                 acceleration=4,
                 price=10500)

car_blade = Car(model='car_blade',
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

menu = Menu
app.run()