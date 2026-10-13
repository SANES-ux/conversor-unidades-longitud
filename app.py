import tkinter as tk
from tkinter import messagebox

def on_click():
    # Mensaje por consola
    print("¡Alerta en consola: hola IA!")
    # Opcional: Alerta visual emergente
    messagebox.showinfo("Alerta", "hola IA")

def main():
    root = tk.Tk()
    root.title("Ejemplo Botón")
    root.geometry("300x150")

    label = tk.Label(root, text="Pulsa el botón para ver la alerta:")
    label.pack(pady=15)

    boton = tk.Button(root, text="Pulsar aquí", command=on_click, padx=10, pady=5)
    boton.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

