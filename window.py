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


app = Ursina()

player = Player(model='player', hp=1000, loadout="Minigun")

crate = Entity(model='cube',
               color=color.rgb(255, 255, 255),
               scale=(2, 2, 2),
               texture='crate_high',
               collider='box',
               position=Vec3(0, 0, 10))

car_base = Entity(model='car_lp',
                  color=color.rgb(0, 0, 0),
                  scale=(0.01, 0.01, 0.01),
                  collider='car_lp',
                  position=Vec3(0, 5, 0),
                  rotation=Vec3(90, 0, 0))


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

car_mustang = Entity(model='car_lp',
                     scale=Vec3(1, 1, 1),
                     collider='car_lp',
                     position=Vec3(0, 10, 0),
                     color=color.orange)

app.run()