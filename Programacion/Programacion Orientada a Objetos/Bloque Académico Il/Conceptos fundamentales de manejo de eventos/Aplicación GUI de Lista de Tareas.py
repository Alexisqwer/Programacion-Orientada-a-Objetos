import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica.
from tkinter import messagebox  # Importa el módulo messagebox para mostrar diálogos emergentes.


class ListaTareas:
    def __init__(self, root):
        self.root = root  # Asigna la ventana principal a la variable `root`.
        self.root.title("Lista de Tareas")  # Establece el título de la ventana.
        self.root.geometry("400x400")  # Define las dimensiones de la ventana.

        # Campo de entrada para escribir nuevas tareas
        self.entry_tarea = tk.Entry(self.root,
                                    font=("Arial", 14))  # Crea un Entry para añadir tareas con una fuente de tamaño 14.
        self.entry_tarea.pack(pady=10)  # Empaqueta el Entry con un espacio vertical de 10 píxeles.

        # Botón para agregar tarea
        self.btn_agregar = tk.Button(self.root, text="Añadir Tarea",
                                     command=self.agregar_tarea)  # Crea un botón que llama a la función `agregar_tarea`.
        self.btn_agregar.pack(pady=5)  # Empaqueta el botón con un espacio vertical de 5 píxeles.

        # Botón para marcar una tarea como completada
        self.btn_completar = tk.Button(self.root, text="Marcar como Completada",
                                       command=self.marcar_como_completada)  # Crea un botón que llama a la función `marcar_como_completada`.
        self.btn_completar.pack(pady=5)  # Empaqueta el botón con un espacio vertical de 5 píxeles.

        # Botón para eliminar una tarea
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Tarea",
                                      command=self.eliminar_tarea)  # Crea un botón que llama a la función `eliminar_tarea`.
        self.btn_eliminar.pack(pady=5)  # Empaqueta el botón con un espacio vertical de 5 píxeles.

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(self.root, selectmode=tk.SINGLE, font=(
        "Arial", 14))  # Crea un Listbox donde se mostrarán las tareas, con selección de una sola tarea a la vez.
        self.lista_tareas.pack(pady=10, fill=tk.BOTH,
                               expand=True)  # Empaqueta el Listbox con espacio y le permite expandirse en ambas direcciones.

        # Mapeo de teclas a eventos
        self.entry_tarea.bind("<Return>",
                              lambda event: self.agregar_tarea())  # Asocia la tecla Enter a la función `agregar_tarea`.
        self.lista_tareas.bind("<Double-1>", lambda
            event: self.marcar_como_completada())  # Asocia el doble clic sobre una tarea a la función `marcar_como_completada`.
        self.root.bind("<Delete>",
                       lambda event: self.eliminar_tarea())  # Asocia la tecla Delete a la función `eliminar_tarea`.
        self.root.bind("<Escape>", lambda event: self.salir())  # Asocia la tecla Escape a la función `salir`.

    def agregar_tarea(self):
        """Agrega una nueva tarea si no está duplicada"""
        tarea = self.entry_tarea.get().strip()  # Obtiene la tarea ingresada en el Entry y elimina espacios en blanco a los lados.
        if tarea == "":  # Verifica si el campo de tarea está vacío.
            messagebox.showwarning("Advertencia",
                                   "No puedes agregar una tarea vacía.")  # Muestra un mensaje de advertencia si está vacío.
            return  # Sale de la función si no hay tarea.

        # Evita que se agreguen tareas duplicadas
        tareas_existentes = self.lista_tareas.get(0, tk.END)  # Obtiene todas las tareas existentes en el Listbox.
        if tarea in tareas_existentes:  # Verifica si la tarea ya existe.
            messagebox.showwarning("Advertencia",
                                   "La tarea ya está en la lista.")  # Muestra un mensaje de advertencia si la tarea es duplicada.
            return  # Sale de la función si la tarea ya existe.

        self.lista_tareas.insert(tk.END, tarea)  # Inserta la nueva tarea al final del Listbox.
        self.entry_tarea.delete(0, tk.END)  # Limpia el campo de entrada de tareas.

    def marcar_como_completada(self):
        """Marca la tarea seleccionada como completada y cambia su color"""
        seleccion = self.lista_tareas.curselection()  # Obtiene la tarea seleccionada en el Listbox.
        if seleccion:  # Verifica si se ha seleccionado una tarea.
            tarea = self.lista_tareas.get(seleccion)  # Obtiene el texto de la tarea seleccionada.
            if not tarea.startswith("✔️"):  # Verifica si la tarea ya está marcada como completada.
                self.lista_tareas.delete(seleccion)  # Elimina la tarea original del Listbox.
                tarea_completada = f"✔️ {tarea}"  # Agrega el símbolo de check a la tarea para indicar que está completada.
                self.lista_tareas.insert(seleccion,
                                         tarea_completada)  # Inserta la tarea completada de nuevo en el mismo lugar.
                self.lista_tareas.itemconfig(seleccion, {
                    'fg': 'gray'})  # Cambia el color de la tarea a gris para indicar su estado de completada.
            else:
                messagebox.showinfo("Info",
                                    "La tarea ya está completada.")  # Muestra un mensaje informando que la tarea ya está completada.
        else:
            messagebox.showwarning("Advertencia",
                                   "Selecciona una tarea para marcar como completada.")  # Muestra un mensaje de advertencia si no se selecciona ninguna tarea.

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.lista_tareas.curselection()  # Obtiene la tarea seleccionada en el Listbox.
        if seleccion:  # Verifica si se ha seleccionado una tarea.
            self.lista_tareas.delete(seleccion)  # Elimina la tarea seleccionada del Listbox.
        else:
            messagebox.showwarning("Advertencia",
                                   "Selecciona una tarea para eliminar.")  # Muestra un mensaje de advertencia si no se selecciona ninguna tarea.

    def salir(self):
        """Cierra la aplicación"""
        self.root.quit()  # Cierra la ventana principal y finaliza la aplicación.


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de la aplicación.
    app = ListaTareas(root)  # Crea una instancia de la clase ListaTareas.
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica.
