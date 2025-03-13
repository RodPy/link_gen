# link_gen

# Generador de Enlaces WhatsApp

Este proyecto es una herramienta de escritorio construida con Python y Tkinter que permite generar enlaces de WhatsApp personalizados a partir de un archivo CSV que contiene números de celular. La herramienta facilita la creación de enlaces para enviar un mensaje específico a múltiples números.

### Versión Ejecutable

Si prefieres no instalar Python, puedes descargar la versión compilada de la herramienta como un archivo ejecutable para Windows:

- [Descargar link_gen.exe]([https://github.com/RodPy/link_gen/blob/main/dist/UI.exe](https://drive.google.com/file/d/1c2AEJzHEjxlfG2dMmza6TZwL4YW1s4bp/view?usp=sharing))


## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python y las siguientes bibliotecas:

- **Tkinter**: Para la interfaz gráfica de usuario.
- **Pandas**: Para manejar y procesar datos CSV.

### Instalación

1. **Clona el repositorio o descarga el código fuente.**
   
2. **Instala las dependencias** utilizando el archivo `requirements.txt`:

   Si no tienes un entorno virtual, puedes crear uno (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux o macOS
   .\venv\Scripts\activate   # En Windows
   ```
   Luego, instala las dependencias con el siguiente comando:

   ```bash
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` contiene las siguientes dependencias necesarias para ejecutar el proyecto:

   ```txt
   pandas
   Pillow
   ```
   
## Características

- **Subir un archivo CSV**: Carga un archivo CSV que contenga números de celular.
- **Generación de enlaces**: Genera enlaces de WhatsApp para cada número en el archivo CSV con un mensaje personalizado.
- **Descarga de archivo**: Guarda el archivo generado con los enlaces de WhatsApp en formato CSV.

## Instrucciones de Uso

1. **Sube un archivo CSV**: Haz clic en "Seleccionar archivo" y elige un archivo CSV que contenga una única columna con de números de celular. El archivo debe contener solo una columna con los números de celular.
2. **Introduce un mensaje**: Escribe el mensaje que deseas enviar en el área de texto proporcionada.
3. **Genera los enlaces**: Haz clic en "Generar enlaces" para crear los enlaces de WhatsApp.

## Contribuir

Si deseas contribuir al proyecto, siéntete libre de abrir un "issue" o hacer un "pull request" en [GitHub](https://github.com/RodPy/link_gen.git).

## Licencia

Este proyecto está bajo la Licencia MIT.
