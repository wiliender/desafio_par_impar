from tkinter import *
from constantes import *
from calculo_par_impar import *

raiz = Tk()

class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()

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
        self.img_img0 = PhotoImage(file="imagens/numero_0.png")
        self.img_img1 = PhotoImage(file="imagens/numero_1.png")
        self.img_img2 = PhotoImage(file="imagens/numero_2.png")
        self.img_img3 = PhotoImage(file="imagens/numero_3.png")
        self.img_img4 = PhotoImage(file="imagens/numero_4.png")
        self.img_img5 = PhotoImage(file="imagens/numero_5.png")
        self.img_img6 = PhotoImage(file="imagens/numero_6.png")
        self.img_img7 = PhotoImage(file="imagens/numero_7.png")
        self.img_img8 = PhotoImage(file="imagens/numero_8.png")
        self.img_img9 = PhotoImage(file="imagens/numero_9.png")
        self.img_img10 = PhotoImage(file="imagens/numero_10.png")

        self.lb1 = Label(self.fr1, text= "Batalha Shinobi", bg=cinza1, font=fonte1, fg=azul2, pady=10)
        self.lb1.pack()

        self.lb_result = Label(self.fr1, text= "", bg=cinza1, font= fonte1, fg= "green")
        self.lb_result.pack()

        self.placar1 = 0
        self.placar2 = 0
        self.lb2 = Label(self.fr2, text= "        Jogador     "+ str(self.placar1) +"      x      " + str(self.placar2)+"      Computador", bg=cinza1, font=fonte2, fg=azul2, pady=10)
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

        self.rb_impar = Radiobutton(self.fr4, text="Impar", value="impar", variable=self.escolha, bg=cinza1, fg=azul2,
                                  font=fonte2, pady=20)  # variavel escolha vai receber o valor
        self.rb_impar.pack(side=LEFT)



raiz.geometry("840x650+300+30") #tamanho da janela e posicao
raiz.iconbitmap("imagens/ninjaa.ico")
raiz.title("Shinobi Par ou Impar")
raiz["bg"] = cinza1

janela = Janela(raiz)

raiz.mainloop()
