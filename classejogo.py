class Jogo:
         
         def __init__(self):
             self.Matriz_Jogo = [[0,0,0],[0,0,0],[0,0,0]]
             
             self.jogador = 2
         
         def recebe_jogada(self,linha,coluna):
             self.Matriz_Jogo[linha][coluna] = self.jogador    
             if self.jogador == 1:
                 self.jogador = 2 #X
             else: 
        	        self.jogador = 1 #O

         def verifica_ganhador(self): #Retorna 0 em empate, 1 se X vencer, 2 se O vencer, -1 caso contrário.
  
             #------verificar ganhador------#
             self.victlinha1 = self.Matriz_Jogo[0][0] * self.Matriz_Jogo[0][1] * self.Matriz_Jogo[0][2] 
             self.victlinha2 = self.Matriz_Jogo[1][0] * self.Matriz_Jogo[1][1] * self.Matriz_Jogo[1][2] 
             self.victlinha3 = self.Matriz_Jogo[2][0] * self.Matriz_Jogo[2][1] * self.Matriz_Jogo[2][2] 
             self.victcoluna1 = self.Matriz_Jogo[0][0] * self.Matriz_Jogo[1][0] * self.Matriz_Jogo[2][0] 
             self.victcoluna2 = self.Matriz_Jogo[0][1] * self.Matriz_Jogo[1][1] * self.Matriz_Jogo[2][1] 
             self.victcoluna3 = self.Matriz_Jogo[0][2] * self.Matriz_Jogo[1][2] * self.Matriz_Jogo[2][2]
             self.victdiagonal = self.Matriz_Jogo[0][0] * self.Matriz_Jogo[1][1] * self.Matriz_Jogo[2][2]
             self.victdiagonal2 = self.Matriz_Jogo[0][2] * self.Matriz_Jogo[1][1] * self.Matriz_Jogo[2][0]
        
             if self.victcoluna1 == 1:
                 return 1
             elif self.victcoluna1 == 8:
                 return 2
             elif self.victcoluna2 == 1:
                 return 1
             elif self.victcoluna2 == 8:
                 return 2
             elif self.victcoluna3 == 1:
                 return 1
             elif self.victcoluna3 == 8:
                 return 2
             elif self.victlinha1 == 1:
                 return 1
             elif self.victlinha1 == 8:
                 return 2
             elif self.victlinha2 == 1:
                 return 1
             elif self.victlinha2 == 8:
                 return 2
             elif self.victlinha3 == 1:
                 return 1
             elif self.victlinha3 == 8:
                 return 2
             elif self.victdiagonal == 1:
                 return 1
             elif self.victdiagonal == 8:
                 return 2
             elif self.victdiagonal2 == 1:
                 return 1
             elif self.victdiagonal2 == 8:
                 return 2
             elif self.victlinha1 == 0 or self.victlinha2 == 0 or self.victlinha3 == 0 or self.victcoluna1 == 0 or self.victcoluna2 == 0 or self.victcoluna3 == 0:
                 return -1
             else:
                 return 0

         def limpa_jogadas(self):
             for i in range (0,3):
                 for j in range(0,3):
                     self.Matriz_Jogo[i][j] = 0
