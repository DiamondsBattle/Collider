# DONE : Add Ground
# DONE : Add Sky
# DONE : Add FirstPersonView
# DONE : Add Crate
# DONE : Add Crate Texture
# DONE : Add Menu
# TODO : Add functionality to Crate
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
from assets.scripts.multi import connect
from assets.prefabs.money_counter import MoneyCounter as MC
from assets.scripts.define_objects import defineObjects
from Boom.player import Player
from assets.prefabs.health_bar import HealthBar
from assets.prefabs.interaction_menu import InteractionMenu
from settings import title
from Boom.first_person_controller import FirstPersonController as FPS
from keybinds import keybinds
from assets.scripts.interact import interact
from Boom.bullet import Bullet


app = Ursina()


def input(key):
    if key == keybinds['weapon_shoot']:
        shoot_test()
        print("Shooted !")
    if key == keybinds['interaction_menu']:
        interaction_menu.enabled = not interaction_menu.enabled
        # player.controller = None
    if key == keybinds['interaction_main']:
        interact(a=player, b=mouse.hovered_entity)
    if key == "left mouse":
        bullet = Bullet()


def load_textures():
    global loaded_textures, player, interaction_menu
    if not loaded_textures:
        if main_menu.has_changed_loading_menu_visibility:
            main_menu.enabled = False
            main_menu.loading_menu.enabled = False
            secondary_menu.enabled = False
            defineObjects()
            loaded_textures = True
            player = Player(hp=1000,
                            loadout=gun_sniper,
                            money=23181231)
            player_controller = FPS()
            # player_weapon.position = Vec3((player.x + 1), player.y, player.z)

            money_counter = MC(position=(.6, -.45, 0),
                               money=player.getMoney())
            health_bar = HealthBar(position=(-.52, -.4, 0),
                                   max_value=player.getHp())
            interaction_menu = InteractionMenu(
                buttons=(
                )
            )
            # for i in player.interactions_names:
            #     new = (InteractionMenuButton(text=i, action=player.interactions_actions[i]))
            # interaction_menu.enabled = False


def update():
    # if key == "escape":
    #     if MM.enabled is False and LM.enabled is False:
    #         SM.changeMenuVisibility(self)
    main_menu.txt_multi_connect_response.text = connect()
    load_textures()
    window.title = str(title)
    try:
        print(entity.name)
    except:
        pass


loaded_textures = False
main_menu = MM(model='quad', texture='background', scale=(15, 8.5))
secondary_menu = SM(model='quad', scale=(15, 8.5))

player = None
interaction_menu = None
crate = None
gun_sniper = None
gun_pistol = None
gun_smg = None
gun_assault_rifle = None
gun_minigun = None
city_lp = None

window.exit_button.visible = True
window.exit_button.ignore_input = True
window.fps_counter.enabled = True
window.fps_counter.color = color.black
window.color = color.white

app.run()