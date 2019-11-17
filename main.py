from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename


# Creo la clase editor
class PyRompniNotePad:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("PyRompniNotePad")

        # barra de navegacion
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)

        menubar = Menu(self.root)
        # Aquí indicamos los menus
        MENUarchivo = Menu(menubar)
        MENUarchivo.add_command(label="Guardar", command=self.guardar)
        MENUarchivo.add_command(label="Abrir", command=self.abrir)
        menubar.add_cascade(label="Archivo", menu=MENUarchivo)

        MENUayuda = Menu(menubar)
        MENUayuda.add_command(label="Sobre", command=self.sobre)
        menubar.add_cascade(label="Ayuda", menu=MENUayuda)
        menubar.add_cascade(label="Compilar")
        self.root.config(menu=menubar)

        # Editor de texto
        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH)

        # barra de desplazamiento
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        # ventanirris
        self.root.mainloop()

    def guardar(self):  # Guardar archivo
        fileName = asksaveasfilename()
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def abrir(self):  # Cargar archivo
        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, END)
            self.text.insert(0.0, contents)
        except:
            pass

    def sobre(self):
        root = Tk()
        root.wm_title("Sobre")
        texto = ("PyRompniNotePad: Version 1.0")
        textONlabel = Label(root, text=texto)
        textONlabel.pack()


# Iniciar
PyRompniNotePad()
