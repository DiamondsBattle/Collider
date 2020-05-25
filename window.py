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
from assets.scripts.define_objects import defineObjects
from assets.prefabs.player import Player
from assets.prefabs.health_bar import HealthBar
from assets.prefabs.interaction_menu import InteractionMenu, InteractionMenuButton


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
        shoot_test()
        print("Shooted !")
    if key == "a":
        interaction_menu.enabled = not interaction_menu.enabled
        # player.controller = None


def load_textures():
    global loaded_textures, player, interaction_menu
    if not loaded_textures:
        if main_menu.has_changed_loading_menu_visibility:
            main_menu.enabled = False
            main_menu.loading_menu.enabled = False
            secondary_menu.enabled = False
            defineObjects()
            loaded_textures = True
            player = Player(model='player',
                            hp=1000,
                            loadout='minigun',
                            money=23181231)
            money_counter = MC(position=(.6, -.45, 0),
                               money=player.getMoney())
            health_bar = HealthBar(position=(-.52, -.4, 0),
                                   max_value=player.getHp())
            interaction_menu = InteractionMenu(
                                buttons=(
                                    InteractionMenuButton(text='Talk'),
                                    InteractionMenuButton(text='Friend'),
                                    InteractionMenuButton(text='Profile'),
                                    InteractionMenuButton(text='Pay'),
                                    InteractionMenuButton(text='Report', color=color.red),
                                    )
                                )
            interaction_menu.enabled = False


def update():
    # if key == "escape":
    #     if MM.enabled is False and LM.enabled is False:
    #         SM.changeMenuVisibility(self)
    # main_menu.txt_multi_connect_response.text = connect()
    load_textures()


loaded_textures = False
main_menu = MM(model='quad', texture='background', scale=(15, 8.5))
secondary_menu = SM(model='quad', scale=(15, 8.5))
player = None
interaction_menu = None

app.run()
