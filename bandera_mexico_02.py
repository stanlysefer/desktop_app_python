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
ventana_principal.title("Bandera de mexico")

#tamaño de la ventana 
ventana_principal.geometry("500x500")

# Desabilitar botón de maximizar 
ventana_principal.resizable(False,False)

# color de fondo de la ventana 
ventana_principal.config(bg="blue")

#-------------------------
#frame azul-----------
#-------------------------
frame_azul=Frame(ventana_principal)
frame_azul.config(bg="sea green", width=166, height=500)
frame_azul.place(x=0, y=0)

#-------------------------
#frame blanco-----------
#-------------------------
frame_blanco=Frame(ventana_principal)
frame_blanco.config(bg="snow", width=332, height=500)
frame_blanco.place(x=166, y=0)


#-------------------------
#frame rojo---------------
#-------------------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=800)
frame_rojo.place(x=332, y=0)
#run
#se ejecuta el metodo mainloop () de la clase Tk() a través de la instancia ventana_principal.Este metodo despliega la ventana en pantalla  queda a la espera a lo que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como un evento. Él metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()