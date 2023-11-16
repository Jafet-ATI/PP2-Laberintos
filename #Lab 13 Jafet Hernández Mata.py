import tkinter as tk
from tkinter import filedialog

laberinto = []  # Variable global para el laberinto
i, j = 0, 0  # Variables para rastrear la posición del cuadro rojo en el laberinto
marco_lab = None  # Variable para el marco donde se muestra el laberinto
etiquetas = []  # Almacenar etiquetas para actualizarlas posteriormente

def seleccionar_archivo():
    global marco_lab
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        leer_laberinto(ruta_archivo)
        marco_lab = tk.Frame(ventana)
        marco_lab.grid(row=1, column=0)
        mostrar_laberinto()

def leer_laberinto(ruta):
    global laberinto
    laberinto = []
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            elementos = [x for x in linea.strip().rstrip(',').split(',') if x]

            if elementos:
                fila = []
                for elemento in elementos:
                    if elemento == 'E':
                        fila.append('E')
                    else:
                        fila.append(int(elemento))
                laberinto.append(fila)

    max_longitud = max(len(fila) for fila in laberinto)

    for fila in laberinto:
        while len(fila) < max_longitud:
            fila.append(0)

def mostrar_laberinto():
    global i, j, etiquetas
    for fila in range(len(laberinto)):
        for col in range(len(laberinto[0])):
            if col < len(laberinto[fila]):
                if laberinto[fila][col] == 'E':
                    color = "red"
                    i, j = fila, col  # Actualiza la posición inicial del cuadro rojo
                elif laberinto[fila][col] == 1:
                    color = "white"
                else:
                    color = "black"
                etiqueta = tk.Label(marco_lab, text="", width=6, height=3, bg=color)
                etiqueta.grid(row=fila, column=col)
                etiquetas.append(etiqueta)

def mover_cuadro():
    global i, j, etiquetas
    if j + 1 < len(laberinto[i]) and laberinto[i][j+1] == 1:
        etiquetas[i * len(laberinto[0]) + j]['bg'] = 'white'
        j += 1  # Mover a la derecha si hay un camino
        etiquetas[i * len(laberinto[0]) + j]['bg'] = 'red'
    elif i + 1 < len(laberinto) and laberinto[i+1][j] == 1:
        etiquetas[i * len(laberinto[0]) + j]['bg'] = 'white'
        i += 1  # Mover hacia abajo si hay un camino
        etiquetas[i * len(laberinto[0]) + j]['bg'] = 'red'

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Laberinto")

    boton_seleccionar = tk.Button(ventana, text="Abrir archivo", command=lambda: seleccionar_archivo())
    boton_seleccionar.grid(row=0, column=0, pady=5)

    boton_mover = tk.Button(ventana, text="Mover", command=mover_cuadro)
    boton_mover.grid(row=0, column=1, padx=5)

    ventana.geometry("800x800")
    ventana.mainloop()
