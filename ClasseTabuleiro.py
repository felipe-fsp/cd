# -*- coding: utf-8 -*-

import tkinter as tk
import ClasseJogo

class Tabuleiro:
    
    def __init__(self):

        self.Main_Game = ClasseJogo.Jogo()
        self.window = tk.Tk()               
        self.window.resizable(height = False, width=False)        
        self.window.title("Tic Tac Toe")
        self.window.geometry("650x650")
        for linhas in range (0,5):
           self.window.rowconfigure(linhas, weight=1)
        for colunas in range (0,3):        
           self.window.columnconfigure(colunas, weight=1)
        self.Game_var = 0
        self.Jogador_1_vic = 0        
        self.Jogador_2_vic = 0
        self.jogador_id = 0
        self.jogador_nome_var = tk.StringVar()
        self.jogador_nome_1 = tk.StringVar()
        self.jogador_nome_2 = tk.StringVar()
        self.label_principal_show = tk.StringVar()
        self.label_principal = ""
        self.jogador_nome = ""
        self.jogador_nome_temp_1 = ""         
        self.jogador_nome_temp_2 = ""
        self.Text_Main = tk.Label(self.window,text="Jogo da Velha", font = "Britannic 30")
        self.Text_Main.configure( bg = "blue", fg = "white")        
        self.Text_Main.grid(row=0, column=0, columnspan=3, rowspan = 3 ,sticky="nsew")         
        self.Button_Main = tk.Button(self.window,text="Iniciar Jogo")
        self.Button_Main.configure(command=self.escolha_jogadores)
        self.Button_Main.grid(row=3, column=0, columnspan =3, rowspan = 2, sticky = "nsew")
        
    def escolha_jogadores(self):
        self.Button_Main.grid_forget()        
        self.Text_Main.grid_forget()
        
        self.Label_nome_1 = tk.Label(self.window,text="Escolha o nome para o jogador X", font = "Helvetica", fg = "white", bg = "blue")        
        self.Label_nome_1.grid(row=0, column=0, columnspan =3, rowspan = 1, sticky = "nsew")       
        
        self.Textbox_1 = tk.Entry(self.window)
        self.Textbox_1.configure(textvariable=self.jogador_nome_1,font = "Helvetica 20")
        self.Textbox_1.grid(row=1, column=0, columnspan = 3, rowspan = 1, sticky="nsew")     
        
        self.Label_nome_2 = tk.Label(self.window,text="Escolha o nome para o jogador O", font = "Helvetica", fg = "white", bg = "blue")        
        self.Label_nome_2.grid(row=2, column=0, columnspan =3, sticky = "nsew")

        self.Textbox_2 = tk.Entry(self.window)
        self.Textbox_2.configure(textvariable=self.jogador_nome_2, font = "Helvetica 20")
        self.Textbox_2.grid(row=3, column=0, columnspan = 3, rowspan = 1, sticky="nsew")            

        self.Button_Main = tk.Button(self.window,text="Iniciar a partida")        
        self.Button_Main.configure(command = self.enter)      
        self.Button_Main.grid(row=4, column=0, columnspan = 3, rowspan = 1, sticky = "nsew")     
     
     def enter(self):       
        self.jogador_nome_temp_1 = self.jogador_nome_1.get()
        self.jogador_nome_temp_2 = self.jogador_nome_2.get()
        self.jogador_nome = self.jogador_nome_temp_1      
        self.jogador_nome_var.set("É a vez do " + self.jogador_nome)        
        self.limpar_tela()
        
    def limpar_tela(self):
      
        if self.Game_var == 0:
            self.Button_Main.grid_forget()
            self.Label_nome_1.grid_forget()
            self.Label_nome_2.grid_forget()
            self.Textbox_1.grid_forget()
            self.Textbox_2.grid_forget()
            self.label_principal = ""
            self.label_principal_show.set("Jogo da Velha")
            self.Main_Game.limpa_jogadas()            
            self.desenhar_tabuleiro()
        
        elif self.Game_var >= 1:        
            self.b_1.grid_forget()
            self.b_2.grid_forget()
            self.b_3.grid_forget()
            self.b_4.grid_forget()
            self.b_5.grid_forget()
            self.b_6.grid_forget()
            self.b_7.grid_forget()
            self.b_8.grid_forget()
            self.b_9.grid_forget()
            self.Prox_Jogada.grid_forget()   
            self.desenhar_tabuleiro()
            
    def bo_1(self):
        self.Main_Game.recebe_jogada(0,0)
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_1.configure(text = 'X')
            self.b_1.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_1.configure(text = 'O')
            self.b_1.configure(state = 'disabled', bg = "orange red")
        self.vitoria()
        
    def bo_2(self): 
        self.Main_Game.recebe_jogada(0,1)  
        self.jogador()
        if self.Main_Game.jogador == 1:
            self.b_2.configure(text = 'X')
            self.b_2.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_2.configure(text = 'O')
            self.b_2.configure(state = 'disabled', bg = "orange red")
        self.vitoria() 
    def bo_3(self):
        self.Main_Game.recebe_jogada(0,2)
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_3.configure(text = 'X')
            self.b_3.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_3.configure(text = 'O')
            self.b_3.configure(state = 'disabled', bg = "orange red")
        self.vitoria() 
    def bo_4(self):
        self.Main_Game.recebe_jogada(1,0)
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_4.configure(text = 'X')
            self.b_4.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_4.configure(text = 'O')
            self.b_4.configure(state = 'disabled', bg = "orange red")
        self.vitoria() 
    def bo_5(self):
        self.Main_Game.recebe_jogada(1,1)
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_5.configure(text = 'X')
            self.b_5.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_5.configure(text = 'O')
            self.b_5.configure(state = 'disabled', bg = "orange red")
        self.vitoria()    
    def bo_6(self):
        self.Main_Game.recebe_jogada(1,2)        
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_6.configure(text = 'X')
            self.b_6.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_6.configure(text = 'O')
            self.b_6.configure(state = 'disabled', bg = "orange red")
        self.vitoria()
        
    def bo_7(self):
        self.Main_Game.recebe_jogada(2,0)        
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_7.configure(text = 'X')
            self.b_7.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_7.configure(text = 'O')
            self.b_7.configure(state = 'disabled', bg = "orange red")
        self.vitoria()
    def bo_8(self):
        self.Main_Game.recebe_jogada(2,1)        
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_8.configure(text = 'X')
            self.b_8.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_8.configure(text = 'O')
            self.b_8.configure(state = 'disabled', bg = "orange red")
        self.vitoria()
    def bo_9(self):
        self.Main_Game.recebe_jogada(2,2)        
        self.jogador()        
        if self.Main_Game.jogador == 1:
            self.b_9.configure(text = 'X')
            self.b_9.configure(state = 'disabled', bg = "turquoise1")
        else:
            self.b_9.configure(text = 'O')
            self.b_9.configure(state = 'disabled', bg = "orange red")
        self.vitoria()              
    
    
    def desenhar_tabuleiro(self):
        self.b_1 = tk.Button(self.window, height = 6, width = 40)
        self.b_1.configure(command=self.bo_1)
        self.b_1.grid(row=0, column=0, sticky = "ns")

        self.b_2 = tk.Button(self.window, height = 6, width = 40)
        self.b_2.configure(command=self.bo_2)
        self.b_2.grid(row=0, column=1, sticky = "ns")
        
        self.b_3 = tk.Button(self.window, height = 6, width = 40)
        self.b_3.configure(command=self.bo_3)
        self.b_3.grid(row=0, column=2, sticky = "ns")
      
        self.b_4 = tk.Button(self.window, height = 6, width = 40)
        self.b_4.configure(command=self.bo_4)
        self.b_4.grid(row=1, column=0, sticky = "ns")

        self.b_5 = tk.Button(self.window, height = 6, width = 40)
        self.b_5.configure(command=self.bo_5)
        self.b_5.grid(row=1, column=1, sticky = "ns")
        
        self.b_6 = tk.Button(self.window, height = 6, width = 40)
        self.b_6.configure(command=self.bo_6)
        self.b_6.grid(row=1, column=2, sticky = "ns")
        
        self.b_7 = tk.Button(self.window, height = 6, width = 40)
        self.b_7.configure(command=self.bo_7)        
        self.b_7.grid(row=2, column=0, sticky = "ns")
        
        self.b_8 = tk.Button(self.window, height = 6, width = 40)
        self.b_8.configure(command=self.bo_8)
        self.b_8.grid(row=2, column=1, sticky = "ns")
        
        self.b_9 = tk.Button(self.window, height = 6, width = 40)
        self.b_9.configure(command=self.bo_9)
        self.b_9.grid(row=2, column=2, sticky = "ns")
        
        self.Prox_Jogada = tk.Label(self.window, font=('Helvetica', 10))
        self.Prox_Jogada.configure(textvariable=self.jogador_nome_var)        
        self.Prox_Jogada.grid(row=3, column=0, columnspan=1, rowspan = 1, sticky="nsew") 
        
        self.Restart_button = tk.Button(self.window)
        self.Restart_button.configure(command=self.limpar_tela, text = "Reiniciar Jogo")
        self.Restart_button.grid(row=3, column=2, columnspan=1, rowspan = 1, sticky="nsew")         
        
        self.Main_label = tk.Label(self.window, font=('Helvetica', 10))
        self.Main_label.configure(textvariable = self.label_principal_show , bg = "white", fg = "blue")        
        self.Main_label.grid(row=4, column=0, columnspan=3, rowspan = 1, sticky="nsew") 
    
        
    def jogador(self):
        if self.jogador_id == 0:
            self.jogador_id += 1
            self.jogador_nome = self.jogador_nome_temp_2
            self.jogador_nome_var.set("É a vez do " + self.jogador_nome)            
            self.jogador_nome = self.jogador_nome_temp_1
            return self.jogador_nome
        elif self.jogador_id == 1:
            self.jogador_id -= 1
            self.jogador_nome = self.jogador_nome_temp_1
            self.jogador_nome_var.set("É a vez do " + self.jogador_nome)            
            self.jogador_nome = self.jogador_nome_temp_2
            return self.jogador_nome
            
    
        
          
    def loop(self):
        self.window.mainloop()
          
main = Tabuleiro()
main.loop()
