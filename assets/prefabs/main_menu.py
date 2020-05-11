from ursina import *
from assets.prefabs.multiplayer_input_field import MultiplayerInputField as MIF
from assets.prefabs.load_textures import LoadTextures
from assets.prefabs.player import Player

class MainMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_solo = Button(text='Solo', background=True, on_click=self.play_solo, color=color.black, collider='box', origin=(.95, -.6), scale=(.5, .15))
        self.btn_multi = Button(text='Multiplayer', background=True, on_click=self.play_multi, color=color.black, collider='box', origin=(.95, .6), scale=(.5, .15))
        self.btn_quit = Button(text='Quit', background=True, on_click=application.quit, color=color.black, highlight_color=color.red, collider='box', origin=(.95, 1.8), scale=(.5, .15))
        self.input_multi_address = MIF()
        self.input_multi_address.enabled = False

    def play_solo(self):
        self.change_menu_visibility(conf=True)
        LoadTextures()

    def play_multi(self):
        self.change_multi_visibility(conf=True)

    def change_menu_visibility(self, conf):
        if conf:
            self.btn_solo.enabled = not self.btn_solo.enabled
            self.btn_multi.enabled = not self.btn_multi.enabled
            self.btn_quit.enabled = not self.btn_quit.enabled
            self.enabled = not self.enabled

    def change_multi_visibility(self, conf):
        if conf:
            self.input_multi_address.enabled = not self.input_multi_address.enabled
            self.btn_solo.enabled = not self.btn_solo.enabled
            self.btn_multi.enabled = not self.btn_multio.enabled
            self.btn_quit.enabled = not self.btn_quit.enabled