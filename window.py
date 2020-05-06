from ursina import *
from playsound import playsound
import random
from assets.prefabs import first_person_controller

def getDistanceTo(orig: object, to: object) -> object:
    if orig.position[0] >= to.position[0]:
        pos_X = orig.position[0] - to.position[0]
    else:
        pos_X = to.position[0] - orig.position[0]

    if orig.position[2] >= to.position[2]:
        pos_Z = orig.position[2] - to.position[2]
    else:
        pos_Z = orig.position[2] >= to.position[2]

    distance = (sqrt((pos_X * pos_X) + (pos_Z * pos_Z)))
    return(distance)

def addInfoBox():
    global info1

def delInfoBox():
    global info

def input(key):
    pass

def update():
    global info, title, debug_build
    if mouse.hovered_entity is not None:
        info.text = mouse.hovered_entity.name
    if mouse.hovered_entity == "vehicle":
        if key == "f":
            print("f")
            distance = getDistanceTo(orig=camera, to=vehicle)
            if distance <= 5:
                togo_X, togo_Y, togo_Z = vehicle.position[0], vehicle.position[1], vehicle.position[2]
                camera.position = Vec3(togo_X, togo_Y, togo_Z)
    debug_fps = window.fps_counter.text
    title = 'Collider [[DEBUG : Development Mode=' + str(development_mode) + ' || Version=' + str(version) + ' || FPS=' + str(debug_fps) + ' || Build=' + str(debug_build) + ']]'
    window.title = str(title)


app = Ursina()

window.exit_button.visible = True
window.fps_counter.enabled = True
window.fps_counter.color = color.black
window.cursor = True
window.vsync = True
window.windowed_position = None
window.borderless = False
window.fullscreen = False
window.color = color.white
version = 'ALPHA'
development_mode = True
debug_build = 0.1
title = 'Collider [[DEBUG : Development Mode=' + str(development_mode) + ' || Version=' + str(version) + '|| FPS=' + str(0) + ' || Build=' + str(debug_build) + ']]'
window.title = str(title)
window.debug = True


package_folder = Path(__file__).parent
models_folder = 'assets/models/' 
prefabs_folder = 'assets/prefabs/' 
scenes_folder = 'assets/scenes/' 
scripts_folder = 'assets/scripts/' 
textures_folder = 'assets/textures/' 
fonts_folder = 'assets/fonts/'
compressed_textures_folder = 'assets/textures/compressed/'
compressed_models_folder = 'assets/models/compressed/'

random_generator = random.Random()
texoffset = 0.0
texoffset2 = 0.0

entities = []

cubes = []
cube = Entity(model='cube', color=color.rgb(255, 255, 255), scale=(2, 2, 2), texture='crate_high', collider='box')
entities.append(cube)
cubes.append(cube)

vehicle = Entity(model='quad', color=color.rgb(0, 0, 0), scale=(2, 2, 2), collider='quad', position=Vec3(0, 5, 0), rotation=Vec3(90, 0, 0))

player = first_person_controller.FirstPersonController()

ground = Entity(model='plane', scale=32, texture='grass', texture_scale=(32, 32), collider='box', position=Vec3(10, 0, 10))
entities.append(ground)

sky = Sky(scale=100, collider='sky_dome')

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text='')
info.x = -0.5
info.y = 0.4
info.background = False
info.color = color.red
info.visible = True
info.visible = False

app.run()