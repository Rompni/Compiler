from tkinter import *
from tkinter import filedialog, messagebox

from Rparser import parser, ERROR


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
        menubar.add_cascade(label="Compilar", command=self.compilar)
        self.root.config(menu=menubar)

        # Editor de texto
        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH)

        # barra de desplazamiento
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        self.ruta = "none"
        # ventanirris
        self.root.mainloop()

    def guardar(self):
        if (self.ruta != "none"):
            f = open(self.ruta, 'w')
            f.write(self.text.get("1.0", END))
            f.close()
        else:
            self.ruta = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                     filetypes=(("Rompni files", "*.romp"), ("all files", "*.*")))
            aux = self.ruta + ".romp"
            f = open(aux, 'w')
            f.write(self.text.get("1.0", END))
            f.close()

    def abrir(self):
        self.text.delete("1.0", END)
        self.ruta = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Rompni files", "*.romp"), ("all files", "*.*")))
        f = open(self.ruta, 'r')
        data = f.read()
        self.text.insert(INSERT, data)
        f.close()

    def compilar(self):
        datos = self.text.get("1.0", END)
        parser.ERROR = 1
        try:
            #print(datos)
            print(self.text.get("1.0", END))
            parser.parse(datos, tracking=True)
            print('[ok]')
            messagebox.showinfo(message="Compilado", title="resultado")
        except:
            print('[error]')
            messagebox.showerror(message="error sintaxis", title="resultado")
        pass

    def sobre(self):
        root = Tk()
        root.wm_title("Sobre")
        texto = "PyRompniNotePad: Version 1.0"
        textONlabel = Label(root, text=texto)
        textONlabel.pack()


# Iniciar
PyRompniNotePad()
