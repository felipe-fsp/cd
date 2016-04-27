import numpy as np
import random

class jogo():
  def __init__(self):
      self.jogadores = ["X","O"," "] #Representa as duas letras tradicionais do Jogo da Velha
      self.vencedor = "*"
      self.sorteio()
      self.jogador = self.jogadores
      self.tabuleiro = np.zeros([3,3]) #Matriz do jogo
      self.GX = 0
      self.GO = 0
  
  
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
    produtocoluna = np.prod(self.matriz, 0)
    produtolinha = np.prod(self.matriz, 1)
    if (produtocoluna[0] %2 == 0 and produtocoluna[0]>0)
    or (produtocoluna[1] %2 == 0 and produtocoluna[1]>0)
    or (produtocoluna[2] %2 == 0 and produtocoluna[2]>0)
    or (produtolinha[0] %2 == 0 and produtolinha[0]>0)
    or (produtolinha[1] %2 == 0 and produtolinha[1]>0)
    or (produtolinha[2] %2 == 0 and produtolinha[2]>0)
    or (((self.tabuleiro[0][0] * self.tabuleiro[1][1] * self.tabuleiro[2][2]) > 0) and ((self.tabuleiro[0][0] * self.tabuleiro[1][1] * self.tabuleiro[2][2])%2==0))
    or (((self.tabuleiro[2][0] * self.tabuleiro[1][1] * self.tabuleiro[0][2]) > 0) and ((self.tabuleiro[2][0] * self.tabuleiro[1][1] * self.tabuleiro[0][2])%2==0)): 
      self.vencedor="O"
      self.jogador=self.jogadores[2]
      self.GO+=1
      print("Jogador O chegou a %d vitórias" % self.GO)
      return 2
    
    
    if (produtocoluna[0] %2 == 1 and produtocoluna[0]>0)
    or (produtocoluna[1] %2 == 1 and produtocoluna[1]>0)
    or (produtocoluna[2] %2 == 1 and produtocoluna[2]>0)
    or (produtolinha[0] %2 == 1 and produtolinha[0]>0)
    or (produtolinha[1] %2 == 1 and produtolinha[1]>0)
    or (produtolinha[2] %2 == 1 and produtolinha[2]>0)
    or (((self.tabuleiro[0][0] * self.tabuleiro[1][1] * self.tabuleiro[2][2]) > 0) and ((self.tabuleiro[0][0] * self.tabuleiro[1][1] * self.tabuleiro[2][2])%2==1))
    or (((self.tabuleiro[2][0] * self.tabuleiro[1][1] * self.tabuleiro[0][2]) > 0) and ((self.tabuleiro[2][0] * self.tabuleiro[1][1] * self.tabuleiro[0][2])%2==1)): 
      self.vencedor="X"
      self.jogador=self.jogadores[2]
      self.GX+=1
      print("Jogador X chegou a %d vitórias" % self.GX)
      return 1
      
    elif np.sum(self.tabuleiro) == 14 or np.sum(self.tabuleiro) == 13:
      print()
      self.vencedor = "Empate - Deu velha!"
      self.jogador = self.jogadores[2]
      return 0
    else:
      return -1
      
  
  
  def limpa_jogadas(self):
    self.matriz = np.zeros([3,3])
    self.sorteio()
    self.ganhador = "*"



