import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import os
import json

# Crea una carpeta si no existe o uno se equivoca al escribir el nombre de algun Pokémon
if not os.path.exists('pokedex'):
    os.makedirs('pokedex')

# Bucle para permitir la búsqueda de varios Pokémon
while True:
    # Obtener el nombre del Pokémon de parte del usuario
    pokemon = input("Introduce el nombre o ID de un Pokémon (o 'salir' para terminar): ").lower()

    if pokemon == 'salir':
        print("Gracias por usar la Pokédex. ¡Hasta la próxima!")
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    try:
        # Hacer la petición a la API
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción si el código de estado no es 200
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}. Verifica el nombre o ID e intenta de nuevo.")
        continue
    except Exception as err:
        print(f"Ocurrió un error: {err}. Verifica el nombre o ID e intenta de nuevo.")
        continue

    # Si la respuesta es exitosa, extraemos los datos
    data = response.json()

    # Extraer datos
    name = data['name'].capitalize()
    weight = data['weight']
    height = data['height']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    moves = [move['move']['name'] for move in data['moves'][:10]]  # Mostrar solo los primeros 10 movimientos
    types = [type_info['type']['name'] for type_info in data['types']]
    image_url = data['sprites']['front_default']

    # Mostrar información en la consola
    print(f"\nNombre: {name}")
    print(f"Peso: {weight} hectogramos")
    print(f"Altura: {height} decímetros")
    print(f"Tipos: {', '.join(types)}")
    print(f"Habilidades: {', '.join(abilities)}")
    print(f"Movimientos (mostrando 10): {', '.join(moves)}")
    print(f"URL de la imagen: {image_url}\n")

    # Guardar la información en un archivo JSON
    pokemon_data = {
        "name": name,
        "weight": weight,
        "height": height,
        "abilities": abilities,
        "moves": moves,
        "types": types,
        "image_url": image_url
    }

    with open(f"pokedex/{name}.json", "w") as json_file:
        json.dump(pokemon_data, json_file, indent=4)

    print(f"Datos guardados en 'pokedex/{name}.json'")

    # Intentar mostrar la imagen con matplotlib y los detalles
    try:
        imagen = Image.open(urlopen(image_url))
        plt.figure(figsize=(8, 6))
        plt.title(name)
        plt.imshow(imagen)
        plt.axis('off')  # Ocultar los ejes para una mejor visualización

        # Añadir detalles del Pokémon como texto en la gráfica
        info_text = (
            f"Peso: {weight} hectogramos\n"
            f"Altura: {height} decímetros\n"
            f"Tipos: {', '.join(types)}\n"
            f"Habilidades: {', '.join(abilities)}\n"
            f"Movimientos: {', '.join(moves)}"
        )
        plt.text(
            0.0, 0.0, info_text, fontsize=12.5, transform=plt.gca().transAxes,
            verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5)
        )

        plt.show()
    except Exception as e:
        print('El Pokémon no tiene imagen disponible o ocurrió un error al mostrar la imagen:', e)
