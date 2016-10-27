
##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2016         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este codigo livremente                 ##
##                                                              ##
##################################################################

import sys
import pygame
from pong import *
import algoritmoGenetico as ag 

# -------------- instanciacao dos individuos -------------
arq_ind1 = sys.argv[1]
arq_ind2 = sys.argv[2]

pesos_1 = map(float, open(arq_ind1).read().split())
pesos_2 = map(float, open(arq_ind2).read().split())

individuo_1 = ag.Individuo(pesos_1)
individuo_2 = ag.Individuo(pesos_2)
# --------------------------------------------------------


# --------------- instanciacao do jogo -------------------
size = [640, 480]
screen = pygame.display.set_mode((size[0], size[1]))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 60

player_1 = Player(size)
player_2 = Player(size)
player_2.x = size[0] - 16
ball = Ball(size)
# --------------------------------------------------------

screen.fill((0, 0, 0))
ball.draw(screen)
player_1.draw(screen)
player_2.draw(screen)


pygame.display.flip()


gameOver = False
# try:
while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise Exception("Game exited by user")
        
        # ----------------- Update INDIVIDUO 1 -----------------------
        entradas_1 = [2.0*(player_1.y + player_1.padHei/2)/size[1] -1,
        			  2.0*ball.x/size[0]-1, 2.0*ball.y/size[1]-1,
        			  ball.speed_x/3.0,
        			  ball.speed_y/3.0]
        direcao_1 = individuo_1.calcular_saida(entradas_1)
        player_1.movement(size,direcao_1)

        
        # ----------------- Update INDIVIDUO 2 -----------------------
        entradas_2 = [2.0*(player_2.y + player_2.padHei/2)/size[1] -1,
        			  -2.0*ball.x/size[0]+1, 2.0*ball.y/size[1]-1,
        			  -ball.speed_x/3.0,
        			  ball.speed_y/3.0]
        direcao_2 = individuo_2.calcular_saida(entradas_2)
        player_2.movement(size,direcao_2)

        # -------------------- Update BALL ----------------------------
        gameOver = not ball.movement(size, player_1, player_2)

        # ------ desenha na tela -------
        screen.fill((0, 0, 0))
        ball.draw(screen)
        player_1.draw(screen)
        player_2.draw(screen)


        pygame.display.flip()
        clock.tick(FPS)
# except Exception as e:
#         print(str(e))
