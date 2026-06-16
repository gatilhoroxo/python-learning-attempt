import pygame as pg
import sys

pg.init()

WINDOW_SIZE = 300
GRID_SIZE = 100
LINE_WIDTH = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)

screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pg.display.set_caption('Tic Tac Toe')

game_board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'


# --- NOVAS FUNÇÕES ADICIONADAS ---

def draw_lines():
    """Desenha as linhas da grade do tabuleiro."""
    # Linhas horizontais
    pg.draw.line(screen, LINE_COLOR, (0, GRID_SIZE), (WINDOW_SIZE, GRID_SIZE), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, GRID_SIZE * 2), (WINDOW_SIZE, GRID_SIZE * 2), LINE_WIDTH)
    # Linhas verticais
    pg.draw.line(screen, LINE_COLOR, (GRID_SIZE, 0), (GRID_SIZE, WINDOW_SIZE), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (GRID_SIZE * 2, 0), (GRID_SIZE * 2, WINDOW_SIZE), LINE_WIDTH)

def draw_figures():
    """Desenha os X e Os no tabuleiro baseado na matriz game_board."""
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == 'X':
                # Desenha duas linhas diagonais para formar o X
                pos_x = col * GRID_SIZE
                pos_y = row * GRID_SIZE
                pg.draw.line(screen, BLACK, (pos_x + 20, pos_y + 20), (pos_x + 80, pos_y + 80), LINE_WIDTH + 2)
                pg.draw.line(screen, BLACK, (pos_x + 80, pos_y + 20), (pos_x + 20, pos_y + 80), LINE_WIDTH + 2)
            elif game_board[row][col] == 'O':
                # Desenha um círculo para formar o O
                center_x = col * GRID_SIZE + GRID_SIZE // 2
                center_y = row * GRID_SIZE + GRID_SIZE // 2
                pg.draw.circle(screen, BLACK, (center_x, center_y), 35, LINE_WIDTH + 2)

def check_winner():
    """Verifica se há um vencedor ou se o jogo empatou."""
    # Verifica linhas e colunas
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != ' ':
            return game_board[i][0]
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != ' ':
            return game_board[0][i]
            
    # Verifica diagonais
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != ' ':
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != ' ':
        return game_board[0][2]
        
    # Verifica se deu velha (empate)
    if all(cell != ' ' for row in game_board for cell in row):
        return 'Empate'
        
    return None

# --- LOOP PRINCIPAL DO JOGO ---
running = True

while running:
    screen.fill(WHITE)  # Limpa a tela com fundo branco
    draw_lines()        # Desenha a grade
    draw_figures()      # Desenha as jogadas

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            # Pega as coordenadas X e Y de onde o mouse foi clicado
            mouse_x, mouse_y = event.pos
            
            # Converte as coordenadas de pixels para índices da matriz (0, 1 ou 2)
            clicked_row = mouse_y // GRID_SIZE
            clicked_col = mouse_x // GRID_SIZE

            # Se o quadrado clicado estiver vazio, realiza a jogada
            if game_board[clicked_row][clicked_col] == ' ':
                game_board[clicked_row][clicked_col] = current_player
                
                # Verifica se a jogada atual encerrou a partida
                winner = check_winner()
                if winner:
                    print(f"Fim de jogo! Resultado: {winner}")
                    # Reinicia o tabuleiro para uma nova partida após alguém ganhar
                    game_board = [[' ' for _ in range(3)] for _ in range(3)]
                
                # Alterna o turno entre 'X' e 'O'
                current_player = 'O' if current_player == 'X' else 'X'

    pg.display.update()  # Atualiza a janela gráfica
