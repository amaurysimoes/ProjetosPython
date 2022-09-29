from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text= "Teste de Aplicação")
        self.msg.pack()
        self.fechar = Button(self, text="Fechar", command=self.quit)
        self.fechar.pack()
        self.pack()

app = Application()
mainloop()