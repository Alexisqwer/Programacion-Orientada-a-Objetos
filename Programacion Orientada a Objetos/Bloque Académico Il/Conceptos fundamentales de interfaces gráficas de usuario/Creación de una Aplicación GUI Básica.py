import tkinter as tk
from tkinter import messagebox, font


# Función que se ejecuta al presionar el botón "Agregar"
def agregar_dato():
    dato = entry_text.get()  # Obtiene el texto del campo de entrada
    if dato:
        listbox_datos.insert(tk.END, dato)  # Agrega el texto a la lista
        entry_text.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia",
                               "El campo de texto está vacío")  # Muestra una advertencia si el campo está vacío


# Función que se ejecuta al presionar el botón "Limpiar"
def limpiar_lista():
    listbox_datos.delete(0, tk.END)  # Elimina todos los elementos de la lista


# Función que se ejecuta al presionar el botón "Eliminar Selección"
def eliminar_seleccion():
    seleccion = listbox_datos.curselection()  # Obtiene el índice del elemento seleccionado
    if seleccion:
        listbox_datos.delete(seleccion)  # Elimina el elemento seleccionado
    else:
        messagebox.showwarning("Advertencia",
                               "No hay ningún elemento seleccionado para eliminar")  # Muestra advertencia si no hay selección


# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Gestión de Datos")  # Título de la ventana

# Configurar el diseño de la ventana
root.geometry("400x500")  # Tamaño inicial de la ventana
root.configure(bg="#f0f0f0")  # Color de fondo

# Crear un marco principal que contendrá todos los componentes
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Crear un marco para la entrada de datos
input_frame = tk.Frame(main_frame, bg="#f0f0f0")
input_frame.pack(pady=10, padx=10, fill=tk.X)

# Fuente personalizada
titulo_fuente = font.Font(family="Helvetica", size=16, weight="bold")
boton_fuente = font.Font(family="Helvetica", size=12)

# Etiqueta de instrucciones
label_instrucciones = tk.Label(input_frame, text="Ingrese un dato y presione 'Agregar':", bg="#f0f0f0",
                               font=titulo_fuente)
label_instrucciones.grid(row=0, column=0, columnspan=2, pady=5, padx=5)  # Etiqueta con instrucciones

# Campo de texto para la entrada de datos
entry_text = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
entry_text.grid(row=1, column=0, columnspan=2, pady=5, padx=5)  # Coloca el campo de texto en el marco de entrada

# Botón en el marco de entrada
button_agregar = tk.Button(input_frame, text="Agregar", command=agregar_dato, font=boton_fuente, bg="#4CAF50",
                           fg="white", relief=tk.RAISED)
button_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")  # Botón de agregar

# Crear un marco para el área de salida
output_frame = tk.Frame(main_frame, bg="#f0f0f0")
output_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

# Lista para mostrar los datos
listbox_datos = tk.Listbox(output_frame, width=50, height=15, font=("Helvetica", 12), bg="#ffffff",
                           selectbackground="#d3d3d3")
listbox_datos.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)  # Coloca la lista en el marco de salida

# Crear un marco para los botones de acción
button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Botones en el marco de acción
button_limpiar = tk.Button(button_frame, text="Limpiar", command=limpiar_lista, font=boton_fuente, bg="#f44336",
                           fg="white", relief=tk.RAISED)
button_limpiar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")  # Botón de limpiar

button_eliminar = tk.Button(button_frame, text="Eliminar Selección", command=eliminar_seleccion, font=boton_fuente,
                            bg="#FFC107", fg="black", relief=tk.RAISED)
button_eliminar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")  # Botón de eliminar selección

button_cerrar = tk.Button(button_frame, text="Cerrar", command=root.quit, font=boton_fuente, bg="#9E9E9E", fg="white",
                          relief=tk.RAISED)
button_cerrar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")  # Botón de cerrar

# Ajustar el peso de las columnas para centrar los botones
input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

# Iniciar el bucle principal de la aplicación
root.mainloop()