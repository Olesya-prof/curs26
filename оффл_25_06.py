import tkinter as tk
from tkinter import *
import os
#
# count = 0
# def change_label():
#     l.config (text=f'Кнопка меняет кнопку:')
#
# def change_sum():
#     global count
#     count += 1
#     l.config (text=f'Кнопка меняет кнопку: {count} раз')
#
# def change_sub():
#     global count
#     count -=1
#     l.config (text=f'Кнопка меняет кнопку: {count} раз')
#
# def print_text():
#     result = e.get()
#     l1.config(text=result)
#     print(result)
#
#
# win = Tk()
# win.geometry ('800x400')
# win.title ('Моя первая программа')
#
# center = tk.Frame (win)
# center.pack()
#
# fr1 = tk.Frame (center)
# fr1.pack(side='left')
#
# fr2 = tk.Frame (center)
# fr2.pack(side='right')
#
#
# l = tk.Label (fr1,text="Моя первая метка", bg='Lightblue', fg='Darkblue', width=50, height=3)
# l.pack(pady=10)
# l1 = tk.Label(fr1,text="Моя вторая метка", bg='Lightblue', fg='Darkblue', width=50, height=3)
# l1.pack (pady=10)
# l2 = tk.Label(fr1,text="Моя третья метка", bg='Lightblue', fg='Darkblue', width=50, height=3)
# l2.pack(pady=10)
#
# b = tk.Button (fr2, text='Нажми меня!', command=change_label)
# b.pack(pady=10)
# b1 = tk.Button (fr2, text='+1',command=change_sum )
# b1.pack (pady=10)
# b2 = tk.Button (fr2,text='-1', command=change_sub )
# b2.pack (pady=10)
#
# e = tk.Entry (fr2, width=30)
# e.pack()
#
# b3 = tk.Button (fr2,text='Текст в консоль', command=print_text)
# b3.pack (pady=10)
#
def int_res():
    name = e.get()
    age_str = e1.get() #Сначала получаем текст
    age = int(age_str)  #Сразу преобразуем в число
#логика определений слова с учётом исключений 11-14
    last_two = age % 100
    last_one = age % 10

    if 11 <= last_two <= 14:
        word = 'лет'
    elif last_one == 1:
        word = 'год'
    elif 2 <= last_one <= 4:
        word = 'года'
    else:
        word = 'лет'

    l_result.config(text=f'Привет{name}!Тебе {age} {word} ')


win = Tk()
win.geometry('600x500')
win.title('Анкета')

m = tk.Label(win,text="Имя:", font=('Arial 15'))
m.pack (pady=10)
e = Entry(width=30)
e.pack ()
m1 = tk.Label (win,text='Возраст',font=('Arial 15'))
m1.pack (pady=10)
e1 = Entry(width=30)
e1.pack (pady=10)
b = tk.Button (win, text='Показать', command=int_res)
b.pack(pady=10)

l_result = Label (text=' ')
l_result.pack ()

#
# def clean():
#     #txt.delete(1.0, tk.END)
#     print(txt.get(1.0, 1.5))
#
# def add_text():
#     txt.insert(tk.END, 'Hello,world!')# продолжаем содержимое поля
#
#
# win = Tk()
# win.title ('Text')
# win.geometry ('600x400')
#
# txt = tk.Text(win, width=40, height=5)
# txt.pack ()
#
# b = tk.Button (win, text='Очистить поле', command= clean)
# b.pack()
# b1 = tk.Button (win,text='Добавить текст', command= add_text)
# b1.pack()
# def get_symb():
#     item = e.get()
#     if item == '':
#         out_text .config (text=f'Ошибка.Введите имя')
#     else:
#         out_text .config (text=f'Привет,{item}')
#
#
#
# win = Tk()
# win.title('Приветcвие')
# win.geometry ('600x400')
#
# int_text = Label (text='')
# int_text.pack(pady=10)
#
# e = Entry()
# e.pack ()
#
# b = tk.Button (text='Приветствие',command= get_symb)
# b.pack (pady=10)
#
# out_text = Label (text='  ')
# out_text.pack()






win.mainloop()