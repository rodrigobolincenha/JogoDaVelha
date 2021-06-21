import pygame, sys
import numpy as np
#*--------------------------------------- Grupo 7 ------------------*
#--------------------------- Rodrigo Alves Bolincenha -----------------*
#--------------------------- Gabriel Marchioro Klein -------------------*
#--------------------------- Guilherme Henrique Schneider Inkotte ---------------*
pygame.init()
# TAMANHO DAS FIGURAS
LARGURA = 600
ALTURA = 800
LINHA_LARGURA = 15
LINHAS_TABU = 3
COLUNAS_TABU = 3
CIRCULO_RADIUS = 60
CIRCULO_LARGURA = 15
CROSS_LARGURA = 25
ESPACO = 55

#cor
RED = (255, 0, 0)
BG_COR = (255, 255, 255)
LINHA_COR = (0, 0, 0)
CIRCULO_COR = (239, 0, 0)
CROSS_COR = (0, 0, 255)

# TELA
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tic Tac Toe")
screen.fill( BG_COR )
pontuacao = [0, 0]

# HUD
fonte_vez = pygame.font.SysFont('comicsans', 40)
fonte_placar = pygame.font.SysFont('comicsans', 52, True)

#BOARD
board = np.zeros( (LINHAS_TABU, COLUNAS_TABU))
#print(board)

def desenha_vez(jogador): # Mostra na tela de quem e a vez de jogar
    pygame.draw.rect(screen, [255,255,255], [0, 620, 300, 45])
    vez_de = 'O'
    if jogador == 2:
        vez_de = 'X'
    texto_vez = fonte_vez.render('A vez é do: ' + vez_de, True, [0, 0, 0])
    screen.blit(texto_vez, [20, 630])

def desenha_pontuacao(): # Desenha a pontuacao na teal
    pygame.draw.rect(screen, [255,255,255], [0, 670, 300, 45])
    texto_placar = fonte_placar.render(str(pontuacao[0]) + ' x ' + str(pontuacao[1]), True, [0, 0, 0])
    screen.blit(texto_placar, [20, 680])

def desenha_tabuleiro(): # Desenha as linhas_ na tela
    # Primeira LINHA_ Horizontal
    pygame.draw.line( screen, LINHA_COR, (0, 200), (600, 200), LINHA_LARGURA)
    # Segunda LINHA_ Horizontal
    pygame.draw.line( screen, LINHA_COR, (0, 400), (600, 400), LINHA_LARGURA)
    # Terceira LINHA_ Horizontal
    pygame.draw.line( screen, LINHA_COR, (0, 600), (600, 600), LINHA_LARGURA)

    # primeira LINHA_ vertical
    pygame.draw.line( screen, LINHA_COR, (200, 0), (200, 600), LINHA_LARGURA)
    # segunda LINHA_ vertical
    pygame.draw.line(screen, LINHA_COR, (400, 0), (400, 600), LINHA_LARGURA)
    texto_reset = fonte_vez.render('Pressione "1" para reiniciar o tabuleiro', True, [0, 0, 0])
    screen.blit(texto_reset, [20, 740])
    desenha_vez(2)
    desenha_pontuacao()

def desenha_figuras(): # Desenha o O e o X
    for linha in range(LINHAS_TABU):
        for coluna in range(COLUNAS_TABU):
            if board[linha][coluna] == 1:
                pygame.draw.circle( screen, CIRCULO_COR, (int( coluna* 200 + 100), int(linha*200 + 100)), CIRCULO_RADIUS, CIRCULO_LARGURA)
            elif board[linha][coluna] == 2:
                pygame.draw.line( screen, CROSS_COR, (coluna*200 + ESPACO, linha * 200 + 200 - ESPACO), (coluna * 200 + 200 - ESPACO, linha * 200 + ESPACO), CROSS_LARGURA )
                pygame.draw.line( screen, CROSS_COR, (coluna * 200 + ESPACO, linha *200 +ESPACO), (coluna * 200 + 200 - ESPACO, linha * 200 + 200 -ESPACO), CROSS_LARGURA)

def marca_quadrado(linha, coluna, jogador): # marca no tabuleiro

    board[linha][coluna] = jogador
    desenha_vez(jogador)

def quadrado_disponivel(linha, coluna):# se o quadrado estiver disponivel retorna TRUE
    if board[linha][coluna] == 0: # zero representa que o quadrado esta vazio
        return True
    else:
        return False

def tabulheiro_cheio(): # Essa fncao vai correr por todos os quadrados.
    for linha in range(LINHAS_TABU):
        for coluna in range(COLUNAS_TABU):
            if board[linha][coluna] == 0:
                return False
    return True

def vitoria(jogador): # COnfere qual jogador ganhou o jogo
    # Vai fazer um LOOP em todos os quadrados na vertical e na horizontal.
    # vitoria na vertical
    for coluna in range(COLUNAS_TABU):
        if board[0][coluna] == jogador and board[1][coluna] == jogador and board[2][coluna] == jogador:
            pontuacao[jogador - 1] = pontuacao[jogador - 1] + 1
            desenha_pontuacao()
            desenha_linha_vertical(coluna, jogador)
            return True
    # vitoria na horizontal
    for linha in range(LINHAS_TABU):
        if board[linha][0] == jogador and board[linha][1] == jogador and board[linha][2] == jogador:
            pontuacao[jogador - 1] = pontuacao[jogador - 1] + 1
            desenha_pontuacao()
            desenha_linha_horizontal(linha, jogador)
            return True
    # vitoria na primeira diagonal
    if board[2][0] == jogador and board[1][1] == jogador and board[0][2] == jogador:
        pontuacao[jogador - 1] = pontuacao[jogador - 1] + 1
        desenha_pontuacao()
        desenha_primeira_diagonal(jogador)
        return True
    # vitoria na segunda diagonal
    if board[0][0] == jogador and board[1][1] == jogador and board[2][2] == jogador:
        pontuacao[jogador - 1] = pontuacao[jogador - 1] + 1
        desenha_pontuacao()
        desenha_segunda_diagonal(jogador)
        return True
    return False


def desenha_linha_vertical(coluna, jogador):
    posX = coluna * 200 + 100
    if jogador == 1:
        color = CIRCULO_COR
    elif jogador == 2:
        color = CROSS_COR
    pygame.draw.line( screen, color, (posX ,15),(posX, 600 - 15), 15)

def desenha_linha_horizontal(linha, jogador):
    posY = linha * 200 + 100
    if jogador == 1:
        color = CIRCULO_COR
    elif jogador == 2:
        color = CROSS_COR
    pygame.draw.line( screen, color, (15, posY), (LARGURA -15, posY), 15)

def desenha_primeira_diagonal(jogador):
    if jogador == 1:
        color = CIRCULO_COR
    elif jogador == 2:
        color = CROSS_COR
    pygame.draw.line( screen, color, (15, 600 -15), (LARGURA - 15, 15), 15)

def desenha_segunda_diagonal(jogador):
    if jogador == 1:
        color = CIRCULO_COR
    elif jogador == 2:
        color = CROSS_COR
    pygame.draw.line( screen, color, (15, 15), (LARGURA - 15, 600 -15), 15)

def recomecar():
    screen.fill(BG_COR)
    desenha_tabuleiro()
    jogador = 1
    for linha in range(LINHAS_TABU):
        for coluna in range(COLUNAS_TABU):
            board[linha][coluna] = 0

desenha_tabuleiro()
jogador = 1
game_over = False
# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over: # Essa funcao ira executar quando clicar na tela
           #para vincular a borda do console ao painel da tela, precisamos acessar as coordenada X e Y.
           # Fazemos isso usando o event.pos

           mouseX = event.pos[0] # quando usamos o event.pos[0] pegamos as coordenadas do X
           mouseY = event.pos[1] # quando usamos o event.pos[1] pegamos as coordenadas do Y

           clicar_linha = int(mouseY // 200)
           clicar_colunauna = int(mouseX // 200)

           if quadrado_disponivel( clicar_linha, clicar_colunauna):
               if jogador == 1:
                   marca_quadrado( clicar_linha, clicar_colunauna, 1)
                   if vitoria(jogador):
                       game_over = True
                   jogador = 2
               elif jogador == 2:
                   marca_quadrado( clicar_linha, clicar_colunauna, 2)
                   if vitoria(jogador):
                    game_over = True
                   jogador = 1
               desenha_figuras()

        if event.type == pygame.KEYDOWN: # funcao que checa qual botao do teclado ira funcionar
           if event.key == pygame.K_1: # botao numero 1
               recomecar()
               game_over = False



    pygame.display.update()