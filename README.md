 ##### Para el archivo "Pokedex_Con_GUI_TKINTER.py
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Para ejecutar el código de la Pokédex, necesitas instalar algunas bibliotecas de Python, especialmente si estás empezando con un entorno limpio. Aquí está la lista de las bibliotecas necesarias y cómo instalarlas:
Instalación de Bibliotecas Necesarias

    requests: Para realizar peticiones HTTP a la API de PokeAPI.
    Pillow (PIL): Para manejar y redimensionar imágenes.
    tkinter: Viene preinstalada con Python en la mayoría de las versiones, pero si tu instalación no la tiene, debes instalarla. En algunos sistemas, especialmente Linux, puede requerir un paquete adicional.

    Comandos para Instalación:
Para instalar estas bibliotecas, abre tu terminal (o símbolo del sistema) y ejecuta los siguientes comandos:

pip install requests
pip install Pillow
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Requisitos del Entorno:

    Python 3.x: Asegúrate de tener Python instalado. Si no lo tienes, descárgalo desde python.org.
    Acceso a Internet: Es necesario para que el programa pueda acceder a la API de pokeapi.co y descargar las imágenes de los Pokémon.

Comprobación de Instalación:
Para verificar si las bibliotecas están correctamente instaladas, puedes ejecutar lo siguiente en tu terminal o un script de Python:

import requests
import PIL
import tkinter as tk

Si no se muestran errores, la instalación ha sido exitosa y ya puedes ejecutar tu código de la Pokédex.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# El código utiliza la biblioteca requests para hacer peticiones a la API de pokeapi.co y obtener información de un Pokémon basado en su nombre o ID.

# La interfaz gráfica se construye con tkinter, configurada para simular una Pokédex con un estilo rojo y blanco.

# La ventana incluye etiquetas para mostrar la información del Pokémon (nombre, ID, peso, altura, habilidades y movimientos).

# La imagen del Pokémon se muestra y se redimensiona para que encaje en la interfaz.

# La función cargar_pokemon se encarga de buscar la información del Pokémon y manejar errores si el Pokémon no es encontrado o si hay problemas de conexión.

# La función mostrar_pokemon despliega la información en la ventana.

# La función guardar_pokemon guarda la información del Pokémon en un archivo .json dentro de la carpeta pokedex.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Este proyecto es un buen ejemplo para aplicar el consumo de APIs, manejo de datos en formato JSON, y la creación de una interfaz gráfica en Python. 
La estructura modular facilita la comprensión y el mantenimiento del código, y la posibilidad de guardar la información de los Pokémon permite extender la funcionalidad en el futuro.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 ##### Para el archivo Pokedex_Sin_GUI.py =  Necesitaras algunas dependecias.... 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Para poder ejecutar el código de la Pokédex, necesitarás instalar algunas bibliotecas de Python. A continuación, te indico las bibliotecas y cómo instalarlas:

Bibliotecas Necesarias

    requests: Permite hacer solicitudes HTTP a la API de PokeAPI para obtener la información de los Pokémon.
    matplotlib: Se usa para mostrar la imagen del Pokémon junto con sus detalles.
    Pillow (PIL): Se usa para abrir y manipular la imagen del Pokémon.
    json: Esta biblioteca viene integrada con Python y se usa para guardar la información del Pokémon en un archivo .json.
    os: También es una biblioteca integrada en Python y se usa para manejar la creación de carpetas y la gestión de archivos en el sistema.

    Instalación de Bibliotecas

Para instalar las bibliotecas que no vienen integradas con Python, abre una terminal o consola de comandos y ejecuta los siguientes comandos:

pip install requests
pip install matplotlib
pip install pillow


Versiones de Python:"""""""""
Asegúrate de tener Python 3.6 o superior, ya que es compatible con todas estas bibliotecas y las funciones usadas en el código. Puedes verificar la versión de Python instalada con:

python --version

"""""""""""""""""""""""""""""

Con estas instalaciones, tu entorno estará listo para ejecutar el código de la Pokédex sin problemas. 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
### Dependencias
- requests
- matplotlib
- Pillow (PIL)
- json (biblioteca estándar)

- Para insatalar las dependecias podrás escribir el siguiente código en terminal de VSC o en la terminal de Windows
- El código para instalar las dependecias es : pip install requests matplotlib pillow

## Cómo usar la Pokédex
1. Ejecuta el archivo `.py`.
2. Introduce el nombre o ID del Pokémon para obtener su información.
3. Para salir, ingresa 'salir'.


Es una Pokedex muy sencilla, pero es funcional, ya que entrega lo solicitado.



Y para terminar, les dejaré mi reflección de lo que aprendí al haber hecho mis programas. De antemano les agradezco su gran apoyo al irme guiando paso a paso en este Ucamp.

"""""""""""""""""""""""""""
## Descripción del Proyecto
Este proyecto consiste en la creación de una Pokédex utilizando Python y la API pública de PokeAPI. La aplicación permite buscar información sobre Pokémon a partir de su nombre o ID, y muestra detalles como su peso, altura, tipos, habilidades, y movimientos. Además, descarga la imagen del Pokémon y la muestra utilizando `matplotlib`.

Cada búsqueda de un Pokémon genera un archivo `.json` con su información, que se guarda dentro de una carpeta llamada `pokedex`. Esto facilita la consulta offline de los Pokémon previamente buscados.

## ¿Qué he aprendido?
Durante el desarrollo de este proyecto, he aprendido a:
-   **Consumir APIs**: A través de la biblioteca `requests`, pude realizar peticiones HTTP y manejar las respuestas para obtener datos de la API de PokeAPI.
-  **Manejo de archivos JSON**: Aprendí a guardar y leer información en archivos `.json`, lo cual me permitió almacenar de forma organizada los datos de cada Pokémon.
- **Control de errores con `try/except`**: Implementé control de errores para manejar problemas como conexiones fallidas, nombres de Pokémon inválidos y otras situaciones imprevistas.
-  **Manipulación de imágenes**: Usé `PIL` y `matplotlib` para descargar y mostrar imágenes de los Pokémon de forma gráfica, añadiendo detalles relevantes.
-   **Interacción con el usuario**: Mejoré la experiencia de usuario con un bucle que permite realizar varias consultas de Pokémon sin necesidad de reiniciar la aplicación.
-  **Organización de proyectos en GitHub**: Aprendí a crear y organizar un repositorio en GitHub, documentando cada parte del proyecto para facilitar su uso por otros desarrolladores.

## Instrucciones de Instalación
Para poder ejecutar este proyecto, necesitas tener instaladas algunas bibliotecas de Python. A continuación, se indican las instrucciones para instalar las dependencias:

### Dependencias
- `requests`
- `matplotlib`
- `pillow`

### Instalación
Ejecuta los siguientes comandos en tu terminal para instalar las bibliotecas necesarias:

```bash
pip install requests
pip install matplotlib
pip install pillow

