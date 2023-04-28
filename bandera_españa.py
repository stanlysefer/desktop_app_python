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
ventana_principal.title("Bandera de alemania")

#tamaño de la ventana 
ventana_principal.geometry("500x500")

# Desabilitar botón de maximizar 
ventana_principal.resizable(False,False)

# color de fondo de la ventana 


#-------------------------
#frame rojo-----------
#-------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0 , y=0)

#-------------------------
#frame Rojo-----------
#-------------------------
frame_amarillo=Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0 , y=125)


#-------------------------
#frame rojo-----------
#-------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0 , y=375)

#-------------------------
#frame rojo-----------
#-------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="gray1", width=70, height=70)
frame_rojo.place(x=100 , y=200)

#run
#se ejecuta el metodo mainloop () de la clase Tk() a través de la instancia ventana_principal.Este metodo despliega la ventana en pantalla  queda a la espera a lo que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como un evento. Él metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()