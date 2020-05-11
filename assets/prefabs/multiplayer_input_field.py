from ursina import *

class MultiplayerInputField(Button):

    def __init__(self, default_value='', label='', **kwargs):
        super().__init__(
            scale=(.5, .1),
            highlight_scale=1,
            pressed_scale=1,
            collider='box',
            )
        for key, value in kwargs.items():
            if 'scale' in key:
                setattr(self, key, value)

        self.default_value = default_value
        self.text_field = TextField(world_parent=self, x=-.45, y=.3, z=-.1, max_lines=2)
        self.text_field.scale *= 2
        self.text_field.text = default_value
        self.text_field.render()
        self.origin = (0, 0)
        self.text_field.register_mouse_input = False
        self.active = False

        if label:
            self.label = Text('IP Address')
            self.text_field.x += 5

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'left mouse down' and not self.active:
            self.active = self.hovered

    @property
    def text(self):
        return self.text_field.text

    @text.setter
    def text(self, value):
        self.text_field.text = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
        self.text_field.ignore = not value
        self.text_field.cursor.enabled = value
        # if value == True:
        #     # self.text_field.select_all()
        #     # self.text_field.register_mouse_input = True
        #     invoke(self.text_field.select_all, delay=.1)
        #     # self.text_field.input(' ')
        #     # self.text_field.erase()
