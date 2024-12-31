import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((W,H))
pg.display.set_caption('Графические примитивы')
pg.display.set_icon(pg.image.load('images/img1.jpg'))

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
"""
# Четырухугольник
pg.draw.rect(sc, WHITE, (10,10,30,100),1)
# Линии прямые не сглаженная и сглаженная
pg.draw.line(sc,RED, (120,20),(200,40))
pg.draw.aaline(sc,GREEN,(120,40),(200,60), 2)

# кривые прямые соедененные не сглаженная и сглаженная
pg.draw.lines(sc, GREEN, True, ((120,60),(200,100),(120,100)))
pg.draw.aalines(sc, GREEN, True, ((220,60),(300,100),(220,100)))

pg.draw.polygon(sc,GREEN, ((10,150),(200,100),(400,290),(10,290)),1)
pg.draw.polygon(sc,GREEN, ((250,250),(280,250),(10,290),(10,320)),1)
"""
pg.draw.ellipse(sc,RED, (50,100,50,20),1)
pg.draw.circle(sc,GREEN,(200,100),25,1)

pi = 3.14
pg.draw.arc(sc,BLUE,(450,20,50,120),pi,2*pi)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()