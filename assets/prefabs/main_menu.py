from ursina import *
from assets.prefabs.multiplayer_input_field import MultiplayerInputField as MIF
from assets.prefabs.load_textures import LoadTextures
from assets.prefabs.player import Player
from assets.prefabs.multi import Connect

class MainMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_solo = Button(text='Solo', background=True, on_click=self.play_solo, color=color.black, collider='box', origin=(.95, -.6), scale=(.5, .15))
        self.btn_multi = Button(text='Multiplayer', background=True, on_click=self.play_multi, color=color.black, collider='box', origin=(.95, .6), scale=(.5, .15))
        self.btn_quit = Button(text='Quit', background=True, on_click=application.quit, color=color.black, highlight_color=color.red, collider='box', origin=(.95, 1.8), scale=(.5, .15))
        self.btn_back = Button(background=True, background_color=color.gray, on_click=self.change_multi_visibility, highlight_color=color.light_gray, collider='box', origin=(5.3, -3), texture='arrow_back', scale=(.15, .15))
        self.btn_back.enabled = False
        self.input_multi_address = MIF()
        self.input_multi_address.enabled = False
        self.btn_multi_connect = Button(text='Connect', background=True, on_click=Connect, color=color.black, highlight_color=color.rgb(7, 118, 10), collider='box', origin=(0, 1), scale=(.5, .15))
        self.btn_multi_connect.enabled = False

    def play_solo(self):
        self.change_menu_visibility()
        LoadTextures()

    def play_multi(self):
        self.change_multi_visibility()

    def change_menu_visibility(self):
        self.btn_solo.enabled = not self.btn_solo.enabled
        self.btn_multi.enabled = not self.btn_multi.enabled
        self.btn_quit.enabled = not self.btn_quit.enabled
        self.enabled = not self.enabled

    def change_multi_visibility(self):
        self.input_multi_address.enabled = not self.input_multi_address.enabled
        self.btn_solo.enabled = not self.btn_solo.enabled
        self.btn_multi.enabled = not self.btn_multi.enabled
        self.btn_quit.enabled = not self.btn_quit.enabled
        self.btn_back.enabled = not self.btn_back.enabled
        self.btn_multi_connect.enabled = not self.btn_multi_connect.enabled