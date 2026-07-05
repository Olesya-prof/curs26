from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg
import time

import winsound


def start():
    global alarm_time
    alarm_time = alarm.get().strip() #считываем символы из виджета Entry alarm
    messagebox.showinfo('Предупреждение', f'Будильник установлен на {alarm_time}')


def stop():
    global alarm_time
    alarm_time = ''
    alarm.delete(0, END )
    pg.mixer.music.stop()
    messagebox.showinfo('Предупреждение', 'Будильник отключен')


def tick():
    global alarm_time
    curr_time = strftime('%H:%M:%S') # подучаем текущее время в строковом ффформате
    if alarm_time == curr_time or alarm_time == strftime('%H:%M') or alarm_time == strftime('%H')  :
        alarm_time = ''
        pg.mixer.music.play()

    current_time.config(text=curr_time)  # меняем значение Label на текущее время
    current_time.after(1000, tick)  # вызов tick    один раз в секунду


pg.mixer.init()
pg.mixer.music.load('music.mp3') #загрузка мелодии
pg.mixer.music.set_volume(.5) #установил громкость

root = Tk()
WIDTH = root.winfo_screenwidth()# получаем ширину монитора в пикселях
HEIGHT = root.winfo_screenheight()# получаем высоту монитора в пикселях
#print(WIDTH,HEIGHT)
X = 400 #задаём ширину окна root
Y = 230  #задаём высоту окна root
#root.geometry ('450x250+400+200')
root.geometry (f'{X}x{Y}+{WIDTH // 2 - X // 2}+'
               f'{HEIGHT // 2 - Y // 2 - 20}')
#адаптивное размещение окна в центре экрана на любом мониторе

root.title ('Будильник')
root.config(bg = 'black')

current_time = Label(root, text='00:00:00')
current_time.config(font=('Arial',50),fg='lime',bg='black') #размер цифр.цвет
current_time.pack () # LEFT, RIGHT, BOTTOM, TOP

alarm = Entry(root)
alarm.config(width=10, justify= 'center', font=('Arial', 20))
alarm.pack()

start_btn = Button(root)
start_btn.config(width=10, text='Включить', justify='center',font=('Arial', 10),command=start)
start_btn.pack(pady=10)

stop_btn = Button(root)
stop_btn.config(width=10, text='Выключить', justify='center',font=('Arial', 10),command=stop)
stop_btn.pack()
alarm_time = ''

tick()

root.mainloop()