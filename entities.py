from ursina import *
from assets.prefabs import first_person_controller
from ursina.shaders import camera_grayscale_shader

app = Ursina()

cube = Entity(model='cube', color=color.rgb(255, 255, 255), scale=(2, 2, 2), texture='crate_high', collider='box', position=Vec3(0, 0, 10))
car_base = Entity(model='car_lp', color=color.rgb(0, 0, 0), scale=(0.01, 0.01, 0.01), collider='car_lp', position=Vec3(0, 5, 0), rotation=Vec3(90, 0, 0))
player = first_person_controller.FirstPersonController()
ground = Entity(model='plane', scale=32, texture='grass', texture_scale=(32, 32), collider='box', position=Vec3(0, 0, 0))
sky = Sky(scale=100, collider='sky_dome')
# city = Entity(model='city_lp', collider='city_lp', scale=Vec3(0.25, 0.25, 0.25), position=Vec3(0, 0, 0), color=color.gray)
gun = Entity(model='gun_lp', scale=1, collider='gun_lp', position=Vec3(0, 0, 0), color=color.light_gray, texture='gun_lp_occlusion')
# car_mustang = Entity(model='car_lp', scale=Vec3(1, 1, 1), collider='car_lp', position=Vec3(0, 10, 0), color=color.orange)
app.run()
