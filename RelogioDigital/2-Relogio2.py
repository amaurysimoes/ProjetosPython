# Exemplo de relógio digital
import tkinter
from time import strftime

clock = tkinter.Label()
clock.pack()
clock['font'] = 'Roboto 100 bold'
clock['text'] = strftime('%H:%M:%S')


def get_current_time():
    now = strftime('%H:%M:%S')
    if now != clock['text']:
        clock['text'] = now
    clock.after(100, get_current_time)


get_current_time()
clock.mainloop()
