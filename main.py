
#Interfaz gráfica con Tkinter

#Importaciones

import tkinter as tk  #módulo para crear la interfaz gráfica
from tkinter import messagebox  #para mostrar mensajes emergentes
from Contactos import Contacto #la clase creada en contactos.py



def agregar_contacto():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    contacto = Contacto(nombre, apellido, telefono, email)
    contacto.guardar()
    messagebox.showinfo("Éxito", "Contacto agregado correctamente")
    listar_contactos()

def listar_contactos():
    lista.delete(0, tk.END)
    for c in Contacto.listar():
        lista.insert(tk.END, f"{c[0]} - {c[1]} {c[2]} - {c[3]} - {c[4]}")

ventana = tk.Tk()
ventana.title("Gestor de Contactos")

tk.Label(ventana, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido").grid(row=1, column=0)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1)

tk.Label(ventana, text="Teléfono").grid(row=2, column=0)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=2, column=1)

tk.Label(ventana, text="Email").grid(row=3, column=0)
entry_email = tk.Entry(ventana)
entry_email.grid(row=3, column=1)

btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_contacto)
btn_agregar.grid(row=4, column=0, columnspan=2)

lista = tk.Listbox(ventana, width=50)
lista.grid(row=5, column=0, columnspan=2)

listar_contactos()

ventana.mainloop()
