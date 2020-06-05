from ursina import *
#  from PhysiX.car_speed import acceleration
from os import system

app = Ursina()

def acceleration(a0, s0, x0, t):
    a = a0
    s = a0 * t + s0
    x = 1 / 2 * a0 * sqrt(t) + s0 * t + x0
    return a, s, x

def update():
    global speed, time
    if held_keys['d']:
        os.system('cls')
        time += 1
        print('time = {}'.format(time))
        h = acceleration(a0=.1, s0=speed, x0=car.x, t=time)
        car.x = h[2]
        print('h = {}'.format(h))
        speed = h[1]
        print('speed = {}'.format(speed))
        print('Current speed : {} kmp/h'.format(speed))
    if held_keys['q']:
        car.x -= .1
        print('q')


time, speed = 0, 0
car = Entity(model='quad', scale=.1, scale_x=.15, color=color.red)

app.run()