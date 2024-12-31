import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((600, 400))
pg.display.set_caption("Изображения")
# pg.display.set_icon(pg.image.load("app.bmp"))

clock = pg.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

print( pg.image.get_extended() )
car_surf = pg.image.load("images/car.bmp").convert()
car_surf.set_colorkey((255, 255, 255))
car_rect = car_surf.get_rect(center=(W//2, H//2))

finish_surf = pg.image.load("images/finish.png").convert_alpha()
bg_surf = pg.image.load("images/sand.jpg").convert()

bg_surf = pg.transform.scale(bg_surf, (bg_surf.get_width()//3, bg_surf.get_height()//3))

car_up = car_surf
car_down = pg.transform.flip(car_surf, 0, 1)
car_left = pg.transform.rotate(car_surf, 90)
car_right = pg.transform.rotate(car_surf, -90)

car = car_up
speed = 5
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    bt = pg.key.get_pressed()
    if bt[pg.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif bt[pg.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > W-car_rect.height:
            car_rect.x = W-car_rect.height
    elif bt[pg.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif bt[pg.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > H-car_rect.height:
            car_rect.y = H-car_rect.height

    sc.blit(bg_surf, (0, 0))
    sc.blit(finish_surf, (0, 0))
    sc.blit(car, car_rect)

    pg.display.update()
    
                
    
                
    
    clock.tick(FPS)