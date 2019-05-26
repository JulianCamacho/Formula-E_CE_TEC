"""
Instituto Tecnológico de Costa Rica
    Ingeniería en Computadores
      Taller de Programación


    III Proyecto Programado
          Fórmula E_Tec
          Segunda Parte


            Profesor:
       Jeff Schmidt Peralta

          Estudiantes:
   José Julián Camacho Hernández
   José Antonio Espinoza Chaves

           I semestre
              2019

"""


### ========== BIBLIOTECAS ========== ###

from tkinter import *
from tkinter import messagebox
from io import open
import time
import os


### ========== VENTANA INICIO ========== ###

def Ventana_inicio():
    global Ventana_Inicio
    Ventana_Inicio = Tk()
    Ventana_Inicio.title("Inicio")
    Ventana_Inicio.minsize(850, 550)
    Ventana_Inicio.resizable(width = NO, height = NO)
    Canvas_Inicio = Canvas(Ventana_Inicio, width = 850, height = 550, bg = "black")
    Canvas_Inicio.place(x = 0, y = 0)
    Imag_Fondo_Inicio = cargarimagen("BMW BG-min.png") 
    Fondo_Inicio = Canvas_Inicio.create_image(0,0, image = Imag_Fondo_Inicio, anchor = NW)
    #Imagen_Logo_Inicio = cargarimagen(Read("archivo_bmw.txt", 1)) 
    #ImagL_Inicio = Canvas_Inicio.create_image(500,30, image = Imagen_Logo_Inicio, anchor = NW)
    
    Li_1 = Label(Ventana_Inicio, text = "Bienvenido", font = ("Consolas","18"), anchor = NW)
    Li_1.place(x = 30, y = 60)
    About_Button = Button(Canvas_Inicio,text ="About" , bg = "black", fg = "White", command = Ventana_about)
    About_Button.place(x = 30, y = 500)
    Tabla_Button = Button(Canvas_Inicio,text ="Tabla de \n Posiciones" , bg = "black", fg = "White", command = Ventana_tabla)
    Tabla_Button.place(x = 100, y = 495)
    Escuderias_Button = Button(Canvas_Inicio,text ="Lista de \n escuderías" , bg = "black", fg = "White", command = Ventana_escuderias)
    Escuderias_Button.place(x = 200, y = 495)
    
    Ventana_Inicio.mainloop()

def cargarimagen(nombre): #Cargar imágenes
    ruta= os.path.join('Images_FE',nombre)
    imagen= PhotoImage(file=ruta)
    return imagen




### ========== VENTANA ABOUT ========== ###

def Ventana_about():
    Ventana_Inicio.withdraw()
    Ventana_About = Toplevel()
    Ventana_About.title("About")
    Ventana_About.minsize(850, 550)
    Ventana_About.resizable(width = NO, height = NO)
    Canvas_About = Canvas(Ventana_About, width = 850, height = 550, bg = "black")
    Canvas_About.place(x = 0, y = 0)
    Imagen1_About = cargarimagen("Formula_E_Logo.png") 
    Imag1_About = Canvas_About.create_image(650, 20, image = Imagen1_About, anchor = NW)
    Imagen2_About = cargarimagen(Read("archivo_about.txt", 12)) 
    Imag2_About = Canvas_About.create_image(50, 300, image = Imagen2_About, anchor = NW)
    #Imagen3_About = cargarimagen(Read("archivo_about.txt", 11)) 
    #Imag3_About = Canvas_About.create_image(550, 300, image = Imagen3_About, anchor = NW)

  
    La_1 = Label(Ventana_About, text = Read("archivo_about.txt", 0), font = ("Consolas","18"), bg = "black", fg = "dark turquoise", anchor = NW)
    La_1.place(x = 30, y = 30)
    La_2 = Label(Ventana_About, text = Read("archivo_about.txt", 1), font = ("Consolas","15"), bg = "black", fg = "dark turquoise", anchor = NW)
    La_2.place(x = 30, y = 70)
    La_3 = Label(Ventana_About, text = Read("archivo_about.txt", 2), font = ("Consolas","15"), bg = "black", fg = "dark turquoise", anchor = NW)
    La_3.place(x = 30, y = 100)
    La_4 = Label(Ventana_About, text = Read("archivo_about.txt", 3), font = ("Consolas","12"), bg = "black", fg = "white", anchor = NW)
    La_4.place(x = 30, y = 130)
    La_5 = Label(Ventana_About, text = Read("archivo_about.txt", 4), font = ("Consolas","12"), bg = "black", fg = "white", anchor = NW)
    La_5.place(x = 30, y = 150)
    La_6 = Label(Ventana_About, text = Read("archivo_about.txt", 5), font = ("Consolas","15"), bg = "black", fg = "dark turquoise", anchor = NW)
    La_6.place(x = 30, y = 220)
    La_7 = Label(Ventana_About, text = Read("archivo_about.txt", 6), font = ("Consolas","12"), bg = "black", fg = "white", anchor = NW)
    La_7.place(x = 30, y = 250)
    La_8 = Label(Ventana_About, text = Read("archivo_about.txt", 7), font = ("Consolas","15"), bg = "black", fg = "dark turquoise", anchor = NW)
    La_8.place(x = 500, y = 220)
    La_9 = Label(Ventana_About, text = Read("archivo_about.txt", 8), font = ("Consolas","12"), bg = "black", fg = "white", anchor = NW)
    La_9.place(x = 500, y = 250)
    La_10 = Label(Ventana_About, text = Read("archivo_about.txt", 9), font = ("Consolas","12"), bg = "black", fg = "white", anchor = NW)
    La_10.place(x = 630, y = 120)
    La_11 = Label(Ventana_About, text = Read("archivo_about.txt", 10), font = ("Consolas","12"), bg = "black", fg = "white", anchor = NW)
    La_11.place(x = 630, y = 140)
    
    
    

    def Cerrar_about():
        Ventana_About.destroy()
        Ventana_Inicio.deiconify()

    About_Cerrar_Button = Button(Canvas_About, text = "Regresar al menú", bg = "dark turquoise", fg = "black", command = Cerrar_about)
    About_Cerrar_Button.place(x = 720, y = 500)
    
    Ventana_About.mainloop()

def Read(archivo, linea):
    archivo = open (archivo, "r")
    lineas_texto = archivo.readlines()
    archivo.close()
    texto = lineas_texto[linea]
    return str(texto)

    
    
### ========== VENTANA TABLA DE POSICIONES ========== ###

def Ventana_tabla():
    Ventana_Inicio.withdraw()
    Ventana_Tabla = Toplevel()
    Ventana_Tabla.title("Tabla de Posiciones")
    Ventana_Tabla.minsize(850, 550)
    Ventana_Tabla.resizable(width = NO, height = NO)
    Canvas_Tabla = Canvas(Ventana_Tabla, width = 850, height = 550, bg = "yellow")
    Canvas_Tabla.place(x = 0, y = 0)

    def Cerrar_tabla():
        Ventana_Tabla.destroy()
        Ventana_Inicio.deiconify()

    Tabla_Cerrar_Button = Button(Canvas_Tabla, text = "Regresar al menú", bg = "black", fg = "white", command = Cerrar_tabla)
    Tabla_Cerrar_Button.place(x = 100, y = 400)

    Ventana_Tabla.mainloop()
    

### ========== VENTANA ESCUDERÍAS ========== ###

def Ventana_escuderias():
    global Ventana_Escuderias
    Ventana_Inicio.withdraw()
    Ventana_Escuderias = Toplevel()
    Ventana_Escuderias.title("Escuderías")
    Ventana_Escuderias.minsize(850, 550)
    Ventana_Escuderias.resizable(width = NO, height = NO)
    Canvas_Escuderias = Canvas(Ventana_Escuderias, width = 850, height = 550, bg = "snow")
    Canvas_Escuderias.place(x = 0, y = 0)
    Imag1_Escuderias = cargarimagen("Formula_E_Logo.png") 
    Imagen1_Escuderias = Canvas_Escuderias.create_image(650, 20, image = Imag1_Escuderias, anchor = NW)

    Crear_Escuderias_Button = Button(Canvas_Escuderias,text ="Crear nueva \n escudería" , bg = "dark turquoise", fg = "black", command = Ventana_crear_escuderias)
    Crear_Escuderias_Button.place(x = 30, y = 490)
    

    def Cerrar_escuderias():
        Ventana_Escuderias.destroy()
        Ventana_Inicio.deiconify()

    Escuderias_Cerrar_Button = Button(Canvas_Escuderias, text = "Regresar al menú", bg = "black", fg = "white", command = Cerrar_escuderias)
    Escuderias_Cerrar_Button.place(x = 720, y = 500)

    Ventana_Escuderias.mainloop()
    

### ========== VENTANA CREAR ESCUDERÍAS ========== ###

def Ventana_crear_escuderias():
    Ventana_Escuderias.withdraw()
    Ventana_Crear_Escuderias = Toplevel()
    Ventana_Crear_Escuderias.title("Crear Escuderías")
    Ventana_Crear_Escuderias.minsize(550, 350)
    Ventana_Crear_Escuderias.resizable(width = NO, height = NO)
    Canvas_Crear_Escuderias = Canvas(Ventana_Crear_Escuderias, width = 550, height = 350, bg = "grey")
    Canvas_Crear_Escuderias.place(x = 0, y = 0)

    def Cerrar_crear_escuderias():
        Ventana_Crear_Escuderias.destroy()
        Ventana_Escuderias.deiconify()

    Crear_Escuderias_Cerrar_Button = Button(Canvas_Crear_Escuderias, text = "Regresar a \n escuderías", bg = "black", fg = "white", command = Cerrar_crear_escuderias)
    Crear_Escuderias_Cerrar_Button.place(x = 460, y = 290)

    Ventana_Crear_Escuderias.mainloop()


### ========== VENTANA CREAR PILOTOS ========== ###

def Ventana_crear_pilotos():
    Ventana_Escuderias.withdraw()
    Ventana_Crear_Pilotos = Toplevel()
    Ventana_Crear_Pilotos.title("Crear Pilotos")
    Ventana_Crear_Pilotos.minsize(550, 350)
    Ventana_Crear_Pilotos.resizable(width = NO, height = NO)
    Canvas_Crear_Pilotos = Canvas(Ventana_Crear_Pilotos, width = 550, height = 350, bg = "grey")
    Canvas_Crear_Pilotos.place(x = 0, y = 0)

    def Cerrar_crear_pilotos():
        Ventana_Crear_Pilotos.destroy()
        Ventana_Escuderias.deiconify()

    Crear_Pilotos_Cerrar_Button = Button(Canvas_Crear_Pilotos, text = "Regresar a \n escuderías", bg = "black", fg = "white", command = Cerrar_crear_pilotos)
    Crear_Pilotos_Cerrar_Button.place(x = 460, y = 290)

    Ventana_Crear_Pilotos.mainloop() 


    
### ========== PILOTO ========== ###

class Piloto:
    def __init__(self, nombre, edad, nacionalidad, comp, podio, victorias, fallos):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad #Archivos de texto ?
        self.temporada = 2019
        self.competencias = comp
        self.podio = podio
        self.victorias = victorias
        self.fallos = fallos
    def get_victorias(self):
        return self.victorias
    def get_podio(self):
        return self.podio
    def get_competencias(self):
        return self.competencias
    def get_abandonos(self):
        return self.fallos
        
    def Rend_Global(self):
        self.RGP = ((get_victorias() + get_podio()) / (get_competencias() - get_abandonos()) * 100)
        return self.RGP
    def Rend_Espec(self):
        self.REP = ( get_victorias() / (get_competencias() - get_abandonos())) * 100
        return self.REP
    def Ind_Ganador(self):
        self.IGE = get_victorias() / get_competencias()
        return self.IGE

### ========== AUTOMÓVIL ========== ###

class Automovil():
    def __init__(self, marca, modelo, pais, baterias, pilas, tension, motores, sensores, peso):
        self.marca = marca
        self.modelo = modelo
        self.pais = pais
        self.temporada = 2019 #Archivos texto ?
        #self.foto =
        self.baterias = baterias
        self.pilas = pilas
        self.tension = tension
        #self.estado = 
        self.consumo = motores
        self.sensores = sensores
        self.peso = peso
        #self.eficiencia
    
    
               
Ventana_inicio()
    














