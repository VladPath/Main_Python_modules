import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((W,H))
pg.display.set_caption('Обработка поверхностей')
pg.display.set_icon(pg.image.load('images/img1.jpg'))

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60
clock = pg.time.Clock()


surf = pg.Surface((W, 200))
bita = pg.Surface((50,10))

surf.fill(BLUE)
bita.fill(RED)

x,y = 0,0
bx,by = 0, 150

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    surf.fill(BLUE)
    surf.blit(bita,(bx,by))
    if bx < W:
        bx += 5
    else:
        bx = 0
    if y < H:
        y += 1
    else:
        y = 0
    sc.fill(WHITE)
    sc.blit(surf,(x,y))
    pg.display.update()
        
        
    clock.tick(FPS)