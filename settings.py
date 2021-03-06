from ursina import *

window.show_ursina_splash = False
window.cursor = True
window.vsync = True
window.windowed_position = None
window.borderless = False
window.fullscreen = False
Texture.default_filtering = None
version = 'ALPHA'
development_mode = True
debug_build = 0.1
title = 'Collider [[DEBUG : Development Mode=' + str(development_mode) + ' || Version=' + str(version) + '|| FPS=' + str(0) + ' || Build=' + str(debug_build) + ']]'
window.title = str(title)
window.debug = True
application.package_folder = Path(__file__).parent
application.models_folder = application.asset_folder / 'models/'
application.prefabs_folder = application.asset_folder / 'prefabs/'
application.scenes_folder = application.asset_folder / 'scenes/'
application.scripts_folder = application.asset_folder / 'scripts/'
application.textures_folder = application.asset_folder / 'textures/'
application.fonts_folder = application.asset_folder / 'fonts/'
application.compressed_textures_folder = application.textures_folder / 'compressed/'
application.compressed_models_folder = application.models_folder / 'compressed/'
Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text='')
info.x = -0.5
info.y = 0.4
info.background = False
info.color = color.red
info.visible = True
info.visible = False