from ursina import *
from playsound import playsound
import random
from assets.prefabs import first_person_controller

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
    global info, title, debug_build
    if mouse.hovered_entity is not None:
        info.text = mouse.hovered_entity.name
    if mouse.hovered_entity == "vehicle":
        if key == "f":
            print("f")
            distance: int = getDistanciationTo(orig=camera, to=vehicle)
            if distance <= 5:
                togo_X, togo_Y, togo_Z = vehicle.position[0], vehicle.position[1], vehicle.position[2]
                camera.position = Vec3(togo_X, togo_Y, togo_Z)
    debug_fps = window.fps_counter.text
    title = 'Collider [[DEBUG : Development Mode=' + str(development_mode) + ' || Version=' + str(version) + ' || FPS=' + str(debug_fps) + ' || Build=' + str(debug_build) + ']]'
    window.title = str(title)


app = Ursina()



app.run()