import pygame as pg

pg.init()

WINDOW_SIZE = 300

WHITE = (255,255,255)
BLACK = (0,0,0)


screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pg.display.set_caption("Janela Branca")

# TIC TAC TOE # tem algo errado
game_board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

GS = 100 # grid size 
LW = 5 # line width 
LC = BLACK # line color 

def draw_lines():
    # horizontais
    pg.draw.line(screen, LC, (0, GS), (WINDOW_SIZE, GS), LW) 
    pg.draw.line(screen, LC, (0, GS*2), (WINDOW_SIZE, GS*2), LW) 
    # verticais
    pg.draw.line(screen, LC, (GS, 0), (GS, WINDOW_SIZE), LW) 
    pg.draw.line(screen, LC, (GS*2,0), (GS*2, WINDOW_SIZE), LW) 

def draw_figures():
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == 'X':
                pos_x = col * GS
                pos_y = row * GS
                pg.draw.line(screen, BLACK, (pos_x + 20, pos_y + 20), (pos_x + 80, pos_y + 80), LW + 2)
                pg.draw.line(screen, BLACK, (pos_x + 80, pos_y + 20), (pos_x + 20, pos_y + 80), LW + 2)
            elif game_board[row][col] == 'O':
                center_x = col * GS + GS // 2 
                center_y = row * GS + GS // 2 
                pg.draw.circle(screen, BLACK, (center_x, center_y), 35, LW + 2)

def check_winner():
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != ' ':
            return game_board[i][0]
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != ' ':
            return game_board[0][i]
    
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != ' ':
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != ' ':
        return game_board[0][2]

    if all(cell != ' ' for row in game_board for cell in row):
        return 'Empate'
    
    return None 

def events_tic_tac_toe():
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            clicked_row = mouse_y // GS
            clicked_col = mouse_x // GS

            if game_board[clicked_row][clicked_col] == ' ':
                game_board[clicked_row][clicked_col] = current_player

                winner = check_winner()
                if winner:
                    print(f"Fim de jogo! Resultado: {winner}")
                    game_board = [[' ' for _ in range(3)] for _ in range(3)]

                current_player = 'O' if current_player == 'X' else 'X'

def tic_tac_toe():
    draw_lines()
    draw_figures()
    events_tic_tac_toe()

# --- LOOP do JOGO ---
running = True

while running:
    # faz as atualizações das mudanças da janela gráfica do último ciclo 
    pg.display.update()

    screen.fill(WHITE)

    tic_tac_toe()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

# fim

