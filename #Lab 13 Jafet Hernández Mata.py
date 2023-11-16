import tkinter as tk
from tkinter import filedialog

laberinto = []  # Variable global para el laberinto
i, j = 0, 0  # Variables para rastrear la posición del cuadro rojo en el laberinto
marco_lab = None  # Variable para el marco donde se muestra el laberinto
etiquetas = []  # Almacenar etiquetas para actualizarlas posteriormente
movimiento_automatico = False  # Controla si el movimiento es automático

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

    mostrar_laberinto()

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

    if movimiento_automatico:  # Si el movimiento es automático, continua moviendo
        ventana.after(5000, mover_cuadro_automatico)

def mover_cuadro_automatico():
    mover_cuadro()

    if movimiento_automatico:  # Si el movimiento es automático, continua moviendo
        ventana.after(500, mover_cuadro_automatico)

def toggle_movimiento_automatico():
    global movimiento_automatico
    movimiento_automatico = not movimiento_automatico
    if movimiento_automatico:
        mover_cuadro_automatico()

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        leer_laberinto(ruta_archivo)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Laberinto")

    marco_lab = tk.Frame(ventana)
    marco_lab.grid(row=1, column=0)  # Colocar el marco debajo del botón

    boton_seleccionar = tk.Button(ventana, text="Abrir archivo", command=seleccionar_archivo)
    boton_seleccionar.grid(row=0, column=0, pady=5)

    boton_mover = tk.Button(ventana, text="Mover", command=mover_cuadro)
    boton_mover.grid(row=0, column=1, padx=5)

    boton_automatico = tk.Button(ventana, text="Reproducir", command=toggle_movimiento_automatico)
    boton_automatico.grid(row=0, column=2, padx=5)

    ventana.geometry("800x800")
    ventana.mainloop()
