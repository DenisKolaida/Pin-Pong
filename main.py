import pygame as pg
import sys, time

pg.init()

W, H = 700, 700
FPS = 60

win = pg.display.set_mode((W, H))
pg.display.set_caption('Пинг-понг')
clock = pg.time.Clock()

ball = pg.image.load('images/ball.png')
ballr = ball.get_rect(topleft = (350, 350))

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    win.fill((40, 230, 241))
    win.blit(ball, ballr)

    pg.display.update()
    clock.tick(FPS)