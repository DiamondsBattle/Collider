from ursina import *
from assets.prefabs.multiplayer_input_field import MultiplayerInputField as MIF


class MainMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_solo = Button(text='Solo', background=True, on_click=self.play_solo, color=color.black, collider='box', origin=(.95, -.6), scale=(.5, .15))
        self.btn_multi = Button(text='Multiplayer', background=True, on_click=self.play_multi, color=color.black, collider='box', origin=(.95, .6), scale=(.5, .15))
        self.btn_quit = Button(text='Quit', background=True, on_click=application.quit, color=color.black, highlight_color=color.red, collider='box', origin=(.95, 1.8), scale=(.5, .15))
        self.input_multi_address = MIF()
        self.input_multi_address.enabled = False

    def play_solo(self):
        pass

    def play_multi(self):
        change_menu_type(conf=True)

    def change_menu_visibility_type(self, conf):
        if conf:
            menu.btn_solo.enabled = not menu.btn_solo.enabled
            menu.btn_multi.enabled = not menu.btn_multi.enabled
            menu.btn_quit.enabled = not menu.btn_quit.enabled
            menu.input_multi_address.enabled = not menu.input_multi_address.enabled