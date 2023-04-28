print("----------------------")
print(" Desktop App No. 1 ")
print("----------------------")

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#---------------------
# funciones de la app
#---------------------

#-------------------
# Ventana principal de la app

#se declara la variable llamada ventana_principal , que adquiere las caracteristicas de un objeto Tk()
ventana_principal=Tk()

# titulo de la ventana 
ventana_principal.title("Bandera de noruega")

#tamaño de la ventana 
ventana_principal.geometry("500x500")

# Desabilitar botón de maximizar 
ventana_principal.resizable(False,False)

# color de fondo de la ventana 
ventana_principal.config(bg="red")

#-------------------------
#frame rojo-----------
#-------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="white", width=300, height=100)
frame_rojo.place(x=100, y=200)

#-------------------------
#frame rojo-----------
#-------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="white", width=100, height=300)
frame_rojo.place(x=200 , y=100) 

#run
#se ejecuta el metodo mainloop () de la clase Tk() a través de la instancia ventana_principal.Este metodo despliega la ventana en pantalla  queda a la espera a lo que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como un evento. Él metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()