# DONE : Add Ground
# DONE : Add Sky
# DONE : Add FirstPersonView
# DONE : Add Crate
# DONE : Add Crate Texture
# DONE : Add Menu
# TODO : Add Car
# TODO : Add Guns
# TODO : Add Shooting
# TODO : Add Texture Packs
# TODO : Add Pause
# TODO : Add loadouts and multiple hands
# TODO : Add Narrator
# TODO : Add Music Player
# TODO : Add SFX
# TODO : Add Game Saving
# TODO : Add Multi-Player

from ursina import *
from assets.prefabs.main_menu import MainMenu as MM
from assets.prefabs.secondary_menu import SecondaryMenu as SM
from assets.prefabs.loading_menu import LoadingMenu as LM
from assets.prefabs.multi import Connect


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
    if key == "escape":
        if MM.enabled is False and LM.enabled is False:
            SM.change_menu_visibility(self)
    main_menu.txt_multi_connect_response.text = Connect()


app = Ursina()

main_menu = MM(model='quad', texture='background', scale=(15, 8.5))
secondary_menu = SM(model='quad', scale=(15, 8.5))
loading_menu = LM(model='quad', texture='loading_textures_background', scale=(15, 8.5))

app.run()
