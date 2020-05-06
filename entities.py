from ursina import *
from assets.prefabs import first_person_controller

app = Ursina()

entities = []

cubes = []
cube = Entity(model='cube', color=color.rgb(255, 255, 255), scale=(2, 2, 2), texture='crate_high', collider='box')
entities.append(cube)
cubes.append(cube)

vehicle = Entity(model='car_lp', color=color.rgb(0, 0, 0), scale=(2, 2, 2), collider='car_lp', position=Vec3(0, 5, 0), rotation=Vec3(90, 0, 0))

player = first_person_controller.FirstPersonController()

ground = Entity(model='plane', scale=32, texture='grass', texture_scale=(32, 32), collider='box', position=Vec3(10, 0, 10))
entities.append(ground)

sky = Sky(scale=100, collider='sky_dome')

city = Entity(model='city_lp', scale=10, collider='city_lp', position=(0, 0, 0), color=color.red)

app.run()