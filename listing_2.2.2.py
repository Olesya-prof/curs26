from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb

# window = Tk()
# l = Listbox(width=15, height=7)
# l.pack()
# l.insert(0, 'Понедельник')
# l.insert(1, 'Вторник')
# l.insert(2, 'Среда')
# l.insert(3, 'Четверг')
# l.insert(4, 'Пятница')
# l.insert(5, 'Суббота')
# l.insert(6, 'Воскресенье')
#
#
# l = Listbox (window, width= 15, height= 7)
# l.pack ()
#
# days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
# for day in days_of_week:
#     l.insert(END,day)

# def add_item():
#     l.insert(END, e.get())
#     e.delete(0, END)
#
#
# def del_item():
#     l.delete(ANCHOR)
#
#
# l = Listbox ()
# l.pack(side='left')
# f = Frame()
# f.pack(side='left')
# e = Entry(f)
# e.pack()
# b1 = Button(f, text='Add', command=add_item)
# b1.pack()
# b2 = Button (f, text='Delete', command=del_item)
# b2.pack()


#def add_item():
#     #print(s.get())
#     if s.get() == '0':
#         l1.insert(END,e.get())
#         e.delete(0, END)
#     else:
#         l2.insert(END, e.get())
#         e.delete(0, END)
#
# def del1_item():
#     l1.delete(ANCHOR)
#
# def del2_item():
#     l2.delete(ANCHOR)
#
# s = StringVar (value='0')
# f1 = Frame()
# f1.pack(side=LEFT)
# m1 = Label (f1, text='Имя')
# m1.pack()
# l1 = Listbox (f1)
# l1.pack()
#
# f2 = Frame()
# f2.pack(side=LEFT)
# m2 = Label (f2, text='Телефон')
# m2.pack()
# l2 = Listbox (f2)
# l2.pack()
#
# f3 = Frame()
# f3.pack(side=LEFT)
# radio1 = Radiobutton (f3, text='Имя',value=0, variable=s)
# radio1.pack()
# radio2 = Radiobutton (f3, text='Телефон', value=1,variable=s)
# radio2.pack()
# e = Entry(f3)
# e.pack()
# b1 = Button (f3,text='Add',command=add_item)
# b1.pack()
# b2 = Button (f3, text='Удалить имя', command=del1_item)
# b2.pack(fill=X)
# b3 = Button (f3, text='Удалить телефон', command=del2_item)
# b3.pack(fill=X)

def add_item():
    if s.get() == '0':
        #Добавление имени
        l1.insert(END, e.get())
        e.delete(0, END)
    else:
        # добавление номера после проверки
        if validate_phone():
            l2.insert(END, e.get())
            e.delete(0, END)

def del1_item():
    l1.delete(ANCHOR)

def del2_item():
    l2.delete(ANCHOR)

def save():
    try:
        with open ('phones.txt', 'w')as f:
            for i in range (l1.size()):
                f.write(f'{l1.get(i)} : {l2.get(i)}\n')
        mb.showinfo('Сохранение', 'Контакты успешно сохранены.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка при сохранении: {e}')


def load():
    try:
        with open ('phones.txt', 'r')as f:
            l1.delete(0, END) # Очищаем списки перед загрузкой
            l2.delete(0, END)
            for line in f:
                name, _, phone = line.partition(':')
                l1.insert(END, name.strip())
                l2.insert(END, phone.strip())

        mb.showinfo('Загрузка', 'Контакты успешно загружены.')
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка при загрузке: {e}')

def validate_phone():
    phone_number = e.get()
    if len(phone_number) == 10 and phone_number.isdigit() and phone_number.startswith('9') :
        # Проверка пройдена
        mb.showinfo('Операция выполнена', 'Номер успешно добавлен')
        return True
    else:
        # Проверка не пройдена
        mb.showerror('Ошибка', 'Номер должен быть 10-значным,состоять только из цифр и начинаться с 9')
        e.delete(0, END)
        return False

window = Tk()
s = StringVar (value=0)

f1 = Frame () # Имена
f1.pack (side=LEFT)
m1 = Label (f1, text='Имя')
m1.pack()
l1 = Listbox (f1)
l1.pack ()
scroll1 = Scrollbar (f1, command=l1.yview)
scroll1.pack (side=RIGHT , fill=Y )
l1.config (yscrollcommand=scroll1.set)

f2 = Frame () #Телефоны
f2.pack (side=LEFT)
m2 = Label (f2, text='Телефон')
m2.pack()
l2 = Listbox (f2)
l2.pack ()
scroll2 = Scrollbar (f2, command=l2.yview)
scroll2.pack (side=RIGHT , fill=Y )
l2.config (yscrollcommand=scroll2.set)

f3 = Frame () #Управление
f3.pack (side=LEFT)
radio1 = Radiobutton (f3, text='Имя', value= 0,variable= s)
radio1.pack ()
radio2 = Radiobutton (f3, text='Телефон', value= 1,variable= s)
radio2.pack ()
e = Entry(f3)
e.pack ()

b1 = Button(f3, text='Добавить', command= add_item)
b1.pack (fill=X)
b2 = Button(f3, text='Удалить имя', command= del1_item)
b2.pack (fill=X)
b3 = Button(f3, text='Удалить телефон', command= del2_item)
b3.pack (fill=X)
b4 = Button(f3, text='Сохранить', command=save)
b4.pack (fill=X)
b5 = Button(f3, text='Загрузить', command=load)
b5.pack (fill=X)





window.mainloop()