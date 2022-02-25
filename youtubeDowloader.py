from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Notebook
from pathlib import Path
from pytube import YouTube, Playlist
import os
import time

class FUNCOES():      
    def baixar_unicoVideo(self):
        self.caminho2 = self.pasta_entry2.get()
        self.link2 = self.entry_LINK2.get()
        if (self.caminho2 =="") or ( self.link2 ==""):
          print("Todos os campos devem ser preenchidas|||")
        else:
          self.barra_Progresso2 = ttk.Progressbar(self.aba2,orient='horizontal', mode='determinate', length=300)
          self.barra_Progresso2.place(relx=0, rely=0.8, relwidth=1)
          self.yt2 = YouTube(self.link2)
          self.tamanho2 =round(((self.yt2.streams.get_highest_resolution().filesize)/1024)/1024)
          #print("Tamanho: ", self.tamanho)
          for item2 in range(self.tamanho2):
               time.sleep(1)
               self.barra_Progresso2['value']=item2
               self.janela.update()
          #print("LINK: ", self.link2)
          self.yt2.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
          self.lblAviso2 = Label(self.aba2, text="Download realizado com Sucesso !!!",bg='green', fg='white', font=('Arial Baltic', 12, 'bold'))
          self.lblAviso2.place(relx=0, rely=0.8, relwidth=1)
     
    def baixar_Playlist(self):
        self.caminho1 = self.pasta_entry1.get()
        self.link1 = self.entry_LINK1.get()
        self.barra_Progresso1 = ttk.Progressbar(self.aba1,orient='horizontal', mode='determinate', length=300)
        self.barra_Progresso1.place(relx=0, rely=0.8, relwidth=1)
        # print("Pasta :",self.caminho1)
        # print("Link: ", self.link1)
        if (self.caminho1 == "") or (self.link1 == ""):
          messagebox.showerror('Erro', 'Todos os camboa devem ser preenchidos!!!')
        else:
          if not 'list' in self.link1:
              messagebox.showerror('URL não é de uma PLAYLIST','O link deve ser de uma Playlist.\nPra unico vídeo use a outra ABA')
          else:
              ##### Bloco de Comandos para baixar a PlayList
              self.playlist = Playlist(self.link1)
              self.calculo = 100/(len(self.playlist.videos))
              self.contador = 1
              self.calculo = 100/(len(self.playlist.videos))
              for self.video in self.playlist.videos:
                  self.yt = YouTube(self.video.watch_url)
                  self.RESOLUCAO = self.yt.streams.get_highest_resolution().itag
                  self.prefixo="#"+str(self.contador)+" - "
                  self.audioStream = self.video.streams.get_by_itag(self.RESOLUCAO)
                  self.audioStream.download(output_path=self.caminho1+self.playlist.title, filename_prefix=self.prefixo)
                  self.barra_Progresso1['value'] += self.calculo
                  self.janela.update()
                  self.contador += 1
              messagebox.showwarning('Youtube Downloader','Download Concluido com Sucesso!!!')


    def limpar_Campos(self):
        self.entry_LINK1.delete(0,END)
        self.entry_LINK2.delete(0,END)
        self.pasta_entry1.delete(0,END)
        self.pasta_entry2.delete(0,END)
    
class APP(FUNCOES):
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
        self.btn_BAIXAR1 = Button(self.aba1, text='Baixar',font=('Arial Baltic',12,'italic'),bg='#DC143C', fg='white', activebackground='#FF1493', activeforeground='white',command=self.baixar_Playlist)
        self.btn_BAIXAR1.place(x=360, y=50)
        #ABA2 Vídeo único
        self.btn_BAIXAR2 = Button(self.aba2, text='Baixar',font=('Arial Baltic',12,'italic'),bg='#DC143C', fg='white', activebackground='#FF1493', activeforeground='white',command=self.baixar_unicoVideo)
        self.btn_BAIXAR2.place(x=360, y=50)
    def ENTRADAS(self):
        #Link PLAYLIST
        self.entry_LINK1 = Entry(self.aba1,font=('Arial Baltic',11,'italic'))
        self.entry_LINK1.place(x=115,y=53, relwidth=0.50)
        #Link VÍDEO ÚNICO
        self.entry_LINK2 = Entry(self.aba2,font=('Arial Baltic',11,'italic'))
        self.entry_LINK2.place(x=115,y=53, relwidth=0.50)
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
