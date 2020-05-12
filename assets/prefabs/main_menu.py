from ursina import *
from assets.prefabs.multiplayer_input_field import MultiplayerInputField as MIF
from assets.prefabs.load_textures import LoadTextures
from assets.prefabs.player import Player
from assets.prefabs.multi import Connect

class MainMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_solo = Button(text='Solo', background=True, on_click=self.playSolo, color=color.black, collider='box', origin=(.95, -.6), scale=(.5, .15))
        self.btn_multi = Button(text='Multiplayer', background=True, on_click=self.playMulti, color=color.black, collider='box', origin=(.95, .6), scale=(.5, .15))
        self.btn_quit = Button(text='Quit', background=True, on_click=self.callDestroyWindow, color=color.black, highlight_color=color.red, collider='box', origin=(.95, 1.8), scale=(.5, .15))
        self.btn_back = Button(background=True, background_color=color.gray, on_click=self.changeMultiVisibility, highlight_color=color.light_gray, collider='box', origin=(5.3, -3), texture='arrow_back', scale=(.15, .15))
        self.btn_back.enabled = False
        self.input_multi_address = MIF()
        self.input_multi_address.enabled = False
        self.btn_multi_connect = Button(text='Connect', background=True, on_click=Connect, color=color.black, highlight_color=color.rgb(7, 118, 10), collider='box', origin=(0, 1), scale=(.5, .15))
        self.btn_multi_connect.enabled = False
        self.txt_multi_connect_response = Text(text='ERROR', color=color.red, origin=(0, 2))
        self.txt_multi_connect_response.enabled = False

    def playSolo(self):
        self.changeMenuVisibility()
        LoadTextures()

    def playMulti(self):
        self.changeMultiVisibility()

    def changeMenuVisibility(self):
        self.btn_solo.enabled = not self.btn_solo.enabled
        self.btn_multi.enabled = not self.btn_multi.enabled
        self.btn_quit.enabled = not self.btn_quit.enabled
        self.enabled = not self.enabled

    def changeMultiVisibility(self):
        self.input_multi_address.enabled = not self.input_multi_address.enabled
        self.btn_solo.enabled = not self.btn_solo.enabled
        self.btn_multi.enabled = not self.btn_multi.enabled
        self.btn_quit.enabled = not self.btn_quit.enabled
        self.btn_back.enabled = not self.btn_back.enabled
        self.btn_multi_connect.enabled = not self.btn_multi_connect.enabled

    def callDestroyWindow(self):
        self.destroyWindow(conf=True)

    def destroyWindow(self, conf):
        if conf:
            application.quit()