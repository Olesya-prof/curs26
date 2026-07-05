from tkinter import *
import time
import tkinterweb

# window = Tk() # просмотр сайта гугл
# frame = tkinterweb.HtmlFrame(window)
# frame.load_website('https://www.google.com')
# frame.pack(fill='both', expand=1)


# def read():
#     Site = e.get()
#     frame.load_website(Site)
#
# window = Tk()
# m = Label (text='Введите адрес сайта:')
# m.pack()
# e = Entry (width=20, justify='left')
# e.pack ()
# b = Button (text='Ввод', command= read)
# b.pack ()
# frame = tkinterweb.HtmlFrame(window)
# frame.pack(fill='both', expand=1)

# def read():
#     Site = e.get()
#     frame.load_website(Site)
#
# window = Tk()
# f = Frame(window )
# f.pack ()
# m = Label (text='Введите адрес сайта:')
# m.pack(side= LEFT )
# e = Entry (width=20, justify='left')
# e.pack (side= LEFT )
# b = Button (text='Ввод', command= read)
# b.pack (side= LEFT )
# frame = tkinterweb.HtmlFrame(window)
# frame.pack(fill='both', expand=1)

# window = Tk() # выводим дату и время
# # time = time.strftime('%c')
# time = time.strftime('%d %B %Y')
# m = Label (font='Verdana 24 bold')
# m.pack()
# m.config (text=time)
window = Tk()
Month = time.strftime('%B')
Year = time.strftime('%Y')
match Month:
    case 'January':
        Month = 'Янаварь'
    case 'February':
        Month = 'Фувраль'
    case 'March':
        Month = 'Март'
m = Label(font='Verdana 24 bold')
m.pack ()
m.config(text=Month + ' ' + Year)





window.mainloop()