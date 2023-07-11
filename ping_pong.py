from pygame import *
from random import randint 

WIDTH = 600
HEIGHT = 500
FPS = 60

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping-pong')
background = transform.scale(image.load('christmas-wrapping.jpg'), (WIDTH, HEIGHT))
window.blit(background, (0, 0))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speed

racket1 = Player('tenis.png', 30, 200, 50, 150, 4)
racket2 = Player('tenis.png', 520, 200, 50, 150, 4)
ball = GameSprite('mach.png', 200, 200, 50, 50, 4)

speed_x = 3
speed_y = 3

font.init()
font2 = font.Font(None, 35)
lose1 = font2.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
            speed_y *= - 1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > WIDTH:
            finish = True
            window.blit(lose2, (200, 200))
        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)