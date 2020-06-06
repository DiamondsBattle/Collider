from ursina import *

def interact(a, b):
    if distance(a, b) <= 5:
        print('Interacted with {0} ({1})'.format(b, distance(a, b)))