from ursina import *
from assets.prefabs.multiplayer_input_field import MultiplayerInputField as MIF

app = Ursina()

def input(key):
    if key == "escape":
        change_menu_all_visibility(conf=True)

def update():
    pass

app.run()
