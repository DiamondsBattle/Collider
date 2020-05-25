from ursina import *
from ursina.prefabs.radial_menu import RadialMenu, RadialMenuButton

app = Ursina()


rm = RadialMenu(
    buttons=(
        RadialMenuButton(text='Talk'),
        RadialMenuButton(text='Send friend request'),
        RadialMenuButton(text='See profile'),
        RadialMenuButton(text='Pay'),
        RadialMenuButton(text='Report', color=color.red),
        ),
    enabled=False
    )

def enable_radial_menu():
    rm.enabled = True


EditorCamera()


app.run()