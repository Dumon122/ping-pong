from pygame import *
from random import randint 

WIDTH = 600
HEIGHT = 500
FPS = 6

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping-pong')
background = transform.scale(image.load('christmas-wrapping.jpg'), (WIDTH, HEIGHT))
window.blit(background, (0, 0))
clock = time.Clock()

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    display.update()
    clock.tick(FPS)