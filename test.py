from ursina import *
from assets.prefabs import first_person_controller

app = Ursina()

def update():
    print(camera.forward)


player = first_person_controller.FirstPersonController()
app.run()