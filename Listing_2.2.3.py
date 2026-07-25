from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox
# def quit():
#     window.destroy()
#
# def open_image():
#     try:
#         file = fd.askopenfilename()
#         if file: # Проверяем,был ли выбран файл
#             img = Image.open(file)
#             imgconv = img
#
#             # Адаптируем размер изображения под размер окна
#             window_width = 500
#             window_height = 500
#             img.thumbnail(( window_width , window_height ))
#
#             imgtk = ImageTk.PhotoImage (img)
#
#             # Обновляем изображение на ветке
#             l.configure(image=imgtk)
#             l.image = imgtk # Сохраняем ссылку на изображение
#
# def open_image():
#     try:
#         file = fd.askopenfilename()
#         if file:  # Проверяем,был ли выбран файл
#             img = Image.open(file)
#
#             window_width = 500
#             window_height = 500
#             img.thumbnail((window_width, window_height))
#             imgtk = ImageTk.PhotoImage(img)
#             img_window = Toplevel (window)
#             img_window.title('Просмотр изображения')
#             l = Label(img_window , image= imgtk )
#             l.pack()
#             l.image = imgtk
#
#
#     except FileNotFoundError :
#         messagebox. showerror('Ошибка', 'Файл не найден')
#     except OSError :
#         messagebox.showerror('Ошибка', 'Не удалось открыть файл,возможно-это не изображение')
#     except Exception as e:
#         messagebox.showerror('Ошибка', f'Произошла ошибка: {e}')
#
#
# window = Tk()
# window.title('PHOTO')
# window.geometry ('500x500')
# # Создаем метку для изображения
# # l = Label (window ) #здесь удаляем создание метки
# # l.pack()
#
# mainmenu = Menu(window )
# window.config (menu= mainmenu )
#
# filemenu = Menu (mainmenu, tearoff= 0)
# filemenu.add_command(label= 'Открыть...', command= open_image)
# filemenu.add_separator()
# filemenu.add_command(label= 'Выход', command= window.quit)
# mainmenu.add_cascade(label= 'Файл',menu= filemenu )

#
#
# def open_image():
#     try:
#         file = fd.askopenfilename()
#         if file:
#             img = Image.open(file)
#
#             width = int(ws.get())
#             height = int(hs.get())
#             img.thumbnail((width , height ))
#             img_window = Toplevel (window)
#             img_window.title('Просмотр изображения')
#             imgtk = ImageTk.PhotoImage(img)
#             img_Label = Label(img_window , image= imgtk)
#             img_Label.image = imgtk # Сохраняем ссылку на изображение
#             img_Label.pack()
#
#     except FileNotFoundError :
#         messagebox. showerror('Ошибка', 'Файл не найден')
#     except OSError :
#         messagebox.showerror('Ошибка', 'Не удалось открыть файл,возможно-это не изображение')
#     except Exception as e:
#         messagebox.showerror('Ошибка', f'Произошла ошибка: {e}')
#
#
# window = Tk()
# window.title ('PHOTO')
# window.geometry ('500x500')
#
# Label (window , text='Ширина окна:').pack()
# ws = Spinbox (window , from_=100, to=500, increment= 100)
# ws.pack()
#
# Label (window ,text='Высота окна:').pack()
# hs = Spinbox (window , from_=100, to=500, increment= 100)
# hs.pack()
#
# mainmenu = Menu(window )
# window.config (menu= mainmenu )
#
# filemenu = Menu (mainmenu, tearoff= 0)
# filemenu.add_command(label= 'Открыть...', command= open_image)
# filemenu.add_separator()
# filemenu.add_command(label= 'Выход', command= window.quit)
# mainmenu.add_cascade(label= 'Файл',menu= filemenu )
#
# def draw_circle():
#     color = color_var.get()
#     canvas.create_oval(50, 50, 150, 150, outline=color, fill=color)
#
# def draw_triangle():
#     color = color_var.get()
#     canvas.create_polygon(50, 150, 100, 50, 150, 150, outline= color, fill= color)
#
#
# def draw_square():
#     color = color_var.get()
#     canvas.create_rectangle(50, 50,150, 150, outline=color, fill=color)
#
#
# def clear_canvas():
#     canvas.delete('all')
#
# window = Tk()
# window.title ('Рисование фигур')
# window.geometry ('400x500')
#
# canvas = Canvas (window, width=300, height=200)
# canvas.pack()
#
# color_var = StringVar (value= 'blue')
#
# circle_button = Button (window, text='Окружность', command=draw_circle)
# circle_button.pack(pady= 10)
#
# triangle_button = Button (window, text='Треугольник', command= draw_triangle)
# triangle_button.pack(pady= 10)
#
# square_button = Button (window, text='Квадрат', command=draw_square)
# square_button.pack(pady= 10)
#
# clear_button = Button (window, text='Очистить', command=clear_canvas)
# clear_button.pack(pady= 10)
#
# blue_radio = Radiobutton (window, text='Синий', variable=color_var, value='blue')
# blue_radio.pack(anchor=W)
#
# red_radio = Radiobutton (window, text='Красный', variable=color_var, value='red' )
# red_radio.pack(anchor=W)
#
# black_radio = Radiobutton (window, text='Чёрный', variable=color_var, value='black')
# black_radio.pack(anchor=W)

def draw_circle():
    fill_color = fill_color_entry.get()
    outline_color = outline_color_entry.get()
    canvas.create_oval(50, 50, 150, 150, outline= outline_color, fill= fill_color)

def draw_triangle():
    fill_color = fill_color_entry.get()
    outline_color = outline_color_entry.get()
    canvas.create_polygon(50, 150, 100, 50, 150, 150, outline= outline_color, fill= fill_color)

def draw_square():
    fill_color = fill_color_entry.get()
    outline_color = outline_color_entry.get()
    canvas.create_rectangle(50, 50, 150, 150, outline= outline_color, fill= fill_color)


def clear_canvas():
    canvas.delete('all')

window = Tk()
window.title ('Риование фигур')
window.geometry ('400x500')

canvas = Canvas (window, width=300, height=200)
canvas.pack()

# Метка и поле ввода цвета заливки
Label (window, text='Цвет заливки:' ).pack()
fill_color_entry = Entry(window )
fill_color_entry.pack(pady= 5)
fill_color_entry.insert(0, 'red')

# Метка и поле для ввода цвета обводки
Label (window, text='Цвет обводки:' ).pack()
outline_color_entry = Entry(window )
outline_color_entry.pack(pady= 5)
outline_color_entry.insert(0, 'black')

circle_button = Button (window, text='Окружность', command= draw_circle)
circle_button.pack(pady= 10)

triangle_button = Button (window, text='Треугольник', command=draw_triangle)
triangle_button.pack(pady= 10)

square_button = Button (window, text='Квадрат', command= draw_square)
square_button.pack(pady= 10)

clear_button = Button (window, text='Очистить', command= clear_canvas)
clear_button.pack(pady= 10)
# Поле для ввода цвета
# color_entry = Entry(window )
# color_entry.pack(pady= 10)
# color_entry.insert(0, 'blue') # Устанавливаем начальный цвет



window.mainloop()