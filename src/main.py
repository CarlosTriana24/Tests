import tkinter as tk
from tkinter import messagebox
from utilities import tkinter_utilities as tk_utils


class Application(tk.Frame):
    def __init__(self, master=None, width=500, height=400):
        super().__init__(master)
        self.master = master
        self.master.update_idletasks()

        # Posicionar ventana en el centro
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        pos_x = (screen_width - width) // 2
        pos_y = (screen_height - height) // 2

        self.master.title("Registro de Usuarios")
        self.master.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        self.pack()

        self.form_user()

    def form_user(self):
        """Formulario de registro de usuario."""
        # Mensaje de bienvenida
        self.label_welcome = tk.Label(
            self,
            text="Bienvenido al Registro de Usuarios",
            font=("Arial", 14),
            relief="solid",
        )
        self.label_welcome.pack(pady=10, padx=10, fill="x")

        # Nombre
        self.label_name = tk.Label(self, text="Nombre:")
        self.label_name.pack()
        self.input_name = tk.Entry(self)
        self.input_name.pack()
        self.input_name.focus()

        # Edad
        self.label_age = tk.Label(self, text="Edad:")
        self.label_age.pack()
        self.input_age = tk.Entry(self)
        self.input_age.pack()
        self.input_age.bind("<Return>", lambda e: self.save_user())

        # Botón de Registrar
        self.button_register = tk.Button(self, text="Registrar", command=self.save_user)
        self.button_register.pack(pady=10)

        # Botón para Mostrar Usuarios
        self.button_show_users = tk.Button(
            self, text="Mostrar Usuarios", command=self.table_users
        )
        self.button_show_users.pack(pady=10)

    def save_user(self):
        """Guarda el usuario en un archivo."""
        try:
            name = self.input_name.get().strip()
            age = self.input_age.get().strip()

            if not name or not age.isdigit():
                tk_utils.show_error(
                    "Error", "Debe ingresar un nombre y una edad válida"
                )
                return

            with open("usuarios.txt", "a", encoding="utf-8") as f:
                f.write(f"{name},{age};")

            tk_utils.show_message("Registro", "Usuario registrado correctamente")

            # Limpiar campos
            self.input_name.delete(0, tk.END)
            self.input_age.delete(0, tk.END)
            self.input_name.focus()

        except FileNotFoundError:
            tk_utils.show_error("Error", "No se pudo abrir el archivo de usuarios")
        except Exception as e:
            tk_utils.show_error("Error", f"Ocurrió un error: {e}")

    def table_users(self):
        """Muestra la lista de usuarios registrados en una nueva ventana."""
        self.master.withdraw()  # Oculta la ventana principal

        self.table = tk.Toplevel(self)
        self.table.title("Usuarios Registrados")

        # Centrar ventana
        pos_x = (self.master.winfo_screenwidth() - 400) // 2
        pos_y = (self.master.winfo_screenheight() - 300) // 2
        self.table.geometry(f"400x300+{pos_x}+{pos_y}")

        # Listbox para mostrar usuarios
        list_users = tk.Listbox(self.table)
        list_users.pack(fill="both", expand=True, padx=10, pady=10)

        # Leer usuarios desde el archivo
        try:
            with open("usuarios.txt", "r", encoding="utf-8") as f:
                contenido = f.read()
                usuarios = contenido.split(";")
                for usuario in usuarios:
                    if usuario:
                        name, age = usuario.split(",")
                        list_users.insert(tk.END, f"{name} - {age} años")
        except FileNotFoundError:
            list_users.insert(tk.END, "No hay usuarios registrados")

        # Botón para volver a la ventana principal
        button_close = tk.Button(
            self.table, text="Volver", command=self.close_table_users
        )
        button_close.pack(pady=10)

    def close_table_users(self):
        """Cierra la ventana de usuarios y muestra la principal."""
        self.table.destroy()
        self.master.deiconify()


class User:
    """Clase para representar un usuario."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
