import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

# Configuración de la conexión a la base de datos
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='videogames_db',  # Base de datos a utilizar
            user='root',  # Cambia esto si tu usuario de MySQL es diferente
            password='password'  # Cambia esto por tu contraseña
        )
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Error de conexión", f"Error al conectar a la base de datos: {e}")
        return None

# Crear un nuevo juego en la base de datos
def create_game():
    name = entry_name.get()
    release_date = entry_release_date.get()
    genre = entry_genre.get()
    
    if not name or not release_date or not genre:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return
    
    connection = connect_to_db()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        query = "INSERT INTO games (name, release_date, genre) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, release_date, genre))
        connection.commit()
        messagebox.showinfo("Éxito", "Juego agregado correctamente.")
        connection.close()
    except Error as e:
        messagebox.showerror("Error de base de datos", f"Error al agregar el juego: {e}")

# Leer todos los juegos de la base de datos
def read_games():
    connection = connect_to_db()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM games")
        games = cursor.fetchall()
        text_output.delete(1.0, tk.END)  # Limpiar el área de texto antes de mostrar los juegos
        for game in games:
            text_output.insert(tk.END, f"ID: {game[0]}, Nombre: {game[1]}, Fecha: {game[2]}, Género: {game[3]}\n")
        connection.close()
    except Error as e:
        messagebox.showerror("Error de base de datos", f"Error al leer los juegos: {e}")

# Actualizar un juego existente
def update_game():
    game_id = entry_id.get()
    new_name = entry_name.get()
    new_release_date = entry_release_date.get()
    new_genre = entry_genre.get()
    
    if not game_id or not new_name or not new_release_date or not new_genre:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return
    
    connection = connect_to_db()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        query = "UPDATE games SET name = %s, release_date = %s, genre = %s WHERE id = %s"
        cursor.execute(query, (new_name, new_release_date, new_genre, game_id))
        connection.commit()
        messagebox.showinfo("Éxito", "Juego actualizado correctamente.")
        connection.close()
    except Error as e:
        messagebox.showerror("Error de base de datos", f"Error al actualizar el juego: {e}")

# Eliminar un juego existente
def delete_game():
    game_id = entry_id.get()
    
    if not game_id:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese el ID del juego a eliminar.")
        return
    
    connection = connect_to_db()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        query = "DELETE FROM games WHERE id = %s"
        cursor.execute(query, (game_id,))
        connection.commit()
        messagebox.showinfo("Éxito", "Juego eliminado correctamente.")
        connection.close()
    except Error as e:
        messagebox.showerror("Error de base de datos", f"Error al eliminar el juego: {e}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Videojuegos")

# Definir los frames
frame_form = tk.Frame(root)
frame_form.grid(row=0, column=0, padx=10, pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.grid(row=1, column=0, padx=10, pady=10)

# Crear los elementos de la interfaz para el formulario
label_id = tk.Label(frame_form, text="ID del juego (para actualizar o eliminar):")
label_id.grid(row=0, column=0, sticky="e")
entry_id = tk.Entry(frame_form)
entry_id.grid(row=0, column=1)

label_name = tk.Label(frame_form, text="Nombre del juego:")
label_name.grid(row=1, column=0, sticky="e")
entry_name = tk.Entry(frame_form)
entry_name.grid(row=1, column=1)

label_release_date = tk.Label(frame_form, text="Fecha de lanzamiento (YYYY-MM-DD):")
label_release_date.grid(row=2, column=0, sticky="e")
entry_release_date = tk.Entry(frame_form)
entry_release_date.grid(row=2, column=1)

label_genre = tk.Label(frame_form, text="Género del juego:")
label_genre.grid(row=3, column=0, sticky="e")
entry_genre = tk.Entry(frame_form)
entry_genre.grid(row=3, column=1)

# Botones para las operaciones CRUD
button_create = tk.Button(frame_buttons, text="Crear Juego", command=create_game)
button_create.grid(row=0, column=0, padx=5, pady=5)

button_read = tk.Button(frame_buttons, text="Ver Juegos", command=read_games)
button_read.grid(row=0, column=1, padx=5, pady=5)

button_update = tk.Button(frame_buttons, text="Actualizar Juego", command=update_game)
button_update.grid(row=0, column=2, padx=5, pady=5)

button_delete = tk.Button(frame_buttons, text="Eliminar Juego", command=delete_game)
button_delete.grid(row=0, column=3, padx=5, pady=5)

# Área de texto para mostrar los resultados de la consulta
text_output = tk.Text(root, width=60, height=15)
text_output.grid(row=2, column=0, padx=10, pady=10)

# Iniciar la aplicación
root.mainloop()
