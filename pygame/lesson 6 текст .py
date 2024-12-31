import pygame as pg

pg.init()

W,H = 600,400

sc = pg.display.set_mode((W,H))
pg.display.set_caption('Обработка текста')
pg.display.set_icon(pg.image.load('images/img1.jpg'))

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60
clock = pg.time.Clock()

f_sys = pg.font.SysFont('arialunicode', 14)
# f_sys = pg.font.Font(None, 25) По умолчанию
sc_text = f_sys.render('Hello world', 1, RED, (121,23,222))
pos = sc_text.get_rect(center=(W//2,H//2))


def draw_text():
    sc.fill(WHITE)
    sc.blit(sc_text,pos)
    pg.display.update()

draw_text()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pg.mouse.get_rel()
    if pg.mouse.get_focused() and pos.collidepoint(pg.mouse.get_pos()):
        btns = pg.mouse.get_pressed()
        if btns[0]:
            rel = pg.mouse.get_rel()
            pos.move_ip(rel)
            draw_text()

    
    clock.tick(FPS)