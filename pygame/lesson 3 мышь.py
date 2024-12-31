import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((W,H))
pg.display.set_caption('Обработка событий мыши')
pg.display.set_icon(pg.image.load('images/img1.jpg'))

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60
clock = pg.time.Clock()

sp = None

sc.fill(WHITE)
pg.display.update()

pg.mouse.set_visible(False)


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    
    pos = pg.mouse.get_pos()
    sc.fill(WHITE)

    if pg.mouse.get_focused():
        pg.draw.circle(sc,BLUE,pos,5)
    
    
    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos
        
        x,y = min(pos[0],sp[0]),min(pos[1],sp[1])
        
        width = max(pos[0],sp[0]) - x
        heith = max(pos[1],sp[1]) - y

        sc.fill(WHITE)
        pg.draw.rect(sc,GREEN,(x,y,width, heith))
    else:
        sp = None
    pg.display.update()
    
        
        
     
            
            
    """
elif event.type == pg.MOUSEBUTTONDOWN:
    print(f'Нажата кнопка: {event.button}')
elif event.type == pg.MOUSEMOTION:
    print(f"позиция мыши: {event.pos}")
    """
        
        
    clock.tick(FPS)