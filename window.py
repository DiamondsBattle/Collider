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
        application.pause = not pause

class Player(Entity):
    __slots__ = [model, hp, loadout]

    def __init__(self, model, hp, loadout, **kwargs):
        super().__init__(**kwargs)
        self.player_controller = FirstPersonController()
        self.model = model
        self.hp = hp
        self.loadout = loadout

    def get_model(self):
        return self.model

    def get_hp(self):
        return self.hp

    def get_loadout(self):
        return self.loadout

class Bullet(Entity):

    def __init__(self, model, speed, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.speed = speed

    def get_model(self):
        return self.model

    def get_speed(self):
        return self.speed

class Weapon(Entity):

    def __init__(self, model, fire_rate, ammo_type, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.fire_rate = fire_rate
        self.ammo_type = ammo_type

    def get_model(self):
        return model

    def get_fire_rate(self):
        return fire_rate

    def get_ammo_type(self):
        return ammo_type

class Car(Entity):

    def __init__(self, model, armor, max_speed, acceleration, price, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.armor = armor
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.price = price

    def get_model(self):
        return model

    def get_armor(self):
        return armor

    def get_max_speed(self):
        return max_speed

    def get_acceleration(self):
        return acceleration

    def get_price(self):
        return price


app = Ursina()

player = Player(model='player', hp=1000, loadout="Minigun")

crate = Entity(model='cube',
               color=color.rgb(255, 255, 255),
               scale=(2, 2, 2),
               texture='crate_high',
               collider='box',
               position=Vec3(0, 0, 10))


car_turr = Car(model='car_turr', armor=0, max_speed=100, acceleration=8, price=1000)
car_narrow = Car(model='car_narrow', armor=1, max_speed=150, acceleration=5, price=2850)
car_mustang = Car(model='car_mustang', armor=2, max_speed=170, acceleration=6, price=5890)
car_cabrot = Car(model='car_cabrot', armor=3, max_speed=210, acceleration=4, price=10500)
car_blade = Car(model='car_blade', armor=5, max_speed=260, acceleration=3, price=25000)

gun_sniper = Weapon(model='gun_sniper', fire_rate=2, ammo_type='heavy')
gun_pistol = Weapon(model='gun_pistol', fire_rate=.25, ammo_type='light')
gun_smg = Weapon(model='gun_smg', fire_rate=.10, ammo_type='light')
gun_assault_rifle = Weapon(model='gun_assault_rifle', fire_rate=.50, ammo_type='normal')

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

gun = Entity(parent=player.player_controller,
             model='gun_lp',
             color=color.gray,
             position=(player_controller.position[0],
                       player_controller.position[1],
                       (player_controller.position[2] + 3)),
             rotation_y=90,
             scale=Vec3(0.25, 0.25, 0.25),
             collider='gun_lp')


app.run()