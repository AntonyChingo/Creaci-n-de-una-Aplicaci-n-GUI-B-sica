import tkinter as tk

class AplicacionGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación GUI Básica")

        self.etiqueta = tk.Label(ventana, text="Ingrese información:")
        self.etiqueta.pack()

        self.campo_texto = tk.Entry(ventana)
        self.campo_texto.pack()

        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar_informacion)
        self.boton_agregar.pack()

        self.lista = tk.Listbox(ventana)
        self.lista.pack()

        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_lista)
        self.boton_limpiar.pack()

    def agregar_informacion(self):
        informacion = self.campo_texto.get()
        if informacion:
            self.lista.insert(tk.END, informacion)

    def limpiar_lista(self):
        self.lista.delete(0, tk.END)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = AplicacionGUI(ventana_principal)
    ventana_principal.mainloop()
