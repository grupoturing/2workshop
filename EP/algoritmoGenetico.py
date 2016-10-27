##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2016         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este codigo livremente                 ##
##                                                              ##
##################################################################

import pygame
import random

class Individuo():

        #O individuo eh o tomador de acoes,
        #Ele eh composto por:
        #       -pesos (uma lista que de fato define o individuo)
        #       -score (pontuacao associada a sua performance)
        #Possui as funcoes:
        #       -fitness
        #       -calcular_saidas
                
        def __init__(self, pesos):
                #nao precisa mexer aqui
                #quando Individuo for chamado, ele deve receber uma lista de pesos como entrada

                self.pesos = pesos
                self.score = 0

        def __str__(self):
                #nao precisa mexer aqui
                #retorna o print do individuo facil de ler
                s = "   Pesos:"
                for i in range(len(self.pesos)):
                        s+= "%5.2f "%(self.pesos[i])
                return s


# -------------------------------------------------------------------
        def fitness(self,gameState):

                #OBJETIVO: Implementar a funcao fitness que avalia o desempenho de um individuo e atualiza self.score

                        #dica: essa funcao recebe como entrada uma variavel com as informacoes de quando o jogo acaba
                                #gameState[0] = player.y (normalizado de -1 a +1)
                                #gameState[1] = ball.x   (normalizado de -1 a +1)
                                #gameState[2] = ball.y   (normalizado de -1 a +1)
                                #gameState[3] = ball.speed_x
                                #gameState[4] = ball.speed_y
                                #gameState[5] = numBat (numero de vezes que a bolinha bateu no player)
                                #gameState[6] = ganhou (True/False, se o player sobreviveu o tempo definido)


                #COMPLETE AQUI:

                        #self.score = ??

                pass
# -------------------------------------------------------------------

# -------------------------------------------------------------------
        def calcular_saida(self, entrada):

                # OBJETIVO: Implementar a decisao a partir dos pesos (self.pesos) e das entradas (entrada).
                
                        # Aqui se faz a decisao entre subir ou descer com o cursor do jogador.
                        # O vetor entrada possui 5 elementos: player.y, ball.x, ball.y, ball.speed_x, ball.speed_y
                                #teoricamente, voce nem precisa saber o que tem em cada posicao
                        
                        #Utilizando esses parametros de entrada combinando com os pesos atribuidos a cada um deles, deve-se retornar Direcao

                        #dica: Essa funcao deve retornar -1 (sobe), 0(parado) ou +1(desce)
                        #dica: As listas "self.pesos" e "entradas" tem que ter o mesmo tamanho
                        #dica: Nao  pra voce tentar resolver manualmente qual decisao ele deve tomar para cada caso.
                                #A inteligencia artificial que descobrira a melhor estrategia sozinha


                #COMPLETE AQUI:

                #return Direcao (-1, 0 ou 1)         
                
                pass



#################################################################################################


class Geracao:
        #A Geracao eh onde ocorre toda a evolucao,
        #Ele e composto por:
        #       -individuos (uma lista obletos da classe Individuo)
        #Possui as funcoes:
        #       -selecao
        #       -reproduzir
        #       -genCrossOver
        #       -genMut


# -------------------------------------------------------------------
        def __init__ (self, numInd):

                #OBJETIVO: gerar a geracao inicial
                        
                        #o objeto Geracao deve ter um atributo "individuos" sendo uma lista de individuos
                        
                        #para isso crie uma lista de individuos com (numInd) individuos,
                        #cada um com uma distribuicao randomica de pesos que contenha 5 pesos.
                        #dica: a funcao random.random() retorna um float entre 0 e 1
                        #dica: os pesos podem ser negativos
                        #dica: eh importante ter variedade!


                #COMPLETE AQUI:

                #self.individuos = individuos

                pass

# -------------------------------------------------------------------

        def __str__(self):
                #nao precisa mexer aqui
                #retorna o print do individuo facil de ler
                for i in range(len(self.individuos)):
                        print("Individuo %d:"%i)
                        print(self.individuos[i])
                return ''
                

# -------------------------------------------------------------------
        def selecao(self, numSelec):

                #OBJETIVO: criar a funcao de selecao
                        #Para isso, deve-se reduzir a lista de individuos para os (numSelec) melhores individuos.
                        #dica: essa funcao nao retorna nada
                        #dica: o python permite mudar o tamanho das listas, nao precisa criar uma nova
                        #dica: essa funcao nao precisa retornar nada, a geracao e alterada globalmente
                
                        
                #COMPLETE AQUI:
                
                pass
# -------------------------------------------------------------------

# -------------------------------------------------------------------
        def reproduzir(self, m, chanceCO, chanceMut):
                        
                #OBJETIVO:
                        #Aumentar o numero de individuos para (m) individuos
                        #e aplicar o crossing over e a mutacao nos novos individuos
                        #Use os individuos anteriores para criar os proximos
                        #Existem diversas maneiras de fazer isso

                        #dica: voce pode chamar as funcoes genCrossOver e genMut (faca elas primeiro)
                        #dica: Cuidado! Se voce fizer individuoA = individuoB,
                                #o python passara por referencia e toda mudanca que voce fizer em individuoA, ocorrera no individuoB (e vice-versa).
                                #O mesmo vale para listas
                                #o jeito correto de fazer isso e: individuoA = individuoB(individuoA.pesos[:])
                                #(Nao necessariamente voce vai precisar usar isso, foi so um aviso previo que faz muita gente erra por motivos de python)
                        #dica: essa funcao nao precisa retornar nada, a geracao e alterada globalmente
                

                #COMPLETE AQUI:
                

                pass
# -------------------------------------------------------------------

# -------------------------------------------------------------------
        def genCrossOver(self, individuo1, individuo2, chanceCO=0.5):


        #OBJETIVO: #Aplicar o crossing over com "chanceCO" de chance de trocar cada peso
                #para isso, voce deve receber 2 objetos do tipo individuo
                #lembrem-se que os valores trocados devem ter o mesmo loco!
                #"Gene de cabelo nao troca com gene de olho"
                #dica: a funcao random.random() retorna um float entre 0 e 1
                #dica: essa funcao nao precisa retornar nada, o individuo1 e o individuo2 serao alterados globalmente

                #COMPLETE AQUI:
                

                pass
# -------------------------------------------------------------------

# -------------------------------------------------------------------
        def genMut(self, individuo1, chanceMut=0.15):

                #OBJETIVO: #Aplicar mutacao com "chanceMut" de chance em cada pesos do "individuo1"
                        #Existem diversas maneiras de fazer isso
                        #dica: a funcao random.random() retorna um float entre 0 e 1
                        #dica: essa funcao nao precisa retornar nada, o individuo1 sera alterado globalmente
                
                #COMPLETE AQUI:    

                pass
# -------------------------------------------------------------------



