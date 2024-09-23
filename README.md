# Convertidor de Notebooks

Aplicación de escritorio desarrollada con Python y Tkinter, que permite convertir archivos Jupyter Notebook (`.ipynb`) a formatos HTML y Markdown.

## Requisitos

- Python 3.x
- Tkinter
- nbformat
- nbconvert

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:

    ```sh
    pip install nbformat nbconvert
    ```

## Uso

1. Ejecuta el script `main.py`:

    ```sh
    python main.py
    ```

2. Haz clic en "Seleccionar archivo" para elegir un archivo `.ipynb`.
3. Selecciona el formato de conversión deseado (HTML o Markdown) haciendo clic en el botón correspondiente.
4. Guarda el archivo convertido en la ubicación deseada.

## Funcionalidades

- **Seleccionar archivo**: Permite seleccionar un archivo Jupyter Notebook (`.ipynb`) desde el sistema de archivos.
- **Convertir a HTML**: Convierte el archivo seleccionado a formato HTML.
- **Convertir a Markdown**: Convierte el archivo seleccionado a formato Markdown.