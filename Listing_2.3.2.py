# Клавиатурный тренажёр
from tkinter import *
import time
from tkinter import messagebox as mb
from tkinter import filedialog as fd
#
# def check(event):
#     global i
#     if event.char == phrase[i]:
#         i += 1
#         label.config (text=phrase[i])
#     else:
#         label.config (text=f'Ошибка! Ожидалась буква "{phrase[i]}", \n нажмите любую клавишу для продолжения')
#         window.bind('<Key>', cont)
#
# def cont(event):
#     label.config(text=phrase[i])
#     window.bind('<Key>', check)
#
# phrase = 'quickbrowfax'
# i = 0
#
# window = Tk()
# window.title ('Клавиатурный тренажёр')
# window.geometry ('900x100')
#
 #label = Label (text=phrase[i], font=('Helvetica', 24))
# label.pack ()
# window.bind('<Key>', check)
#
# window.mainloop()
# def check(event):
#     global i, t
#     if event.char == phrase[i]: # сравниваем нажатую букву с текущей
#         i += 1                  # переходим к следующей букве
#         if i == len(phrase):   # если дошли до конца слова
#             elapsed = time.time()-t # вычисляем время
#             label.config(text=f'Ваше время: {elapsed:.2f}сек.')
#             window.unbind('<Key>')  # отключаем клавиши
#         else:
#             label.config (text=phrase[i]) #показываем следующую букву
#     else:
#         label.config (text=f'Ошибка! Ожидалась буква "{phrase[i]}", \n нажмите любую клавишу для продолжения')
#         window.bind('<Key>', cont) # переключаем обработчик на cont
#
# def cont(event):
#     global i
#     label.config(text=phrase[i]) # показываем ту же букву
#     window.bind('<Key>', check) # возвращаем обработчик на check
#
# phrase = 'quickbrowfax' # слово для ввода
# i = 0                   # счётчик текущей позиции
# t = time.time()         # запоминаем время старта
#
# window = Tk()
# window.title ('Клавиатурный тренажёр')
# window.geometry ('900x100')
#
# label = Label (text=phrase[i], font=('Helvetica', 24))  # показывает q
# label.pack ()
# window.bind('<Key>', check) # Привязываем клавищи к функции check
#
# window.mainloop()

# def check(event):
#     global i, t
#     if event.char == phrase[i]: # сравниваем нажатую букву с текущей
#         i += 1                  # переходим к следующей букве
#         if i == len(phrase):   # если дошли до конца слова
#             elapsed = time.time()-t # вычисляем время
#             time_allowed = len(phrase)
#             if elapsed <= time_allowed:
#                 label.config(text=f'Вы победили! Время: {elapsed:.2f}сек. Надо уложиться в {time_allowed}сек.')
#             else:
#                 label.config (text=f'Прошло {elapsed:.2f}сек. Надо уложиться в {time_allowed}сек.')
#         else:
#             label.config(text=phrase[i])
#     else:
#         label.config(text=f'Ошибка! Ожидалась буква "{phrase[i]}", \n нажмите любую клавишу для продолжения')
#         window.bind('<Key>', cont)  # переключаем обработчик на cont
#
# def cont(event):
#     global i
#     label.config(text=phrase[i]) # показываем ту же букву
#     window.bind('<Key>', check) # возвращаем обработчик на check
#
#
# phrase = 'quickbrowfax' # слово для ввода
# i = 0                   # счётчик текущей позиции
# t = time.time()         # запоминаем время старта
#
# window = Tk()
# window.title ('Клавиатурный тренажёр')
# window.geometry ('900x100')
#
# label = Label (window, text=phrase[i], font=('Helvetica', 24))  # показывает q
# label.pack ()
# window.bind('<Key>', check) # Привязываем клавищи к функции check
#
# window.mainloop()

# def start():
#     global t, i
#     i = 0  #сбрасывает позицию на начало
#     t = time.time()  #запоминаем время старта
#     label.config (text=phrase[i])  #показываем первую букву
#     window.bind('<KeyPress>', check)  #привязываем клавиши к проверке
#
# def check(event):
#     global i, t
#     if not event.char or not event.char.isalpha():
#         return
#     if event.char == phrase[i]: # сравниваем нажатую букву с текущей
#         i += 1                  # переходим к следующей букве
#         if i >= len(phrase): # если дошли до концы игры
#             finish()
#         else:
#             label.config(text=phrase[i])   #показываем следующую букву
#     else:
#         label.config(text=f'Ошибка! Ожидалась буква "{phrase[i]}", \n нажмите любую клавишу для продолжения')
#         window.bind('<Key>', cont)  # переключаем обработчик на cont на режим ожидания повторения
#
# def cont(event):
#     label.config(text=phrase[i])  # показываем ту же букву,правильную
#     window.bind('<Key>', check)  # возвращаем обработчик на check,на проверку
#
#
# def finish():
#     elapsed = time.time() - t
#     time_allowed = len (phrase)
#     if elapsed <= time_allowed :
#         res = f'Вы победили! Время: {elapsed:.2f}сек.'
#     else:
#         res = f'Время истекло! Затрачено {elapsed:.2f}сек. Разрешённое время: {time_allowed}сек.'
#
#     mb.showinfo('Результат', res)
#     if mb.askyesno('Повторить', 'Хотите попробовать ещё раз?'):
#         start()
#     else:
#         window.destroy()
#
# phrase = 'quickbrowfax' # слово для ввода
# i = 0
# t = None # Время начала,пока не установлено
#
# window = Tk()
# window.title ('Клавиатурный тренажёр')
# window.geometry ('900x100')
#
# label = Label (window, text=phrase[i], font=('Helvetica', 24))  # показывает q
# label.pack ()
#
# start() # автоматический запуск игры
# window.mainloop() #апускаем цикл обработки событий
# def load_phrase():
#     try:
#         with open('phrase.txt', 'r')as file:
#             return file.read().strip()
#     except FileNotFoundError :
#         mb.showerror('Ошибка', 'Файл с фразой не найден')
#         return 'quickbrownfox' # возвращаем фразу по умолчанию
#     phrase = load_phrase
# window = Tk()
#
def delete():
    text.delete(1.0, END)

def insert():
    try:
        file = fd.askopenfilename()
        if file: # проверяем выбран ли файл
            with open(file, 'r')as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError :
        mb.showerror('Ошибка', 'Файл не найден')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')

def save():
    try:
        file = fd.askopenfilename()
        filetypes = ('TXT files', '*.txt', 'HTML files', '*.html', '*.htm', 'ALL files', '*.*')
        if file:
            with open(file, 'w')as file:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Не удалось сохранить файл')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')

def quit():
    window.destroy()

window = Tk()
window.title('Текстовый редактор')
# Создание текстового поля
text = Text(window , width= 30, height= 8, bg='gray', wrap=WORD)
text.pack(side=LEFT)

# создание скроллбара
scroll = Scrollbar (window , command= text.yview)
scroll.pack(side=LEFT,fill=Y)
text.config (yscrollcommand= scroll.set)
 #создание меню
menu_bar = Menu(window)
window.config (menu= menu_bar)
 # создание подменю Файл
file_menu = Menu (menu_bar, tearoff= 0)
menu_bar.add_cascade(label= 'Файл', menu= file_menu )
file_menu.add_command(label= 'Открыть', command= insert)
file_menu.add_command(label= 'Сохранить', command= save)
file_menu.add_command(label= 'Удалить всё', command= delete)
file_menu.add_separator()
file_menu.add_command(label= 'Выход', command= quit )
window.mainloop()




