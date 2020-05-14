from ursina import *                    # Import the ursina engine
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    pass

def update():
    for i in astres:
        i.rotation_y += time.dt * 100    # Rotate every time update is called


app = Ursina()                         # Initialise your Ursina app

window.title = 'Solar System simplistic simulation'              # The window title
window.exit_button.visible = True      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True      # Show the FPS (Frames per second) counter
window.cursor = True
window.vsync = True
window.windowed_position = None
window.borderless = False
window.fullscreen = True
window.color = color.rgb(7, 1, 51)

camera.position = Vec3(0, 0, -200)

astres = []    # Create the list

sun = Entity(model='sphere', color=color.yellow, scale=(10, 10, 10))
astres.append(sun)                                  # Add the planet to the list

mercure = Entity(parent=sun, model='sphere', color=color.black, scale=(0.02, 0.02, 0.02), position=Vec3(1, 0, 0))
astres.append(mercure)

venus = Entity(parent=sun, model='sphere', color=color.brown, scale=(0.03, 0.03, 0.03), position=Vec3(2, 0, 0))
astres.append(venus)

earth = Entity(parent=sun, model='sphere', color=color.blue, scale=(0.05, 0.05, 0.05), position=Vec3(3, 0, 0))
astres.append(earth)

mars = Entity(parent=sun, model='sphere', color=color.red, scale=(0.045, 0.045, 0.045), position=Vec3(4, 0, 0))
astres.append(mars)

saturne = Entity(parent=sun, model='sphere', color=color.rgb(255, 199, 1), scale=(0.2, 0.2, 0.2), position=Vec3(5, 0, 0))
astres.append(saturne)

jupiter = Entity(parent=sun, model='sphere', color=color.rgb(255, 199, 1), scale=(0.3, 0.3, 0.3), position=Vec3(6, 0, 0))
astres.append(jupiter)

uranus = Entity(parent=sun, model='sphere', color=color.blue, scale=(0.15, 0.15, 0.15), position=Vec3(7, 0, 0))
astres.append(uranus)

neptune = Entity(parent=sun, model='sphere', color=color.rgb(19, 800, 791), scale=(0.151, 0.151, 0.151), position=Vec3(8, 0, 0))
astres.append(neptune)

player = FirstPersonController()
camera.position = Vec3(0, 0, -200)

app.run()                               # Run the app