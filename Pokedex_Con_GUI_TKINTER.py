import requests
import json
import os
import PIL.Image, PIL.ImageTk
import tkinter as tk
from io import BytesIO

# Configuración de la ventana principal para simular la apariencia de una Pokédex
ventana = tk.Tk()
ventana.geometry("800x900")  # Ventana más grande
ventana.title("Pokédex")
ventana.config(bg="#D32F2F", padx=20, pady=20)

# Crear la carpeta 'pokedex' si no existe
if not os.path.exists("pokedex"):
    os.makedirs("pokedex")

# Etiqueta de título
titulo = tk.Label(ventana, text="Pokédex de Máximo", bg="#D32F2F", fg="white", font=("Arial", 32, "bold"))
titulo.pack(pady=10)

# Etiqueta para la imagen del Pokémon (aumentar el tamaño)
imagen_pokemon = tk.Label(ventana, bg="#D32F2F")
imagen_pokemon.pack(pady=10)

# Etiqueta para mostrar el ID y el nombre del Pokémon
info_id_nombre = tk.Label(ventana, bg="#D32F2F", fg="white", font=("Arial", 16), text="ID: - Nombre:")
info_id_nombre.pack(pady=5)

# Etiqueta para mostrar el peso y la altura del Pokémon
info_peso_altura = tk.Label(ventana, bg="#D32F2F", fg="white", font=("Arial", 16))
info_peso_altura.pack(pady=5)

# Etiqueta para mostrar las habilidades del Pokémon
info_habilidades = tk.Label(ventana, bg="#D32F2F", fg="white", font=("Arial", 14), justify="left", wraplength=700)
info_habilidades.pack(pady=5)

# Etiqueta para mostrar algunos movimientos del Pokémon
info_movimientos = tk.Label(ventana, bg="#D32F2F", fg="white", font=("Arial", 14), justify="left", wraplength=700)
info_movimientos.pack(pady=5)

# Función para buscar el Pokémon usando la API
def cargar_pokemon():
    nombre_o_id = texto_id_nombre.get(1.0, "end-1c").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id}"
    
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            mostrar_pokemon(datos)
            guardar_pokemon(datos)
        else:
            info_id_nombre.config(text="Pokémon no encontrado. Verifica el ID o nombre e intenta de nuevo.", fg="yellow")
            info_peso_altura.config(text="")
            info_habilidades.config(text="")
            info_movimientos.config(text="")
            imagen_pokemon.config(image="")
    except requests.exceptions.RequestException:
        info_id_nombre.config(text="Error al conectarse a la API. Inténtalo de nuevo.", fg="red")

# Función para mostrar la información del Pokémon
def mostrar_pokemon(datos):
    nombre = datos['name'].capitalize()
    numero = datos['id']
    peso = datos['weight'] / 10  # Peso en kilogramos
    altura = datos['height'] / 10  # Altura en metros
    habilidades = ', '.join([h['ability']['name'].capitalize() for h in datos['abilities']])
    movimientos = ', '.join([m['move']['name'].capitalize() for m in datos['moves'][:5]])  # Mostrar solo los primeros 5 movimientos

    # Obtener la imagen del Pokémon
    imagen_url = datos['sprites']['front_default']
    imagen_respuesta = requests.get(imagen_url)
    imagen = PIL.Image.open(BytesIO(imagen_respuesta.content))

    # Redimensionar la imagen
    imagen = imagen.resize((250, 250), PIL.Image.LANCZOS)  # Cambia el tamaño a 250x250 píxeles
    img = PIL.ImageTk.PhotoImage(imagen)
    imagen_pokemon.config(image=img)
    imagen_pokemon.image = img

    # Mostrar la información en los apartados
    info_id_nombre.config(text=f"ID: {numero} - Nombre: {nombre}", fg="white")
    info_peso_altura.config(text=f"Peso: {peso} kg - Altura: {altura} m", fg="white")
    info_habilidades.config(text=f"Habilidades: {habilidades}", fg="white")
    info_movimientos.config(text=f"Movimientos (ejemplos): {movimientos}", fg="white")

# Función para guardar la información del Pokémon en un archivo JSON
def guardar_pokemon(datos):
    nombre = datos['name']
    archivo_path = os.path.join("pokedex", f"{nombre}.json")
    with open(archivo_path, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    info_id_nombre.config(text=f"Datos de {nombre.capitalize()} guardados en {archivo_path}", fg="green")

# Etiqueta y cuadro de texto para el ID o nombre del Pokémon
etiqueta_id_nombre = tk.Label(ventana, text="ID o Nombre del Pokémon:", bg="#D32F2F", fg="white", font=("Arial", 16))
etiqueta_id_nombre.pack(pady=5)

texto_id_nombre = tk.Text(ventana, height=1, font=("Arial", 16))
texto_id_nombre.pack(pady=5)

# Botón para cargar la información del Pokémon
boton_cargar = tk.Button(ventana, text="Cargar Pokémon", command=cargar_pokemon, bg="#1976D2", fg="white", font=("Arial", 16))
boton_cargar.pack(pady=20)

# Iniciar la ventana principal
ventana.mainloop()
