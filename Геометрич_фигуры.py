import time
import turtle
import math
from turtle import *
from math import sin,pi
# shape('turtle')
# colormode(255)
# speed(5)
# pensize(3)
# Шестиугольная спираль
# color('red')
# rt (60) #поворот направо на 60 градусов
# for i in range (6, 100, 6):   # i = 6, 12, 18...96,внешний цикл делает 16 шагов
#     fd(i)  #идти вперёд на i пикселей
#     rt(120)   #поворот направо на 120 градусов, на каждом шаге,что равно внешнему углу треугольника
# speed(10)
# colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan'] # разные цвета для каждого сегмента
#
# for i in range(6, 100, 6):
#     color(colors[i // 6 % len(colors)])
#     forward(i)
#     rt(120)
# speed(10)
# color('purple')
#
# for i in range(6, 100, 6):
#     forward(i)
#     rt(120 + i // 10)  # Угол постепенно увеличивается
#


# for i in range (6, 100, 12):
#     fd(i)
#     rt(120)
# for i in range (4, 80, 4):
#     fd(i)
#     rt(60)
# ht()
# pensize(4)
# color('blue')
# for i in range (4, 56, 4):
#     fd(i)
#     rt(90)
# for i in range (56, 4, -4):
#     fd(i)
#     rt(90)
# ht()
# pensize(4)
# color('blue')
# for i in range (4, 56, 4):
#     fd(i)
#     rt(90)
# rt(270)
# for i in range (52, 0, -4):
#     fd(i)
#     rt(90)

# r = 40
# pensize(5)
# color('#FFA500')
# for i in range (6):
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)
# r = 40
# pensize(10)
# color('#FFA500')
# fillcolor('#A200FF')
# for i in range (6):
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)
# r = 30
# for i in range (6):
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)
# r = 20
# for i in range (6):
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)
# r = 20
# for i in range (6):
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)
# r = 10
# for i in range (6):
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)

# pensize(4)
# color('#FFA500')
# fillcolor('#A200FF')
# for k in range (3):
#     r = 20
#     for j in range (4):
#         for i in range (6):
#             begin_fill()
#             circle(r)
#             end_fill()
#             rt(60)
#         r = r - 5
#     penup()
#     fd(80)
#     pendown()
#
# pensize(4)
# color('#FFA500')
# fillcolor('#A200FF')
# for k in range (3):
#     print('!_k = ' + str(k))
#     r = 20
#     for j in range (4):
#         print('_ j =' + str(j))
#         for i in range (6):
#             print('i = ' + str(i))
#             begin_fill()
#             circle(r)
#             end_fill()
#             rt(60)
#             time.sleep(1)
#         r = r - 5
#         print('Следующие 6')
#     penup()
#     fd(80)
#     pendown()
#     print('Цветок готов!')
# print(range (40, 0, -10))
# speed(0)
# r = 40
# pensize(10)
# color(255, 165, 0)
# fillcolor(162, 0, 255)
# for j in range (40, 0, -10):
#     for i in range (6):
#         begin_fill()
#         circle(j)
#         end_fill()
#         rt(60)
#     r = r - 10
# ht
# pensize(5)
# for r in range (40, 0, -10):
#     for i in range (6):
#         color(255, 165, r * 6)
#         fillcolor(162, r * 5, 255)
#         begin_fill()
#         circle(r)
#         end_fill()
#         rt(60)

# fd(100)
# lt(90)
# fd(100)
# lt(90)
# begin_fill()
# for _ in range(4): #диапазон
#     fd(100)
#     lt(90)
# end_fill()

# for i in range(4):  #цикл для квадрата
#     fd(100)
#     lt(90)
# Ugol = 3  #используем переменную количества углов
# for i in range (Ugol):
#     fd(100)
#     lt(360 / Ugol)
# Ugol = 5
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     lt(360 / Ugol)
# end_fill()
# Ugol = input('Введите количество углов')
# Ugol = int(Ugol)
# Color = input('Введите цвет на английском')
# color(Color)
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     lt(360 / Ugol)
# end_fill()
# Ugol = 5   #пятиугольная звезда первёрнутая
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     lt(360 * 2 / Ugol)
# end_fill()
# Ugol = 5   #пятиугольная звезда нормальная
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     rt (360 * 2 / Ugol)
# end_fill()
# Ugol = 7   #семиугольная звезда
# color('red')
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     rt (360 * 2 / Ugol)
# end_fill()
# Ugol = 7   # вторая семиугольная звезда
# color('red')
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     rt (360 * 3/ Ugol)
# end_fill()
# Ugol = 9   #девятиугольная звезда
# color('red')
# begin_fill()
# for i in range (Ugol):
#     fd(100)
#     rt (360 * 4 / Ugol)
# end_fill()
# for i in range (3): #три круга с помощью цикла
#     begin_fill()
#     color('coral')
#     circle(50)
#     end_fill()
#     penup()
#     fd(50)
#     pendown()
# for i in range (3): #добавляем поворот
#     begin_fill()
#     color('coral')
#     circle(50)
#     end_fill()
#     penup()
#     fd(50)
#     lt (120)
#     pendown()
# for i in range (4):
#     begin_fill()  # 4 круга
#     color('coral')
#     circle(20)
#     end_fill()
#     penup()
#     fd(50)
#     lt (90)
#     pendown()
colormode(255)
# for i in range (4): #используем переменную внутри цикла
#     begin_fill()
#     color(60 * i, 60 * i, 60 * i)
#     circle(20)
#     end_fill()
#     penup()
#     fd (50)
#     lt(90)
#     pendown()







mainloop()

