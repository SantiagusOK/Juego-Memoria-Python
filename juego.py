from tkinter import *
import tkinter as tk
import random
from threading import Timer
from revisar_mezclas import *
import pygame
ventana = tk.Tk()
ventana.geometry("1280x720")
pygame.init()
class JuegoMemoria:
    def __init__(self):
        self.img_fondo = PhotoImage(file="fondo.png")
        self.fondo = Label(image=self.img_fondo,borderwidth=0)
        self.fondo.place(x=0,y=0)
        self.img_mezclando = PhotoImage(file="negro.png")
        self.cartas_totales = 10
        self.cartas_elejidas = 0
        self.carta1 = ""
        self.carta2 = ""
        self.cartas_seleccionadas = []
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        self.x5 = 0
        self.x6 = 0
        self.x7 = 0
        self.x8 = 0
        self.x9 = 0
        self.x10 = 0
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.y4 = 0
        self.y5 = 0
        self.y6 = 0
        self.y7 = 0
        self.y8 = 0
        self.y9 = 0
        self.y10 = 0
    def empezar_juego(self):
        self.cartas_totales = 10
        self.fondo.configure(image=self.img_fondo)
        musica.volumen = 10
        musica.reproducir_musica1()
        self.mezclar_cartas()
    def mezclar_cartas(self):
        ordenar_cartas(posicion_x,posicion_y)
        self.x1 = posicion_x[0]
        self.x2 = posicion_x[1]
        self.x3 = posicion_x[2]
        self.x4 = posicion_x[3]
        self.x5 = posicion_x[4]
        self.x6 = posicion_x[5]
        self.x7 = posicion_x[6]
        self.x8 = posicion_x[7]
        self.x9 = posicion_x[8]
        self.x10 = posicion_x[9]

        self.y1 = posicion_y[0]
        self.y2 = posicion_y[1]
        self.y3 = posicion_y[2]
        self.y4 = posicion_y[3]
        self.y5 = posicion_y[4]
        self.y6 = posicion_y[5]
        self.y7 = posicion_y[6]
        self.y8 = posicion_y[7]
        self.y9 = posicion_y[8]
        self.y10 = posicion_y[9]
        cartas.Mostrar_cartas(self.x1,self.x2,self.x3,self.x4,self.x5,
                              self.x6,self.x7,self.x8,self.x9,self.x10,
                              self.y1,self.y2,self.y3,self.y4,self.y5,
                              self.y6,self.y7,self.y8,self.y9,self.y10)
    def revisar_cartas2(self):
        self.cartas_elejidas = len(self.cartas_seleccionadas)
        if self.cartas_elejidas == 2:
            self.carta1 = self.cartas_seleccionadas[0]
            self.carta2 = self.cartas_seleccionadas[1]
            if self.carta1 == "leon" and self.carta2 == "leon":
                self.cartas_seleccionadas.clear()
                self.cartas_elejidas = 0
                self.cartas_totales -= 2
                cartas.quitar_leon()
            if self.carta1 == "perro" and self.carta2 == "perro":
                self.cartas_seleccionadas.clear()
                self.cartas_elejidas = 0
                self.cartas_totales -= 2
                cartas.quitar_perro()
            if self.carta1 == "gato" and self.carta2 == "gato":
                self.cartas_seleccionadas.clear()
                self.cartas_elejidas = 0
                cartas.quitar_gato()
                self.cartas_totales -= 2
            if self.carta1 == "vaca" and self.carta2 == "vaca":
                self.cartas_seleccionadas.clear()
                self.cartas_elejidas = 0
                cartas.quitar_vaca()
                self.cartas_totales -= 2
            if self.carta1 == "pollo" and self.carta2 == "pollo":
                self.cartas_seleccionadas.clear()
                self.cartas_elejidas = 0
                self.cartas_totales -= 2
                cartas.quitar_pollo()
            if self.cartas_totales == 6:
                musica.reproducir_musica2()
            if self.cartas_totales == 0:
                self.fondo.configure(image=self.img_mezclando)
                musica.volumen = 0
                musica.reproducir_musica2()
                tiempo_espera2()
            cartas.girar_cartas()
            self.cartas_elejidas = 0
            self.cartas_seleccionadas.clear()
            cartas.desbloquear_botones()
    def revisar_cartas(self):
        self.cartas_elejidas = len(self.cartas_seleccionadas)
        if self.cartas_elejidas == 2:
            cartas.bloquear_botones()
            tiempo_esperar()

class ImagenesCartas:
    def __init__(self):
        self.img_cartaLeon = PhotoImage(file="carta_leon.png")
        self.img_cartaPerro = PhotoImage(file="carta_perro.png")
        self.img_cartaGato = PhotoImage(file="carta_gato.png")
        self.img_cartaVaca = PhotoImage(file="carta_vaca.png")
        self.img_cartaPollo = PhotoImage(file="carta_pollo.png")

class CartasJuegos:
    def __init__(self):
        self.img_carta = PhotoImage(file="carta_atras.png")
        self.carta_leon1 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_leon1)
        self.carta_leon2 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_leon2)
        self.carta_perro1 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_perro1)
        self.carta_perro2 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_perro2)
        self.carta_gato1 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_gato1)
        self.carta_gato2 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_gato2)
        self.carta_vaca1 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_vaca1)
        self.carta_vaca2 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_vaca2)
        self.carta_pollo1 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_pollo1)
        self.carta_pollo2 = Button(ventana,image=self.img_carta,height=330,width=216,borderwidth=0,command=self.Eleccion_pollo2)
    def Mostrar_cartas(self,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,
                            y1,y2,y3,y4,y5,y6,y7,y8,y9,y10):
        self.carta_leon1.place(x=x1,y=y1)
        self.carta_leon2.place(x=x2,y=y2)
        self.carta_perro1.place(x=x3 ,y=y3)
        self.carta_perro2.place(x=x4  ,y=y4)
        self.carta_gato1.place(x=x5,y=y5)

        self.carta_gato2.place(x=x6,y=y6) 
        self.carta_vaca1.place(x=x7,y=y7)
        self.carta_vaca2.place(x=x8 ,y=y8)
        self.carta_pollo1.place(x=x9  ,y=y9)
        self.carta_pollo2.place(x=x10,y=y10)

################## LEON ##################
    
    def Eleccion_leon1(self):
        musica.sonar_paper()
        self.carta_leon1.configure(image=img.img_cartaLeon)
        juego.cartas_seleccionadas.append("leon")
        juego.revisar_cartas()
    def Eleccion_leon2(self):
        musica.sonar_paper()
        self.carta_leon2.configure(image=img.img_cartaLeon)
        juego.cartas_seleccionadas.append("leon")
        juego.revisar_cartas()
    def quitar_leon(self):
        self.carta_leon1.place_forget()
        self.carta_leon2.place_forget()

################## PERRO ##################

    def Eleccion_perro1(self):
        musica.sonar_paper()
        self.carta_perro1.configure(image=img.img_cartaPerro)
        juego.cartas_seleccionadas.append("perro")
        juego.revisar_cartas()
    def Eleccion_perro2(self):
        musica.sonar_paper()
        self.carta_perro2.configure(image=img.img_cartaPerro)
        juego.cartas_seleccionadas.append("perro")
        juego.revisar_cartas()
    def quitar_perro(self):
        self.carta_perro1.place_forget()
        self.carta_perro2.place_forget()

################## GATO ##################

    def Eleccion_gato1(self):
        musica.sonar_paper()
        self.carta_gato1.configure(image=img.img_cartaGato)
        juego.cartas_seleccionadas.append("gato")
        juego.revisar_cartas()
    def Eleccion_gato2(self):
        musica.sonar_paper()
        self.carta_gato2.configure(image=img.img_cartaGato)
        juego.cartas_seleccionadas.append("gato")
        juego.revisar_cartas()
    def quitar_gato(self):
        self.carta_gato1.place_forget()
        self.carta_gato2.place_forget()

################## VACA ##################

    def Eleccion_vaca1(self):
        musica.sonar_paper()
        self.carta_vaca1.configure(image=img.img_cartaVaca)
        juego.cartas_seleccionadas.append("vaca")
        juego.revisar_cartas()
    def Eleccion_vaca2(self):
        musica.sonar_paper()
        self.carta_vaca2.configure(image=img.img_cartaVaca)
        juego.cartas_seleccionadas.append("vaca")
        juego.revisar_cartas()
    def quitar_vaca(self):
        self.carta_vaca1.place_forget()
        self.carta_vaca2.place_forget()

################## POLLO ##################

    def Eleccion_pollo1(self):
        musica.sonar_paper()
        self.carta_pollo1.configure(image=img.img_cartaPollo)
        juego.cartas_seleccionadas.append("pollo")
        juego.revisar_cartas()
    def Eleccion_pollo2(self):
        musica.sonar_paper()
        self.carta_pollo2.configure(image=img.img_cartaPollo)
        juego.cartas_seleccionadas.append("pollo")
        juego.revisar_cartas()
    def quitar_pollo(self):
        self.carta_pollo1.place_forget()
        self.carta_pollo2.place_forget()


    def bloquear_botones(self):
        self.carta_leon1.configure(command=self.nada)
        self.carta_leon2.configure(command=self.nada)
        self.carta_perro1.configure(command=self.nada)
        self.carta_perro2.configure(command=self.nada)
        self.carta_gato1.configure(command=self.nada)
        self.carta_gato2.configure(command=self.nada)
        self.carta_vaca1.configure(command=self.nada)
        self.carta_vaca2.configure(command=self.nada)
        self.carta_pollo1.configure(command=self.nada)
        self.carta_pollo2.configure(command=self.nada)
    
    def desbloquear_botones(self):
        self.carta_leon1.configure(command=self.Eleccion_leon1)
        self.carta_leon2.configure(command=self.Eleccion_leon2)
        self.carta_perro1.configure(command=self.Eleccion_perro1)
        self.carta_perro2.configure(command=self.Eleccion_perro2)
        self.carta_gato1.configure(command=self.Eleccion_gato1)
        self.carta_gato2.configure(command=self.Eleccion_gato2)
        self.carta_vaca1.configure(command=self.Eleccion_vaca1)
        self.carta_vaca2.configure(command=self.Eleccion_vaca2)
        self.carta_pollo1.configure(command=self.Eleccion_pollo1)
        self.carta_pollo2.configure(command=self.Eleccion_pollo2)
    
    def girar_cartas(self):
        self.carta_leon1.configure(image=self.img_carta)
        self.carta_leon2.configure(image=self.img_carta)
        self.carta_perro1.configure(image=self.img_carta)
        self.carta_perro2.configure(image=self.img_carta)
        self.carta_gato1.configure(image=self.img_carta)
        self.carta_gato2.configure(image=self.img_carta)
        self.carta_vaca1.configure(image=self.img_carta)
        self.carta_vaca2.configure(image=self.img_carta)
        self.carta_pollo1.configure(image=self.img_carta)
        self.carta_pollo2.configure(image=self.img_carta)

    def nada(self):
        print("nada")
        #una funcion que no hace nada
        #excepto que printiar un "nada"

class MusicaParaJuego:
    def __init__(self):
        self.volumen = 0
        self.sound_seleccion = pygame.mixer.Sound("paper.wav")
    def reproducir_musica1(self):
        pygame.mixer.music.load("music1.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(999)
    def reproducir_musica2(self):
        pygame.mixer.music.load("music2.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(999)
    def reproducir_win(self):
        pygame.mixer.music.load("win.wav")
        pygame.mixer.music.play()
    def sonar_paper(self):
        pygame.mixer.Sound.play(self.sound_seleccion)
    
juego = JuegoMemoria()
cartas = CartasJuegos()
img = ImagenesCartas()
musica = MusicaParaJuego()

def tiempo_esperar():
    t1 = Timer(1,juego.revisar_cartas2)
    t1.start()
def tiempo_espera2():
    t1 = Timer(2,juego.empezar_juego)
    t1.start()

juego.empezar_juego()
ventana.mainloop()