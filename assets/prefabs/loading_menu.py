from ursina import *
from time import sleep

class LoadingMenu(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.loading_icon = Text(text='', texture='loading')
        # self.loading_icon.enabled = False

    def changeMenuVisibility(self):
        self.enabled = not self.enabled
        # self.loading_icon.enabled = not self.loading_icon.enabled