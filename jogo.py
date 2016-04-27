import numpy as np
import random

class jogo():
  def __init__(self):
      self.jogadores = ["X","O"," "] #Representa as duas letras tradicionais do Jogo da Velha
      self.vencedor = "*"
      self.sorteio()
      self.jogador = self.jogadores
      self.tabuleiro = np.zeros([3,3]) #Matriz do jogo
      self.games_X = 0
      self.gamess_O = 0
      



