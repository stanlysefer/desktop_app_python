# Desktop app No. 1

#Se importa toda la libreria tkinter
from tkinter import *
from tkinter import messagebox

#Funciones de la app
#sumar
def sumar():
    pass
#borrar
def borrar():
    pass
#salir
def salir():
    messagebox.showinfo("suma enteros 1.0 ", "la app se va a cerrar")
    ventana_principal.destroy()


#Ventana principal de la app


#Se declara una ventana llamada ventana_principal, que adquiere las caracteristicas de un objeto TK()
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("suma de enteros")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Desabilitar el boton de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="cyan2")


#---------------------------
#variables globales
#---------------------------
x = StringVar()
y = StringVar()



#-----------------------------------
# Entrada datos
#-----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

#logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=40)

#titulo de la app
titulo = Label(frame_entrada, text="Suma Enteros 1.0")
titulo.config(bg="white", fg="blue", font=("helvetica", 20))
titulo.place(x=240, y=10)

#etiqueta para elvalor de x
lb_x=Label(frame_entrada, text= " x =")
lb_x.config(bg="white", fg="blue", font=("helvetica", 20))
lb_x.place(x=240, y=60)

#caja de texto para elvalor x
entry_x=Entry(frame_entrada, textvariable="x =")
entry_x.config(bg="white", fg="blue", font=("Times New Roman", 18),width=6)
entry_x.focus_set()
entry_x.place(x=290, y=60)

#etiqueta para el valor de y
lb_y=Label(frame_entrada, text= " y =")
lb_y.config(bg="white", fg="blue", font=("helvetica", 20))
lb_y.place(x=240, y=120)

#caja de texto para el valor y
entry_y=Entry(frame_entrada, textvariable="y = ")
entry_y.config(bg="white", fg="blue", font=("Times New Roman", 18),width=6)
entry_y.focus_set()
entry_y.place(x=290, y=120)

#----------------------------------
# frama operaciones
#-----------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)


#boton para sumar
bt_sumar=Button(frame_operaciones , text="sumar", command=sumar)
bt_sumar.place(x=45, y=35, width=100, height=30)

#boton para borrar
bt_borrar=Button(frame_operaciones, text="borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=38)

#boton para salir
bt_salir=Button(frame_operaciones, text="salir",  command=salir)
bt_salir.place(x=335, y=35, width=100, height=38)


#-----------------------------------
# frame resultados
#-----------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

#area de texto para los resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow",font=("courier",20))
t_resultados.place(x=10, y=10, width=460, height=160)

#run
# Se ejecuta el metodo mainloop() de la clase Tk() a través de la ventana_prinsipal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que elusuario haga (click en un boton,escribir, etc). cada accion del usuario se conose como un evento. el método mainloop() es un bucle infinito.

ventana_principal.mainloop()