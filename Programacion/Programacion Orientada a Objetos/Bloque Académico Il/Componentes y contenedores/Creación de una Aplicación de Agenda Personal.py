import tkinter as tk  # Importa la librería Tkinter para crear la interfaz gráfica.
from tkinter import ttk, messagebox  # Importa ttk para widgets avanzados y messagebox para mostrar mensajes.
from tkcalendar import DateEntry  # Importa el DateEntry de tkcalendar para el selector de fecha.
import re  # Importa re para utilizar expresiones regulares, en este caso para validar la hora.


class AgendaPersonal:
    def __init__(self, root):
        # Inicializa la ventana principal de la aplicación.
        self.root = root
        self.root.title("Agenda Personal Mejorada")  # Establece el título de la ventana.
        self.root.geometry("700x500")  # Define el tamaño de la ventana.

        # Frame principal para entrada de datos (fecha, hora y descripción).
        frame_inputs = tk.Frame(self.root)
        frame_inputs.pack(pady=10)  # Coloca el frame con un poco de espacio vertical (10 píxeles).

        # Etiqueta y campo para la entrada de fecha con un DateEntry.
        tk.Label(frame_inputs, text="Fecha:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_inputs, date_pattern='y-mm-dd', width=12, font=("Arial", 10))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo para la entrada de la hora.
        tk.Label(frame_inputs, text="Hora (HH:MM):", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
        self.hour_entry = tk.Entry(frame_inputs, width=12, font=("Arial", 10))
        self.hour_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo para la descripción del evento.
        tk.Label(frame_inputs, text="Descripción:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_inputs, width=30, font=("Arial", 10))
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones de acción (agregar, eliminar, buscar, salir).
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        # Botón para agregar un nuevo evento.
        self.add_button = tk.Button(frame_buttons, text="Agregar Evento", command=self.agregar_evento, width=15,
                                    font=("Arial", 10))
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        # Botón para eliminar el evento seleccionado.
        self.delete_button = tk.Button(frame_buttons, text="Eliminar Evento", command=self.eliminar_evento, width=15,
                                       font=("Arial", 10))
        self.delete_button.grid(row=0, column=1, padx=10, pady=5)

        # Botón para buscar eventos por descripción.
        self.search_button = tk.Button(frame_buttons, text="Buscar Evento", command=self.buscar_evento, width=15,
                                       font=("Arial", 10))
        self.search_button.grid(row=0, column=2, padx=10, pady=5)

        # Botón para salir de la aplicación.
        self.quit_button = tk.Button(frame_buttons, text="Salir", command=self.confirmar_salida, width=15,
                                     font=("Arial", 10))
        self.quit_button.grid(row=0, column=3, padx=10, pady=5)

        # Tabla (Treeview) para mostrar los eventos agregados.
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Establece el encabezado de la columna Fecha.
        self.tree.heading("Hora", text="Hora")  # Establece el encabezado de la columna Hora.
        self.tree.heading("Descripción", text="Descripción")  # Establece el encabezado de la columna Descripción.
        self.tree.pack(pady=20, fill="both", expand=True)  # Empaqueta la tabla en la ventana principal.

        # Barra de desplazamiento vertical para la tabla.
        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Etiqueta y campo de entrada para buscar eventos por descripción.
        tk.Label(self.root, text="Buscar por descripción:", font=("Arial", 10)).pack(pady=5)
        self.search_entry = tk.Entry(self.root, width=30, font=("Arial", 10))
        self.search_entry.pack()  # Empaqueta el campo de búsqueda en la ventana principal.

    def agregar_evento(self):
        """Agrega un nuevo evento a la agenda."""
        fecha = self.date_entry.get()  # Obtiene la fecha ingresada en el DateEntry.
        hora = self.hour_entry.get()  # Obtiene la hora ingresada en el campo de texto.
        descripcion = self.desc_entry.get()  # Obtiene la descripción del evento.

        # Valida que la hora esté en formato HH:MM.
        if not self.validar_hora(hora):
            messagebox.showerror("Hora inválida", "Por favor, ingrese una hora válida en formato HH:MM.")
            return

        # Verifica que la descripción no esté vacía antes de agregar el evento.
        if descripcion:
            # Agrega el evento en la tabla (Treeview).
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.limpiar_campos()  # Limpia los campos de entrada después de agregar el evento.
        else:
            messagebox.showwarning("Campos incompletos",
                                   "Por favor, complete todos los campos.")  # Muestra advertencia si faltan campos.

    def eliminar_evento(self):
        """Elimina el evento seleccionado de la tabla."""
        selected_item = self.tree.selection()  # Obtiene el elemento seleccionado en la tabla.
        if selected_item:
            # Muestra un cuadro de confirmación antes de eliminar el evento.
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)  # Elimina el evento seleccionado si el usuario confirma.
        else:
            messagebox.showwarning("Sin selección",
                                   "Por favor, seleccione un evento para eliminar.")  # Muestra advertencia si no hay selección.

    def buscar_evento(self):
        """Busca eventos por la descripción ingresada en el campo de búsqueda."""
        search_term = self.search_entry.get().lower()  # Obtiene el término de búsqueda y lo convierte a minúsculas.
        # Recorre cada evento en la tabla para verificar si coincide con el término de búsqueda.
        for row in self.tree.get_children():
            desc = self.tree.item(row, "values")[2].lower()  # Obtiene la descripción del evento en minúsculas.
            if search_term in desc:
                # Si encuentra una coincidencia, selecciona y enfoca ese evento.
                self.tree.selection_set(row)
                self.tree.focus(row)
                break
        else:
            messagebox.showinfo("Búsqueda",
                                "No se encontraron coincidencias.")  # Muestra un mensaje si no hay coincidencias.

    def limpiar_campos(self):
        """Limpia los campos de entrada después de agregar un evento."""
        self.hour_entry.delete(0, tk.END)  # Borra el campo de hora.
        self.desc_entry.delete(0, tk.END)  # Borra el campo de descripción.

    def confirmar_salida(self):
        """Confirma si el usuario desea salir de la aplicación."""
        # Muestra un cuadro de confirmación para salir de la aplicación.
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()  # Cierra la aplicación si el usuario confirma.

    def validar_hora(self, hora):
        """Valida que la hora ingresada esté en formato HH:MM usando una expresión regular."""
        return bool(re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", hora))  # Verifica que la hora esté entre 00:00 y 23:59.


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de Tkinter.
    app = AgendaPersonal(root)  # Instancia la clase AgendaPersonal con la ventana root.
    root.mainloop()  # Inicia el loop principal de la aplicación.
