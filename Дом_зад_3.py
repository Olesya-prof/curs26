from tkinter import *


def get_sum():
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())
    result = n1 + n2 + n3
    num4.delete(0, END)  # Очищаем поле
    num4.insert(0, str(result)) # Вставляем результат


def get_multiply():
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())
    result = n1 * n2 * n3
    num4.delete(0, END)
    num4.insert(0, str(result))


root = Tk()
root.title ('Calculator')
root.geometry ('400x250')
metka = Label (text='Введите три числа и нажмите на кнопку для вычисления суммы')
metka.pack (pady=15)

frame = Frame (root )
frame.pack ()

num1 = Entry (frame, width=12, font=('Arial',15), justify='center')
num1.grid(row=0, column=0)

num2 = Entry (frame, width=12, font=('Arial',15), justify='center')
num2.grid(row=1, column=0)

num3 = Entry (frame, width=12, font=('Arial',15), justify='center')
num3.grid(row=2, column=0)

knopka1 = Button (frame, text='Сложить три числа',width=18, command=get_sum)
knopka1.grid (row=3,column=0,pady=2)

knopka2 = Button (frame, text='Умножить три числа',width=18, command=get_multiply)
knopka2.grid (row=4,column=0,pady=2)

num4 = Entry (frame, width=12, font=('Arial',15), justify='center')
num4.grid(row=5, column=0,pady=2)


root.mainloop()