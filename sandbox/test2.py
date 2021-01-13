from ursina import *
from keybinds import keybinds

app = Ursina()

class FPS(Entity):

    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 5

        self.i = 0
        self.update_interval = 30

        self.cursor = Entity(
            parent=camera.ui,
            model='sphere',
            color=color.white66,
            scale=.01
            )
        self.position = (0, 1, 1)
        camera.position = self.position
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = True
        self.mouse_sensitivity = Vec2(40, 40)
        self.target_smoothing = 100
        self.smoothing = self.target_smoothing

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]
        camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

        self.y += held_keys[keybinds['player_jump']]
        self.y -= held_keys[keybinds['player_sneak']]

        self.direction = Vec3(
            self.forward * (held_keys[keybinds['player_forward']] - held_keys[keybinds['player_backward']])
            + self.right * (held_keys[keybinds['player_right']] - held_keys[keybinds['player_left']])
            ).normalized()

        self.smoothing = lerp(self.smoothing, self.target_smoothing, 4*time.dt)
        camera.position = lerp(
            camera.position,
            self.position + (self.up*1.5),
            self.smoothing / 100)

        camera.rotation_y = self.rotation_y

        origin = self.world_position + self.up + (self.direction/2)
        middle_ray = raycast(origin, self.direction, ignore=[self, ], distance=1.0, debug=False)
        left_ray = raycast(origin, lerp(self.left, self.forward, .5), ignore=[self, ], distance=3.0, debug=False)
        right_ray = raycast(origin, lerp(self.right, self.forward, .5), ignore=[self, ], distance=3.0, debug=False)

        if left_ray.hit:
            self.smoothing = 2
            self.position -= lerp(self.left, self.forward, .5) * (1.399-left_ray.distance)

        elif right_ray.hit:
            self.smoothing = 2
            self.position -= lerp(self.right, self.forward, .5) * (1.399-right_ray.distance)

        if not middle_ray.hit:
            self.position += self.direction * self.speed * time.dt


def update():
    global player_in_car
    if player_in_car:
        player.position = car.position
    position = Text(text=player.position)
    position.text = 0
    if held_keys['interaction_main']:
        if distance(car, player) <= 5:
            player_in_car = True
            player.parent = car
            player.position = car.position


car = Entity(model='cube', scale=2, color=color.red, collider='cube')
ground = Entity(model='quad', scale=10, color=color.azure, rotation=Vec3(90, 0, 0), collider='cube')
player = FPS()

player_in_car = False

app.run()