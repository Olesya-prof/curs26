from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox as mb


def check():
    colors = ['зелёный', 'красный', 'жёлтый']
    computer = random.choice (colors)
    user = e.get().lower()
    if computer == user:
        mb.showinfo('Результат', 'Вы угадали')
    else:
        mb.showinfo ('Результат', f'Вы не угадали \n компьютер выбрал {computer}')

win = Tk()
win.geometry ('600x500')
win.title('Светофор')

m = tk.Label(win, text='Введите цвет светофора!', font='Arial 15')
m.pack (pady=10)

e = Entry(win, width= 30)
e.pack(pady=10)

b = tk.Button (win, text='Проверить', font='Arial 15', command= check)
b.pack(pady=10)

win.mainloop()