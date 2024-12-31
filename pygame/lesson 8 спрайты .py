from random import randint
import pygame as pg
from ball import Ball

pg.init()

W,H = 600,400

pg.time.set_timer(pg.USEREVENT, 2000)

sc = pg.display.set_mode((600, 400))
pg.display.set_caption("Спрайты")
pg.display.set_icon(pg.image.load("pygame/images/img1.jpg"))

clock = pg.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

speed = 1
bg_surf = pg.image.load("pygame/images/back1.jpg").convert()
bg_surf = pg.transform.scale(bg_surf, (bg_surf.get_width()-100, bg_surf.get_height()-180))

balls_list = ['ball_bear.png','ball_fox.png', 'ball_kitten.png' ]
balls_surf = [pg.image.load("pygame/images/"+path).convert_alpha() for path in balls_list]

balls_group = pg.sprite.Group()

def creat_balls(group):
    indx = randint(0,len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1,4)
    return Ball(x, speed, balls_surf[indx], group)
    

creat_balls(balls_group
            )
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.USEREVENT:
            creat_balls(balls_group)
            
    sc.blit(bg_surf, (0, 0))
    balls_group.draw(sc)
    balls_group.update(H)
    pg.display.update()
    
                
    
    clock.tick(FPS)