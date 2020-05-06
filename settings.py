
window.exit_button.visible = True
window.fps_counter.enabled = True
window.fps_counter.color = color.black
window.cursor = True
window.vsync = True
window.windowed_position = None
window.borderless = False
window.fullscreen = False
window.color = color.white
version = 'ALPHA'
development_mode = True
debug_build = 0.1
title = 'Collider [[DEBUG : Development Mode=' + str(development_mode) + ' || Version=' + str(version) + '|| FPS=' + str(0) + ' || Build=' + str(debug_build) + ']]'
window.title = str(title)
window.debug = True


package_folder = Path(__file__).parent
models_folder = 'assets/models/'
prefabs_folder = 'assets/prefabs/'
scenes_folder = 'assets/scenes/'
scripts_folder = 'assets/scripts/'
textures_folder = 'assets/textures/'
fonts_folder = 'assets/fonts/'
compressed_textures_folder = 'assets/textures/compressed/'
compressed_models_folder = 'assets/models/compressed/'
