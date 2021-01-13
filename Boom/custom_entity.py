from ursina import *

class CustomEntity(Entity):

    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)
        self.message = message

    def interact(self):
        if mouse.hovered_entity == self:
            if distance(self, b):
                print(self.message)