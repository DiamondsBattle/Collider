from ursina import *

class SecondaryMenu(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enabled = False
        self.btn_play = Button(text='Play')
        self.btn_play.enabled = False
        self.btn_settings = Button(text='Settings')
        self.btn_settings.enabled = False
        self.btn_goto_menu = Button(text='Return to the Menu')
        self.btn_goto_menu.enabled = False

    def changeMenuVisibility(self):
        self.enabled = not self.enabled
        self.btn_play.enabled = not btn_play.enabled
        self.btn_settings.enabled = not btn_settings.enabled
        self.btn_play.enabled = not btn_play.enabled