import pygame as pg
import random as rd
import sys, time

pg.init()

W, H = 700, 700
FPS = 60

win = pg.display.set_mode((W, H))
pg.display.set_caption('Пинг-понг')
clock = pg.time.Clock()

ball = pg.image.load('images/ball.png')
ballr = ball.get_rect(topleft = (350, 350))

pl1 = pg.image.load('images/racket.png')
pl2 = pg.image.load('images/racket.png')
pl1r = pl1.get_rect(topleft = (20, H/2-68))
pl2r = pl2.get_rect(topleft = (641, H/2-68))

bXSpeed = rd.randint(0, 10)
bYSpeed = rd.randint(0, 10)

pl1Speed = 3
pl2Speed = 3

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    ballr.x += bXSpeed
    ballr.y += bYSpeed
    if ballr.x < 1 or ballr.x >= W-ballr.width:
        bXSpeed *= -1
    if ballr.colliderect(pl1r) or ballr.colliderect(pl2r):
        bXSpeed *= -1
    if ballr.y < 1 or ballr.y >= H-ballr.height:
        bYSpeed *= -1

    pl1r.y += pl1Speed
    pl2r.y += pl2Speed

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pl1Speed = -3
    if keys[pg.K_s]:
        pl1Speed = 3
    if keys[pg.K_UP]:
        pl2Speed = -3
    if keys[pg.K_DOWN]:
        pl2Speed = 3

    if pl1r.y < 3 or pl1r.y > 561:
        pl1Speed *= -1
    if pl2r.y < 3 or pl2r.y > 561:
        pl2Speed *= -1 

    win.fill((40, 230, 241))
    win.blit(ball, ballr)
    win.blit(pl1, pl1r)
    win.blit(pl2, pl2r)

    pg.display.update()
    clock.tick(FPS)