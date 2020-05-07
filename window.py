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
from playsound import playsound
import random
from entities import *

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
    pass

def update():
    if mouse.hovered_entity == "vehicle":
        if key == "f":
            print("f")
            distance: int = getDistanciationTo(orig=camera, to=vehicle)
            if distance <= 5:
                togo_X, togo_Y, togo_Z = vehicle.position[0], vehicle.position[1], vehicle.position[2]
                camera.position = Vec3(togo_X, togo_Y, togo_Z)
    gun.position = Vec3((camera.position[0] + 1), camera.position[1], (camera.position[2] + 1))


app = Ursina()

camera.position = Vec3(0, 4, 0)

app.run()