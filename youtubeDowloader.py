from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Progressbar, Notebook
from pathlib import Path
from pytube import YouTube, Playlist
import os


class APP():
    def __init__(self):
        self.tela()
        self.ABAS_FRAMES()
        self.LABEL()
        self.imagem()
        self.ENTRADAS()
        self.BOTAO()
        self.LABEL()
        self.janela.mainloop()
    def tela(self):
        self.janela = Tk()
        self.largura = 500
        self.altura = 200
        self.janela.resizable(width=False, height=False)
        self.largura_screen = self.janela.winfo_screenwidth()
        self.altura_screen = self.janela.winfo_screenheight()
        self.posX = self.largura_screen/2 - self.largura/2
        self.posY = self.altura_screen/2 - self.altura/2
        self.janela.geometry("%dx%d+%d+%d" % (self.largura, self.altura,self.posX,self.posY))
        self.janela.title("Baixador de PlayList")
    def imagem(self):
        ################## IMAGEM #####################
        self.imagem_yt="youtube.png"
        self.logo = PhotoImage(file=self.imagem_yt)
        self.logo = self.logo.subsample(2,2)
        self.figura1 = Label(self.aba1,image=self.logo)
        self.figura1.place(x=10,y=10)
        self.figura2 = Label(self.aba2,image=self.logo)
        self.figura2.place(x=10,y=10)
        ###############################################
    def LABEL(self):
        ##############LINK YOUTUBE##############
        #ABA1 Playlist
        self.lbl_LINK1 = Label(self.aba1,text='Link Playlist:',bg='lightgray',font=('Arial Baltic', 10))
        self.lbl_LINK1.place(x=25,y=55)
        #ABA2 Vídeo único
        self.lbl_LINK2 = Label(self.aba2,text='Link Vídeo:',bg='lightgray',font=('Arial Baltic', 10))
        self.lbl_LINK2.place(x=25,y=55)
    def BOTAO(self):
        ##############BTN DIRETORIO##############
        #ABA1 Playlist
        self.btn_DIR1 = Button(self.aba1, text='Diretorio',font=('Arial Baltic',12,'italic'),bg='#DC143C', fg='white', activebackground='#FF1493', activeforeground='white',command=self.DIRETORIOP)
        self.btn_DIR1.place(x=360, y=12)
        #ABA2 Vídeo único
        self.btn_DIR2 = Button(self.aba2, text='Diretorio',font=('Arial Baltic',12,'italic'),bg='#DC143C', fg='white', activebackground='#FF1493', activeforeground='white',command=self.DIRETORIOV)
        self.btn_DIR2.place(x=360, y=12)
        ##############BTN Baixar##############
        #ABA1 Playlist
        self.btn_BAIXAR1 = Button(self.aba1, text='Baixar',font=('Arial Baltic',12,'italic'),bg='#DC143C', fg='white', activebackground='#FF1493', activeforeground='white')
        self.btn_BAIXAR1.place(x=360, y=50)
        #ABA2 Vídeo único
        self.btn_BAIXAR2 = Button(self.aba2, text='Baixar',font=('Arial Baltic',12,'italic'),bg='#DC143C', fg='white', activebackground='#FF1493', activeforeground='white')
        self.btn_BAIXAR2.place(x=360, y=50)
    def ENTRADAS(self):
        #Link PLAYLIST
        self.entry_LINK1 = Entry(self.aba1,font=('Arial Baltic',11,'italic'))
        self.entry_LINK1.place(x=115,y=53, relwidth=0.50)
        #Link VÍDEO ÚNICO
        self.entry_LINK1 = Entry(self.aba2,font=('Arial Baltic',11,'italic'))
        self.entry_LINK1.place(x=115,y=53, relwidth=0.50)
        #Escolha de pasta PLAYLIST
        self.pasta_entry1= Entry(self.aba1,font=('Arial Baltic',11,'italic'))
        self.pasta_entry1.place(x=115,y=13, relwidth=0.50)
        self.pasta_entry1.focus()
        #Escolha de pasta VÍDEO ÚNICO
        self.pasta_entry2= Entry(self.aba2,font=('Arial Baltic',11,'italic'))
        self.pasta_entry2.place(x=115,y=13, relwidth=0.50)
        self.pasta_entry2.focus()
    def DIRETORIOP(self):
        self.home = Path.home()
        self.DIR = filedialog.askdirectory(initialdir=self.home)
        self.DIR = self.DIR+str("/")
        self.pasta_entry1.insert(END, self.DIR)
    def DIRETORIOV(self):
        self.home = Path.home()
        self.DIR = filedialog.askdirectory(initialdir=self.home)
        self.DIR = self.DIR+str("/")
        self.pasta_entry2.insert(END, self.DIR)
    def ABAS_FRAMES(self):
        self.FRAME_01 = Frame(self.janela)
        self.FRAME_01.place(relx=0.01,rely=0.01, relwidth=0.99,relheight=0.90)
        self.abas = Notebook(self.FRAME_01)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba1.configure(background='lightgray')
        self.aba2.configure(background="lightgray")
        self.abas.add(self.aba1,text="PlayList")
        self.abas.add(self.aba2,text="Video Unico")
        self.abas.place(relx=0,rely=0, relwidth=0.98,relheight=0.98)
APP()
