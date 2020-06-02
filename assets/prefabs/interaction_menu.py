from ursina import *

class InteractionMenu(Entity):
    def __init__(self, buttons=list(), **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.buttons = buttons
        origin = Entity(parent=self)
        self.open_at_cursor = True
        self.open_duration = .25
        self.z = -99
        self.bg = color.gray

        offset = lerp(.5, 2, len(self.buttons) / 8)
        for i, b in enumerate(self.buttons):
            b.parent = origin
            b.y = offset
            origin.rotation_z = i / len(self.buttons) * 360
            b.world_parent = self
            b.rotation_z = 0
            if hasattr(b, 'text_entity') and b.text_entity:
                b.text_entity.world_scale /= .075

        destroy(origin)
        self.scale = .075

        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_enable(self):
        self.bg.enabled = True
        if self.open_at_cursor:
            self.position = mouse.position

        delay_step = self.open_duration / (len(self.children)-1)
        original_scales = [c.scale for c in self.children]
        for i, c in enumerate(self.children):
            if c is self.bg:
                continue

            c.scale = 0
            c.animate_scale(original_scales[i], duration=.2, delay=i*delay_step, curve=curve.out_bounce)

    def input(self, key):
        if key == 'left mouse down' and mouse.hovered_entity in [c for c in self.children if isinstance(c, Button)]:
            invoke(setattr, self, 'enabled', False, delay=.1)
        elif key == 'left mouse down' and mouse.hovered_entity == self.bg:
            invoke(setattr, self, 'enabled', False, delay=.1)

    def enable_interaction_menu(self):
        self.enabled = True


class InteractionMenuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(
            model='sphere',
            scale=1.3,
            highlight_scale=1.2,
            pressed_color=color.black10
            )

        for key, value in kwargs.items():
            setattr(self, key, value)
