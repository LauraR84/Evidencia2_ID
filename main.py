
#Interfaz gráfica con Tkinter

#Importaciones

import tkinter as tk  #módulo para crear la interfaz gráfica
from tkinter import messagebox  #para mostrar mensajes emergentes
from Contactos import Contacto #la clase creada en contactos.py

#Función para agregar contactos
#get() obtiene lo que el usuario escribió en el campo
#.strip() elimina espacios en blanco al inicio y al final (evita guardar “ Juan ” con espacios de más).

def agregar_contacto():
    nombre = entry_nombre.get().strip() 
    apellido = entry_apellido.get().strip()
    telefono = entry_telefono.get().strip()
    email = entry_email.get().strip()

#Si alguno está vacío → muestra un aviso y corta (return).

    if not nombre or not apellido or not telefono or not email:
        messagebox.showwarning("Atención", "Todos los campos son obligatorios")
        return

#Se crea un objeto Contacto.Se ejecuta su método .guardar() para escribir en la base.   

    contacto = Contacto(nombre, apellido, telefono, email)
    contacto.guardar()
    messagebox.showinfo("Éxito", "Contacto agregado correctamente")

#Limpiar los campos
#.delete(0, tk.END) borra el texto de cada campo de entrada
#listar_contactos() vuelve a cargar la lista con los datos actualizados

    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Refrescar la lista
    listar_contactos()

#Función para listar contactos
#lista.delete(0, tk.END) limpia la lista gráfica antes de cargarla de nuevo
#Contacto.listar() obtiene todos los contactos desde la base
#lista.insert() → agrega cada contacto al Listbox
def listar_contactos():
    lista.delete(0, tk.END)
    for c in Contacto.listar():
        lista.insert(tk.END, f"{c[0]} - {c[1]} {c[2]} - {c[3]} - {c[4]}")

#Configuración de la ventana principal (crea la ventana y le pone título)
ventana = tk.Tk()
ventana.title("Gestor de Contactos")

#Campos de entrada
#Label muestra un texto fijo
#.grid(row, column) organiza los elementos en una cuadrícula (fila, columna)
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

#Se repite para Apellido, Teléfono, Email
tk.Label(ventana, text="Apellido").grid(row=1, column=0)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1)

tk.Label(ventana, text="Teléfono").grid(row=2, column=0)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=2, column=1)

tk.Label(ventana, text="Email").grid(row=3, column=0)
entry_email = tk.Entry(ventana)
entry_email.grid(row=3, column=1)

#Botón Agregar
#Button crea un botón
#command=agregar_contacto  llama a esa función cuando se aprieta Agregar
#columnspan=2 el botón ocupa 2 columnas
#pady=5 agrega espacio vertical (en píxeles)
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_contacto)
btn_agregar.grid(row=4, column=0, columnspan=2, pady=5)

#Lista de contactos
#Listbox un cuadro donde se muestran todos los contactos
#width=50 define el ancho
#columnspan=2 ocupa dos columnas
lista = tk.Listbox(ventana, width=50)
lista.grid(row=5, column=0, columnspan=2)

#Cargar contactos al inicio
#Apenas se abre la ventana, ya carga los contactos guardados en la base
listar_contactos()

#Loop principal
#Mantiene abierta la ventana y esperando interacción del usuario
ventana.mainloop()
