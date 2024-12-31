import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((W,H))
pg.display.set_caption('Обработка событий клавиатуры')
pg.display.set_icon(pg.image.load('images/img1.jpg'))

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60
clock = pg.time.Clock()

x = W//2
y = H//2

speed = 5

move = 0

flLeft = flRight = False

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and event.mod == pg.KMOD_LSHIFT:
                move = -speed
            elif event.key == pg.K_RIGHT and event.mod == pg.KMOD_LSHIFT:
                move = speed
        elif event.type == pg.KEYUP:
            if event.key in [pg.K_LEFT, pg.K_RIGHT]:
                move = 0
    x += move
    
   
    """
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT]:
        x -= speed
    elif keys[pg.K_RIGHT]:
        x += speed
    """
        
    sc.fill(WHITE)
    pg.draw.rect(sc,GREEN,(x,y,10,10))
    pg.display.update()
    clock.tick(FPS)