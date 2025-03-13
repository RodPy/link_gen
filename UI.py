import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from urllib.parse import quote
from datetime import datetime
import webbrowser
from PIL import Image, ImageTk
import os

# Función para abrir el proyecto en GitHub
def abrir_github():
    webbrowser.open("https://github.com/RodPy/link_gen.git")

def subir_archivo():
    global df
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        print(f"Archivo seleccionado: {archivo}")

        # Mostrar el nombre del archivo en la interfaz
        nombre_archivo.set(archivo.split('/')[-1])  # Extraer solo el nombre del archivo

        # Marcar el checkbutton de que se cargó el archivo
        archivo_cargado.set(True)
        df = pd.read_csv(archivo)

        # Verificar si hay más de una columna
        if df.shape[1] > 1:
            messagebox.showerror("Error", "El archivo debe contener solo una columna con los números de celular.")
        else:
            df = df.rename(columns={df.columns[0]: 'celular'})
            df.dropna(subset=['celular'], inplace=True)

            mensaje.set("Archivo cargado correctamente")
            check_archivo_cargado.config(text="Archivo cargado")

            button_generar.config(state="normal")  # Habilitar el botón para generar enlaces

    else:
        nombre_archivo.set("Archivo no cargado")
        archivo_cargado.set(False)
        mensaje.set("Archivo no cargado")
        check_archivo_cargado.config(text="Archivo No cargado")
def generar_enlaces():

    # Verificar que df esté cargado
    global df
    mensaje_unificado = entry_mensaje.get("1.0", tk.END).strip()

    if 'df' not in globals():
        print("No se ha cargado un archivo CSV.")
        return

    if not mensaje_unificado:
        messagebox.showinfo("Error", "El mensaje no puede estar vacío.")

        print("El mensaje no puede estar vacío.")
        return

    print("Generando enlaces...")

    # Limpiar los números de celular
    df['celular'] = df['celular'].astype(str).str.replace(r'\.0$', '', regex=True)  # Eliminar .0 de los floats
    df['celular'] = df['celular'].str.replace(r'[^0-9]', '', regex=True)  # Eliminar caracteres no numéricos
    df['celular'] = df['celular'].str.lstrip('0')  # Eliminar ceros a la izquierda

    # Reemplazar los prefijos específicos (59590, 59509, 59599) por 5959
    df['celular'] = df['celular'].str.replace(r'^(59590|59509|59599)', '5959', regex=True)

    # Asegurarnos de agregar el prefijo 595 solo si no está presente
    df['celular'] = df['celular'].apply(lambda x: '595' + x if not x.startswith('595') else x)

    # Codificar el mensaje
    df['Mensaje_Codificado'] = quote(mensaje_unificado)

    # Crear enlace de WhatsApp
    df['Enlace_WhatsApp'] = df.apply(
        lambda row: f"https://web.whatsapp.com/send/?phone={row['celular']}&text={row['Mensaje_Codificado']}", axis=1)

    # Seleccionar solo la columna de enlaces
    df = df[['Enlace_WhatsApp']]

    # Obtener el directorio home del usuario
    home_dir = os.path.expanduser("~")
    # Obtener la fecha actual en formato DD_MM_AAAA
    fecha_actual = datetime.now().strftime("%d_%m_%Y")

    # Establecer el nombre por defecto del archivo
    nombre_por_defecto = f"enlaces_whatsapp_{fecha_actual}.csv"

    # Solicitar la ubicación para guardar el archivo
    archivo_guardar = filedialog.asksaveasfilename(
        initialdir=home_dir,  # Directorio inicial por defecto (home)
        title="Guardar archivo",
        initialfile=nombre_por_defecto,  # Nombre por defecto del archivo
        filetypes=[("CSV files", "*.csv"), ("Todos los archivos", "*.*")],
        defaultextension=".csv"  # Establecer una extensión por defecto
    )

    if archivo_guardar:  # Si el usuario seleccionó una ubicación y nombre de archivo
        print(f"Archivo guardado en: {archivo_guardar}")
    else:
        print("No se seleccionó ninguna ubicación para guardar el archivo.")
        return

    # Guardar el resultado en el archivo seleccionado
    df.to_csv(archivo_guardar, index=False)
    print(f"Archivo generado: {archivo_guardar}")
    # Mostrar mensaje de éxito

    try:
        messagebox.showinfo("Éxito", "El archivo se generó correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Crear la ventana
root = tk.Tk()
root.title("Generador de Enlaces")
root.geometry("500x350")
root.resizable(False, False)  # Bloquear el tamaño de la ventana

# Mensaje
label_mensaje = tk.Label(root, text="Mensaje")
label_mensaje.pack(pady=5)
entry_mensaje = tk.Text(root, height=5, width=60)  # Más grande y multilínea
entry_mensaje.pack(pady=5)
# Crear barras de desplazamiento (scrollbars) vertical y horizontal
scrollbar_vertical = tk.Scrollbar(root, command=entry_mensaje.yview)
scrollbar_horizontal = tk.Scrollbar(root, command=entry_mensaje.xview, orient=tk.HORIZONTAL)

# Configurar las barras de desplazamiento
entry_mensaje.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

# Empaquetar las scrollbars y el Text
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
# scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
entry_mensaje.pack(pady=5)

# Botón para subir archivo CSV
label_archivo = tk.Label(root, text="Subir archivo CSV numero")
label_archivo.pack(pady=5)
button_archivo = tk.Button(root, text="Seleccionar archivo", command=subir_archivo)
button_archivo.pack()

# Variable para el nombre del archivo
nombre_archivo = tk.StringVar(root)

# Etiqueta para mostrar el nombre del archivo subido
label_nombre_archivo = tk.Label(root, textvariable=nombre_archivo)
label_nombre_archivo.pack(pady=5)

# Variable para el checkbutton
archivo_cargado = tk.BooleanVar(root)
# Variable para mostrar el mensaje de carga del archivo
mensaje = tk.StringVar(root)

# Checkbutton para indicar si el archivo se cargó correctamente
check_archivo_cargado = tk.Checkbutton(root, text="Archivo NO cargado", variable=archivo_cargado, state="disabled")
check_archivo_cargado.pack()

# Botón para generar enlaces
button_generar = tk.Button(root, text="Generar enlaces", command=generar_enlaces, state="disabled")
button_generar.pack(pady=10)

# Cargar la imagen del logo de GitHub
github_logo = Image.open("github_logo.png")  # Asegúrate de tener este archivo en el mismo directorio
github_logo = github_logo.resize((40, 40), Image.Resampling.LANCZOS)  # Usar el nuevo método de resampling
github_logo_tk = ImageTk.PhotoImage(github_logo)

# Crear el botón con el logo de GitHub
button_github = tk.Button(root, image=github_logo_tk, command=abrir_github, relief="flat")
button_github.place(x=460, y=310)  # Coloca el botón en la esquina inferior derecha


# Ejecutar la ventana
root.mainloop()