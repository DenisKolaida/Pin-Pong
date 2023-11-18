import pygame as pg
import sys, time

pg.init()

W, H = 700, 700
FPS = 60

win = pg.display.set_mode((W, H))
pg.display.set_caption('Пинг-понг')
clock = pg.time.Clock()

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
    clock.tick(FPS)