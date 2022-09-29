from tkinter import *
from shutil import disk_usage

class Sizer(Frame):

    @classmethod
    def main(cls):
        NoDefaultRoot()
        root = Tk()
        root.geometry('{}x{}'.format(200, 100))
        root.resizable(False, False)
        root.title('Drive Information')
        widget = cls(root)
        widget.grid(row=0, column=0, sticky=NSEW)
        root.mainloop()

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.selection = StringVar(self)
        self.menu = OptionMenu(self, self.selection, 'D:\\', 'E:\\', 'F:\\')
        self.menu.grid(row=0, column=0, sticky=NSEW)
        self.button = Button(self, text='Scan the drive', command=self.scan)
        self.button.grid(row=1, column=0, sticky=NSEW)
        self.display = Label(self)
        self.display.grid(row=2, column=0, sticky=NSEW)

    def scan(self):
        disk = self.selection.get()
        try:
            information = disk_usage(disk)
        except FileNotFoundError:
            self.display['text'] = 'Disk {!r} cound not be found'.format(disk)
        else:
            self.display['text'] = 'Used: {}\nFree: {}'.format(
                information.used, information.free)

if __name__ == '__main__':
    Sizer.main()