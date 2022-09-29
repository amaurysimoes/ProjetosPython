from tkinter import *
top = Frame() ; top.pack()
a = Label (top, text="A") ; a.pack (side="left")
b = Label (top, text="B") ; b.pack (side="bottom")
c = Label (top, text="C") ; c.pack (side="right")
d = Label (top, text="D") ; d.pack (side="top")
for widget in (a,b,c,d):
 widget.configure(relief="groove", border=2,
font="Times 24 bold")
top.mainloop()