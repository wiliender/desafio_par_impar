import random
from tkinter import *
from constantes import *
from calculo_par_impar import *
import tkinter.messagebox as mbox
import win32gui, win32con

try:
    ocultar_janela = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(ocultar_janela, win32con.SW_HIDE)

except:
    pass


raiz = Tk()

class Janela:
    """Construtor da Janela do jogo"""
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()

        self.fr_result = Frame(raiz, bg=cinza1)
        self.fr_result.pack()

        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()

        self.fr3 = Frame(raiz, bg=cinza1)
        self.fr3.pack()

        self.fr4 = Frame(raiz, bg=cinza1)
        self.fr4.pack()

        self.fr5 = Frame(raiz, bg=cinza1)
        self.fr5.pack()

        self.fr5 = Frame(raiz, bg=cinza1)
        self.fr5.pack()

        self.fr6 = Frame(raiz, bg=cinza1)
        self.fr6.pack()
        #instanciando as imagens antes de executar pois e um programa simples
        self.img_player = PhotoImage(file="imagens/ninja.png")
        self.img_pc = PhotoImage(file="imagens/robo.png")
        self.img0 = PhotoImage(file="imagens/numero_0.png")
        self.img1 = PhotoImage(file="imagens/numero_1.png")
        self.img2 = PhotoImage(file="imagens/numero_2.png")
        self.img3 = PhotoImage(file="imagens/numero_3.png")
        self.img4 = PhotoImage(file="imagens/numero_4.png")
        self.img5 = PhotoImage(file="imagens/numero_5.png")
        self.img6 = PhotoImage(file="imagens/numero_6.png")
        self.img7 = PhotoImage(file="imagens/numero_7.png")
        self.img8 = PhotoImage(file="imagens/numero_8.png")
        self.img9 = PhotoImage(file="imagens/numero_9.png")
        self.img10 = PhotoImage(file="imagens/numero_10.png")

        self.lb1 = Label(self.fr1, text="Batalha Shinobi", bg=cinza1, font=fonte1, fg=azul2, pady=10, padx=35)
        self.lb1.pack(side=LEFT)

        self.botao_restart = Button(self.fr1, text="Restart", font=fonte4, relief=RAISED, command=self.resetar)
        self.botao_restart.bind("<Return>", self.resetar2)
        self.botao_restart.pack(side=LEFT)

        self.lb_result = Label(self.fr_result, text= "", bg=cinza1, font= fonte1, fg= "green")
        self.lb_result.pack()

        self.placar1 = 0
        self.placar2 = 0
        self.lb2 = Label(self.fr2, text="        Jogador     "+ str(self.placar1) +"      x      " + str(self.placar2)+"      Computador", bg=cinza1, font=fonte2, fg=azul2, pady=10)
        self.lb2.pack()

        self.lb_img1 = Label(self.fr3, image=self.img_player, bg=cinza1)
        self.lb_img1.pack(side=LEFT)#posicionando a imagem a esquerda para que não fique uma em cima da outra

        self.lb_espaco = Label(self.fr3, text="             ",bg=cinza1)
        self.lb_espaco.pack(side=LEFT)

        self.lb_img2 = Label(self.fr3, image=self.img_pc, bg=cinza1)
        self.lb_img2.pack(side=LEFT)

        self.escolha = StringVar() #recebe o valor da escolha, nome da classe primeira letra maiuscula

        self.rb_par = Radiobutton(self.fr4, text="Par", value="par", variable=self.escolha, bg=cinza1, fg=azul2,
                                  font=fonte2, pady=20)#variavel escolha vai receber o valor
        self.rb_par.pack(side=LEFT)

        self.rb_impar = Radiobutton(self.fr4, text="Ímpar", value="impar", variable=self.escolha, bg=cinza1, fg=azul2,
                                  font=fonte2, pady=20)  #variavel escolha vai receber o valor
        self.rb_impar.pack(side=LEFT)

        self.lb3 = Label(self.fr5, text="Número de 0 a 10: ", bg=cinza1, fg=azul2, font=fonte3, width=15, pady=20)
        self.lb3.pack(side=LEFT)

        self.num = Entry(self.fr5, width=2, font=fonte3)
        self.num.pack(side=LEFT)

        self.bt_jogar = Button(self.fr6, text="Jogar", font=fonte1, bg=cinza2, relief=RAISED, border=8, command=self.jogar)
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack()

        self.lb_erro = Label(self.fr6, text="", font=fonte4, bg=cinza1, fg="red")
        self.lb_erro.pack()

    def jogar(self):

        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_comp = random.randrange(0,11)#pega até o penultimo

            #print(escolha)
            #print(num_comp)

            if escolha == "par" or escolha == "impar":
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ""
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ""
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ""
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ""
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ""
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ""
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ""
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ""
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ""
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ""
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ""
                    #imagem comp
                    if num_comp == 0:
                        self.lb_img2['image'] = self.img0
                    elif num_comp == 1:
                        self.lb_img2['image'] = self.img1
                    elif num_comp == 2:
                        self.lb_img2['image'] = self.img2
                    elif num_comp == 3:
                        self.lb_img2['image'] = self.img3
                    elif num_comp == 4:
                        self.lb_img2['image'] = self.img4
                    elif num_comp == 5:
                        self.lb_img2['image'] = self.img5
                    elif num_comp == 6:
                        self.lb_img2['image'] = self.img6
                    elif num_comp == 7:
                        self.lb_img2['image'] = self.img7
                    elif num_comp == 8:
                        self.lb_img2['image'] = self.img8
                    elif num_comp == 9:
                        self.lb_img2['image'] = self.img9
                    elif num_comp == 10:
                        self.lb_img2['image'] = self.img10


                    par_impar = calcular_par_impar(num, num_comp)
                    ##print(num_comp)
                    if par_impar == "par":
                        self.lb_result['text'] = "Deu par"
                    elif par_impar == "impar":
                        self.lb_result['text'] = "Deu ímpar"

                    if par_impar == "par" and escolha == "par":
                        self.placar1 += 1
                        self.lb2['text'] = "        Jogador     "+ str(self.placar1) +"      x      " +\
                                           str(  self.placar2)+"      Computador"
                    elif par_impar == "impar" and escolha == "impar":
                        self.placar1 += 1
                        self.lb2['text'] = "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"
                    elif par_impar == "par" and escolha == "impar":
                        self.placar2 += 1
                        self.lb2['text'] = "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"
                    elif par_impar == "impar" and escolha == "par":
                        self.placar2 += 1
                        self.lb2['text'] = "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"

                else:
                    self.lb_erro['text'] = "Erro escolha par ou imar e um valor de 0 a 10"
            else:
                self.lb_erro['text'] = "Erro escolha par ou imar e um valor de 0 a 10"

        except:
            self.lb_erro['text'] = "Erro escolha par ou imar e um valor de 0 a 10"

    def jogar2(self, event):

        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_comp = random.randrange(0,11)#pega até o penultimo

            #print(escolha)
            #print(num_comp)

            if escolha == "par" or escolha == "impar":
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ""
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ""
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ""
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ""
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ""
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ""
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ""
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ""
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ""
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ""
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ""
                    #imagem comp
                    if num_comp == 0:
                        self.lb_img2['image'] = self.img0
                    elif num_comp == 1:
                        self.lb_img2['image'] = self.img1
                    elif num_comp == 2:
                        self.lb_img2['image'] = self.img2
                    elif num_comp == 3:
                        self.lb_img2['image'] = self.img3
                    elif num_comp == 4:
                        self.lb_img2['image'] = self.img4
                    elif num_comp == 5:
                        self.lb_img2['image'] = self.img5
                    elif num_comp == 6:
                        self.lb_img2['image'] = self.img6
                    elif num_comp == 7:
                        self.lb_img2['image'] = self.img7
                    elif num_comp == 8:
                        self.lb_img2['image'] = self.img8
                    elif num_comp == 9:
                        self.lb_img2['image'] = self.img9
                    elif num_comp == 10:
                        self.lb_img2['image'] = self.img10


                    par_impar = calcular_par_impar(num, num_comp)
                    ##print(num_comp)
                    if par_impar == "par":
                        self.lb_result['text'] = "Deu par"
                    elif par_impar == "impar":
                        self.lb_result['text'] = "Deu ímpar"

                    if par_impar == "par" and escolha == "par":
                        self.placar1 += 1
                        self.lb2['text'] = "        Jogador     "+ str(self.placar1) +"      x      " +\
                                           str(  self.placar2)+"      Computador"
                    elif par_impar == "impar" and escolha == "impar":
                        self.placar1 += 1
                        self.lb2['text'] = "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"
                    elif par_impar == "par" and escolha == "impar":
                        self.placar2 += 1
                        self.lb2['text'] = "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"
                    elif par_impar == "impar" and escolha == "par":
                        self.placar2 += 1
                        self.lb2['text'] = "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"

                else:
                    self.lb_erro['text'] = "Erro escolha par ou imar e um valor de 0 a 10"
            else:
                self.lb_erro['text'] = "Erro escolha par ou imar e um valor de 0 a 10"

        except:
            self.lb_erro['text'] = "Erro escolha par ou imar e um valor de 0 a 10"

    def resetar(self):
        resposta = mbox.askquestion("Restart", "Deseja reiniciar!?")
        if resposta == "yes":
            self.lb_result["text"] = ""
            self.lb_img1["image"] = self.img_player
            self.lb_img2["image"] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2["text"]= "        Jogador     " + str(self.placar1) + "      x      " +\
                                           str(self.placar2) + "      Computador"
            self.lb_erro["text"] = ""
    def resetar2(self,event):
        resposta = mbox.askquestion("Restart", "Deseja reiniciar!?")
        if resposta == "yes":
            self.lb_result["text"] = ""
            self.lb_img1["image"] = self.img_player
            self.lb_img2["image"] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2["text"] = "        Jogador     " + str(self.placar1) + "      x      " + \
                               str(self.placar2) + "      Computador"
            self.lb_erro["text"] = ""


raiz.geometry("840x650+300+30") #tamanho da janela e posicao
raiz.iconbitmap("imagens/ninjaa.ico")
raiz.title("Shinobi Par ou Impar")
raiz["bg"] = cinza1

janela = Janela(raiz)

raiz.mainloop()
