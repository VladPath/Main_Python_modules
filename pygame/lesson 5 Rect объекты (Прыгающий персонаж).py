import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((W,H))
pg.display.set_caption('Rect объекты')
pg.display.set_icon(pg.image.load('images/img1.jpg'))

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60
clock = pg.time.Clock()

"""rect1 = pg.Rect((0,0,30,30))
rect2 = pg.Rect((30,30,30,30))

rect2.move_ip(20,20)
print(rect2)
rect3 = rect2.union(rect1)
print(rect3)

hero = pg.Surface((40,50))
hero.fill(BLUE)
"""

ground = H - 70
jump_force = 15
move = jump_force+1


hero = pg.Surface((50,50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=W//2)
rect.bottom = ground

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and ground == rect.bottom:
                move = -jump_force
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move +=1
        else:
            
            rect.bottom = ground
            move = jump_force + 1
    sc.fill(WHITE)
    sc.blit(hero,rect)
    pg.display.update()

    clock.tick(FPS)