from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import Rparser, Rlexer


class MainWindow:
    WIDTH = 700
    HEIGHT = 600

    def __init__(self):

        self.root = Tk()
        self.root.tk_setPalette(background='#0e1717', foreground='white',
                           activeBackground='#1c2f2f', activeForeground='white')
        self.root.resizable(0, 0)
        self.root.title('Rompni NotePad')
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        #self.root.iconbitmap('icono.ico')
        self.fileName = None

        # menu
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)
        self.file_dropdown = Menu(self.menuBar, tearoff=0)
        self.file_dropdown.add_command(label='New File', accelerator='Ctrl+N', command=self.newFile)
        self.file_dropdown.add_command(label='Open File', accelerator='Ctrl+O', command=self.openFile)
        self.file_dropdown.add_command(label='Save', accelerator='Ctrl+S', command=self.saveFile)
        self.file_dropdown.add_command(label='Save As', accelerator='Ctrl+Shitf+S', command=self.saveAsFile)
        self.file_dropdown.add_separator()
        self.file_dropdown.add_command(label='Exit', command=self.root.destroy)

        self.run_dropdown = Menu(self.menuBar, tearoff=0)
        self.run_dropdown.add_command(label='▶  Run', accelerator='Ctrl+R', command=self.compiler)

        self.menuBar.add_cascade(label='File', menu=self.file_dropdown)
        self.menuBar.add_cascade(label='Run', menu=self.run_dropdown)

        self.text = Text(self.root, selectbackground="#2F4F4F")

        self.scroll = Scrollbar(self.root, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set, font=("consolas", 11))
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll.pack(side=RIGHT, fill=Y)
        # status
        self.statusBar = StringVar()
        self.statusBar.set('Rompni NotePad - 0.1 Compiler')
        Label(self.text, textvariable=self.statusBar, fg='black', bg='lightgrey', anchor='sw').pack(side=BOTTOM,
                                                                                                    fill=BOTH)
        # atajos
        self.bind_shortCuts()

    def setWindowsTitle(self, name=None):
        if name:
            self.root.title(name + ' - Rompni NotePad')
        else:
            self.root.title('Rompni NotePad')

    def newFile(self, *args):
        self.text.delete(1.0, END)
        self.fileName = None
        self.setWindowsTitle()

    def openFile(self, *args):
        self.fileName = filedialog.askopenfilename(
            defaultextension='.romp',
            filetypes=[('text files', '*.romp*')]
        )
        if self.fileName:
            self.text.delete(1.0, END)
            with open(self.fileName, 'r') as f:
                self.text.insert(1.0, f.read())
                self.setWindowsTitle(self.fileName)

    def saveFile(self, *args):
        if self.fileName:
            try:
                textArea_content = self.text.get(1.0, END)
                with open(self.fileName, 'w') as f:
                    f.write(textArea_content)
                self.updateStatus(True)
            except Exception as e:
                print(e)
        else:
            self.saveAsFile()

    def saveAsFile(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile='Untlited.romp',
                defaultextension='.romp',
                filetypes=[('Text Files', '*.romp*')]
            )
            textArea_content = self.text.get(1.0, END)
            with open(new_file, 'w') as f:
                f.write(textArea_content)
            self.fileName = new_file
            self.setWindowsTitle(self.fileName)
            self.updateStatus(True)

        except Exception as e:
            print(e)

    def bind_shortCuts(self):
        self.text.bind('<Control-n>', self.newFile)
        self.text.bind('<Control-o>', self.openFile)
        self.text.bind('<Control-s>', self.saveFile)
        self.text.bind('<Control-S>', self.saveAsFile)
        self.text.bind('<Control-r>', self.compiler)
        self.text.bind('<Key>', self.updateStatus)

    def updateStatus(self, *args):
        if isinstance(args[0], bool):
            self.statusBar.set('Your File Has Been Saved!')
        else:
            self.statusBar.set('Rompni - 0.1 Compiler')

    def compiler(self, *args):
        data = self.text.get(1.0, END)
        print(data)
        Rparser.ERRORES = ""
        Rparser.variables = {}
        try:
            Rparser.parser.parse(data)
            print('[ok]')
            messagebox.showinfo(message="Compilado con exito", title="resultado")
        except:
            print('[error]')
            text = Rparser.ERRORES
            messagebox.showerror(message="Error de sintaxis, "+text, title="resultado")

    def run(self):
        self.root.mainloop()


windows = MainWindow()
windows.run()
