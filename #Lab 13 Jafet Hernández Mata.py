import tkinter as tk

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
                color = "blue"
            else:
                color = "red"
            etiqueta = tk.Label(ventana, text="", width=2, height=1, bg=color)
            etiqueta.grid(row=fila, column=col)

if __name__ == "__main__":
    ruta_archivo = 'C:/Users/jcia9/Escritorio/TEC/Algoritmos y estructuras de datos/laberinto.txt'  # Cambia esto con la ruta correcta de tu archivo
    laberinto = leer_laberinto(ruta_archivo)

    ventana = tk.Tk()
    ventana.title("Laberinto")

    mostrar_laberinto(ventana, laberinto)

    ventana.mainloop()
