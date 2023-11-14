import tkinter as tk
from tkinter import filedialog


def leer_laberinto(ruta):
    laberinto = []
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            # Elimina la coma adicional al final de cada línea y luego divide por comas
            fila = [int(x) for x in linea.strip().rstrip(',').split(',') if x]
            # Agregar la fila solo si tiene elementos
            if fila:
                laberinto.append(fila)
    return laberinto



def mostrar_laberinto(ventana, laberinto):
    for fila in range(len(laberinto)):
        for col in range(len(laberinto[0])):
            if laberinto[fila][col] == 1:
                color = "white"
            else:
                color = "black"
            etiqueta = tk.Label(ventana, text="", width=2, height=1, bg=color)
            etiqueta.grid(row=fila, column=col)

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        laberinto = leer_laberinto(ruta_archivo)
        mostrar_laberinto(ventana, laberinto)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Laberinto")

    boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
    boton_seleccionar.pack(pady=10)

    ventana.mainloop()
