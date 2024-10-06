import tkinter as tk  # Importa Tkinter, la librería estándar de interfaces gráficas en Python
from tkinter import messagebox  # Importa las funciones de Tkinter para mostrar cuadros de mensajes
import re  # Importa la librería de expresiones regulares, aunque en este caso no se utiliza


class TaskManagerApp:
    def __init__(self, root):
        """Inicializa la aplicación."""
        self.root = root  # Guarda la referencia a la ventana principal
        self.root.title("Gestor de Tareas")  # Define el título de la ventana
        self.root.geometry("400x400")  # Establece el tamaño de la ventana

        # Crea una entrada de texto para escribir las tareas
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)  # Empaqueta el campo de entrada y agrega espacio vertical
        self.task_entry.bind("<Return>", self.add_task_event)  # Asigna la tecla "Enter" para añadir tarea

        # Crea un Listbox para mostrar la lista de tareas
        self.task_listbox = tk.Listbox(self.root, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, fill=tk.BOTH)  # Empaqueta el Listbox y lo ajusta al tamaño del contenedor
        self.task_listbox.bind("<Double-1>", self.complete_task_event)  # Asigna doble clic para completar tarea

        # Botón para añadir tareas
        self.add_task_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)  # Empaqueta el botón de añadir tarea

        # Botón para marcar como completada la tarea seleccionada
        self.complete_task_button = tk.Button(self.root, text="Marcar Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)  # Empaqueta el botón de marcar tarea como completada

        # Botón para eliminar la tarea seleccionada
        self.delete_task_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)  # Empaqueta el botón de eliminar tarea

        # Vincula la tecla "Delete" para eliminar la tarea seleccionada
        self.root.bind("<Delete>", self.delete_task_event)
        # Vincula la tecla "C" para marcar la tarea seleccionada como completada
        self.root.bind("<c>", self.complete_task_event)
        # Vincula la tecla "Escape" para salir de la aplicación
        self.root.bind("<Escape>", self.exit_app)

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get()  # Obtiene el texto del campo de entrada
        if task:  # Si hay texto, añade la tarea
            self.task_listbox.insert(tk.END, task)  # Añade la tarea al final del Listbox
            self.task_entry.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")  # Muestra un mensaje si está vacío

    def add_task_event(self, event):
        """Añade tarea cuando se presiona la tecla Enter."""
        self.add_task()  # Llama a la función para añadir tarea

    def complete_task(self):
        """Marca una tarea como completada."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
            task_text = self.task_listbox.get(selected_task_index)  # Obtiene el texto de la tarea seleccionada
            # Si la tarea ya está marcada como completada, no hacer nada
            if not task_text.startswith("[Completada]"):
                task_text = "[Completada] " + task_text  # Añade el prefijo de completada al texto de la tarea
                self.task_listbox.delete(selected_task_index)  # Elimina la tarea de la lista
                self.task_listbox.insert(selected_task_index,
                                         task_text)  # Inserta la tarea marcada en la misma posición
                self.task_listbox.itemconfig(selected_task_index, {'fg': 'green'})  # Cambia el color del texto a verde
        except IndexError:
            messagebox.showwarning("Sin selección",
                                   "Por favor, selecciona una tarea para marcar como completada.")  # Muestra un mensaje si no hay selección

    def complete_task_event(self, event):
        """Marca la tarea como completada con doble clic o la tecla 'C'."""
        self.complete_task()  # Llama a la función para completar tarea

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
            self.task_listbox.delete(selected_task_index)  # Elimina la tarea seleccionada de la lista
        except IndexError:
            messagebox.showwarning("Sin selección",
                                   "Por favor, selecciona una tarea para eliminar.")  # Muestra un mensaje si no hay selección

    def delete_task_event(self, event):
        """Elimina tarea cuando se presiona la tecla 'Delete'."""
        self.delete_task()  # Llama a la función para eliminar tarea

    def exit_app(self, event):
        """Cierra la aplicación cuando se presiona 'Escape'."""
        self.root.quit()  # Cierra la ventana principal y finaliza la aplicación


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManagerApp(root)  # Inicializa la aplicación con la ventana principal
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica
