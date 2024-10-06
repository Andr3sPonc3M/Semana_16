

import tkinter as tk
from tkinter import messagebox

# Creación de la ventana principal
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tareas UEA POO")  # Nombre de la ventana

        # Campo para añadir tareas
        self.task_entry = tk.Entry(root, width=45)  # Ancho de la barra
        self.task_entry.pack(pady=10)  # Espaciado vertical

        # Botón para una nueva tarea
        self.add_task_button = tk.Button(root, text="Nueva Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Botón para marcar tarea completada
        self.complete_task_button = tk.Button(root, text="Tarea Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Campo para mostrar las tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Manejo de eventos para la tecla Enter
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())  # Atajo para completar tarea
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Atajo para eliminar tarea
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Atajo para cerrar la aplicación

    # Método para añadir tarea
    def add_task(self):
        task = self.task_entry.get()  # Obtener el texto del campo de entrada
        if task:  # Verificar que el campo no esté vacío
            self.task_listbox.insert(tk.END, task)  # Añadir tarea a la lista
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Ingrese una tarea para comenzar.")  # Mensaje si el campo de tareas está vacío

    # Método para marcar tarea como completada
    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            task = self.task_listbox.get(selected_index)  # Obtener la tarea seleccionada
            completed_task = f"{task} (Tarea Completada)"  # Marcarla como completada visualmente
            self.task_listbox.delete(selected_index)  # Eliminar la tarea original de la lista
            self.task_listbox.insert(selected_index, completed_task)  # Insertar la tarea completada en su lugar
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea antes de marcarla como completada.")  # Mensaje si no hay selección

    # Método para eliminar tarea
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            self.task_listbox.delete(selected_index)  # Eliminar la tarea seleccionada de la lista
        except IndexError:
            messagebox.showwarning("Advertencia", "Primero seleccione una tarea para eliminarla.")  # Mensaje si no hay selección

# Configuración y ejecución del programa
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = TaskManagerApp(root)  # Instanciar la clase principal
    root.mainloop()  # Iniciar el bucle principal de eventos
