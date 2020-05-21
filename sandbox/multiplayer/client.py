import socket
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as FPS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET : IPv6 and SOCK_STREAM : TCP
s.connect((socket.gethostname(), 8888))

data = s.recv(1024)
print(data.decode('utf-8'))

app = Ursina()

ground = Entity(color=color.red, scale=32)
player_controller = FPS()
sky = Sky()

app.run()