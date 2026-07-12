import pygame as pg

pg.init()

WINDOW_SIZE = 300

WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pg.display.set_caption("Janela Branca")

# --- LOOP do JOGO ---
running = True

while running:
    # faz as atualizações das mudanças da janela gráfica do último ciclo 
    pg.display.update()

    screen.fill(WHITE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

# fim

