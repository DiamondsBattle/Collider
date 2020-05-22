# DONE : Add Ground
# DONE : Add Sky
# DONE : Add FirstPersonView
# DONE : Add Crate
# DONE : Add Crate Texture
# DONE : Add Menu
# TODO : Add Cars
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
from assets.scripts.shoot_bullet import shoot
from assets.scripts.multi import connect
from assets.prefabs.money_counter import MoneyCounter as MC
from assets.scripts.define_objects import defineTextures
from assets.prefabs.player import Player


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


app = Ursina()

def input(key):
    if key == "left mouse down":
        # shoot(facing='North', gun=)
        print("Shooted !")


def update():
    if key == "escape":
        if MM.enabled is False and LM.enabled is False:
            SM.changeMenuVisibility(self)
    main_menu.txt_multi_connect_response.text = connect()
    if hasLoadedTextures:
        player = Player(model='player',
                        hp=1000,
                        loadout='minigun',
                        money=23181231)
        money_counter = MC(position=(0, 0, 0), money=player.getMoney())


main_menu = MM(model='quad', texture='background', scale=(15, 8.5))
secondary_menu = SM(model='quad', scale=(15, 8.5))

app.run()
