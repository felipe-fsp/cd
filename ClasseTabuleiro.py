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
        
    def limpar_tela(self):
        self.Matriz_Jogo = [[0,0,0],[0,0,0],[0,0,0]]
      
        if self.Game_var == 0:
            self.botão_main.grid_forget()
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
        self.b_1.configure(text = self.jogador())
        self.b_1.configure(state = "disabled")        
    
    
    def desenhar_tabuleiro(self):
        self.b_1 = tk.Button(self.window,height =8, width =20)
        self.b_1.configure(command=self.bo_1)
        self.b_1.grid(row=0, column=0,pady=5)

        self.b_2 = tk.Button(self.window,height =8, width =20)
        self.b_2.configure(command=lambda: self.b_2.configure(text = self.jogador()))
        self.b_2.grid(row=1, column=0,padx=5)
        
        self.b_3 = tk.Button(self.window,height =8, width =20)
        self.b_3.configure(command=lambda: self.b_3.configure(text = self.jogador()))
        self.b_3.grid(row=2, column=0)
      
        self.b_4 = tk.Button(self.window,height =8, width =20)
        self.b_4.configure(command=lambda: self.b_4.configure(text = self.jogador()))
        self.b_4.grid(row=0, column=1)

        self.b_5 = tk.Button(self.window,height =8, width =20)
        self.b_5.configure(command=lambda: self.b_5.configure(text = self.jogador()))
        self.b_5.grid(row=1, column=1)
        
        self.b_6 = tk.Button(self.window,height =8, width =20)
        self.b_6.configure(command=lambda: self.b_6.configure(text = self.jogador()))
        self.b_6.grid(row=2, column=1)
        
        self.b_7 = tk.Button(self.window,height =8, width =20)
        self.b_7.configure(command=lambda: self.b_7.configure(text = self.jogador()))
        self.b_7.grid(row=0, column=2)

        self.b_8 = tk.Button(self.window,height =8, width =20)
        self.b_8.configure(command=lambda: self.b_8.configure(text = self.jogador()))
        self.b_8.grid(row=1, column=2, padx =5)
        
        self.b_9 = tk.Button(self.window,height =8, width =20)
        self.b_9.configure(command=lambda: self.b_9.configure(text = self.jogador()))
        self.b_9.grid(row=2, column=2,pady=5)
        
        self.Prox_Jogada = tk.Label(self.window, font=('Helvetica', 10))
        self.Prox_Jogada.configure(textvariable=self.jogador_nome_var)        
        self.Prox_Jogada.grid(row=3, column=0, columnspan=1, sticky="nsew", pady=15) 
        
    def jogador(self):
        if self.jogador_id == 0:
            self.jogador_id += 1
            self.jogador_nome = "Superman"
            self.jogador_nome_var.set("É a vez do " + self.jogador_nome)            
            self.jogador_nome = "Bambam"
            return self.jogador_nome
        elif self.jogador_id == 1:
            self.jogador_id -= 1
            self.jogador_nome = "Bambam"
            self.jogador_nome_var.set("É a vez do " + self.jogador_nome)            
            self.jogador_nome = "Superman"
            return self.jogador_nome
            
    
        
          
    def loop(self):
        self.window.mainloop()
          
main = Tabuleiro()
main.loop()
