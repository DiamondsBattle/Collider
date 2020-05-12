from ursina import *

class LoadingMenu(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loading_icon = Text(text='', texture='loading')
        self.loading_icon.enabled = False

    def change_menu_visibility(self):
        self.enabled = not self.loading_icon.enabled
        self.loading_icon.enabled = not self.loading_icon.enabled