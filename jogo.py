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
      self.games_O = 0
  
  
  def jogar(self):
    self.window.mainloop()
  def sorteio(self):
    b=random.uniform(0,20)
    if int(b)%2==0:
    	self.jogador=self.jogadores[0]
    else:
    	self.jogador=self.jogadores[1]
    
  def recebe_jogada(self,l,c):
  
  def verifica_ganhador(self):
  
  del limpa_jogadas(self):



