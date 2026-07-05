from tkinter import *

# window = Tk()
# privet = Label(text='Привет!')
# privet.pack()
#
# metka = Label(text='Привет всем!', bg='yellow')
# metka.pack()
# #
# privet = Label(text='Привет всем!', bg='Pink', fg='MediumVioletRed',
#                width=30, height=3)
# privet.pack()
# window = Tk()
#
# def change():
#     metka['text'] = 'Чёрная метка!'
#     metka['bg'] = 'black'
#     metka['fg'] = 'white'
# #
# #
# metka = Label(text='Привет, Россия!',bg='Lavender', fg='Indigo',
#                width= 15, height= 5)
# metka.pack()
# knopka = Button(text='Изменить метку', width= 15, height= 3)
# knopka.config(command= change)
# knopka.pack()
# knopka = Button(text= 'Изменить метку', width= 15, height= 3)

#Проект 'Инкремент'
# a = 0
#
# def change():
#     global a
#     a+=1
#     metka['text'] = str(a)
#
# window = Tk()
# metka = Label(text= '0',bg='Pink', fg='MediumVioletRed',
#             width= 30, height= 3)
# metka.pack()
# knopka = Button(text='Инкремент',width= 15, height= 3)
# knopka.config(command=change)
# knopka.pack()

# a = 100
#
# def change():
#     global a
#     a-=1
#     metka['text'] = str(a)
#
# window = Tk()
# metka = Label(text='100', bg='Pink', fg='MediumVioletRed',
#               width= 30, height= 3)
# metka.pack ()
# knopka = Button (text= 'Декремент', width= 15, height= 3)
# knopka .config (command= change)
# knopka .pack()

# a = 128512 # Смайлики
#
# def change():
#     global a
#     a+=1
#     metka ['text'] = chr(a)
#
# window = Tk()
# metka = Label (text = chr(a), font='Arial 64')
# metka .pack ()
# knopka = Button (text= 'Следующий', font='Arial 14' )
# knopka .config (command= change)
# knopka .pack ()

# window = Tk() #Размещаем метки с помощью  Pack сверху вниз по умолчанию
# metka1 = Label (text= 'Метка 1', bg='red')
# metka1 .pack()
# metka2 = Label (text= 'Метка 2', bg='yellow')
# metka2 .pack()
# metka3 = Label (text= 'Метка 3', bg='lightgreen')
# metka3 .pack()

# window = Tk() #размещаем метки справа налев
# metka1 = Label (text= 'Метка 1', bg='red')
# metka1 .pack (side=RIGHT )
# metka2 = Label (text= 'Метка 2', bg='yellow')
# metka2 .pack (side=RIGHT )
# metka3 = Label (text= 'Метка 3', bg='lightgreen')
# metka3 .pack (side=RIGHT )
#
#
# window = Tk() #размещаем метки слева направо
# metka1 = Label (text= 'Метка 1', bg='red')
# metka1 .pack (side=LEFT  )
# metka2 = Label (text= 'Метка 2', bg='yellow')
# metka2 .pack (side=LEFT  )
# metka3 = Label (text= 'Метка 3', bg='lightgreen')
# metka3 .pack (side=LEFT  )

# window = Tk() #размещаем метки снизу вверх
# metka1 = Label (text= 'Метка 1', bg='red')
# metka1 .pack (side=BOTTOM   )
# metka2 = Label (text= 'Метка 2', bg='yellow')
# metka2 .pack (side=BOTTOM  )
# metka3 = Label (text= 'Метка 3', bg='lightgreen')
# metka3 .pack (side=BOTTOM  )
# window = Tk()

# metka1 = Label (text= 'Метка 1', bg='red')
# metka1.pack(side=TOP)
# metka2 = Label (text= 'Метка 2', bg='yellow')
# metka2.pack(side=LEFT)
# metka3 = Label (text= 'Метка 3', bg='lightgreen')
# metka3.pack(side=RIGHT)
# metka4 = Label (text='Метка 4', bg='brown')
# metka4.pack(side=BOTTOM)
#
# window = Tk()
# frame_top = Frame(window )
# frame_bottom = Frame (window )
# frame_top .pack ()
# frame_bottom .pack ()
#
# metka1 = Label (frame_top , text='Метка 1', bg='red')
# metka1 .pack (side= LEFT )
# metka2= Label (frame_top , text='Метка 2', bg='yellow')
# metka2 .pack (side= LEFT )
# metka3 = Label (frame_top , text='Метка 3', bg='Lightgreen')
# metka3 .pack (side= LEFT )
# metka4 = Label (frame_bottom , text='Метка 4', bg='Lightblue')
# metka4 .pack (side= RIGHT )
# metka5 = Label (frame_bottom , text='Метка 5', bg='pink')
# metka5 .pack (side= RIGHT )
# metka6 = Label (frame_bottom , text='Метка 6', bg='magenta')
# metka6 .pack (side= RIGHT )

# def read():
#     Name = e.get()
#     print(Name )
#
#
# window = Tk()
# m = Label (text='Введите имя', bg='gray', font='Courier 16')
# m.pack (side= LEFT )
# e = Entry(width= 20, justify= 'center', bg='gray', fg='white',
#           font='Courier 18 bold')
# e.pack (side= LEFT)
# b =Button (text= 'Ввод', bg='gray', font='Courier 12', command= read)
# b.pack (side=LEFT)

# def read_name():  #получаем введённый тек
#     Name = e.get()
#     print(Name)  # выводим введённый текст
#
# def read_city():
#     City = e2.get()
#     print(City)
#
# window = Tk()
# f1 = Frame ()
# f2 = Frame ()
# f1.pack ()
# f2.pack ()
# m = Label (f1, text='Введите имя : ', bg='gray', font='Courier 16')
# m.pack(side=LEFT)
# e = Entry (f1, width= 20, justify='left', bg='gray',fg='brown',
#            font= 'Courier 18 bold')
# e.pack (side= LEFT)
# b = Button (f1, text='Ввод', bg='gray', font='Courier 12 bold', command= read_name)
# b.pack ()
#
# m2 = Label (f2,text='Введите город : ', bg='gray', font='Courier 16')
# m2.pack(side=LEFT)
# e2 = Entry (f2, width= 20, justify='left', bg='gray',fg='brown',
#            font= 'Courier 18 bold')
# e2.pack (side= LEFT )
# b2 = Button (f2, text='Ввод', bg='gray', font='Courier 12 bold', command= read_city)
# b2.pack ()

def read():
    T = text.get(1.3, 1.7)
    print(T)

def delete():
    text.delete(1.0, END)

def insert():
    pushkin = 'Это текстовое поле можно очистить с помощью кнопки.'
    text.insert(1.0, pushkin)
    # T = text.insert(1.0, pushkin)
    # print(T)


window = Tk()
text = Text(width= 30, height= 8,bg='black',fg='white', wrap=WORD)
text.pack (side= LEFT )
scroll = Scrollbar (command= text.yview)
scroll.pack (side=LEFT , fill=Y)
text.config (yscrollcommand= scroll.set)
b1 = Button(text='Вставка текста', command=insert)
b1.pack (side= LEFT )
b2 = Button(text='Удаление текста', command= delete)
b2.pack(side= LEFT )












window.mainloop()
