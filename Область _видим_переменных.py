# def summator(x, y):
# def summator(z, y):
#     global x
#     # x = 30
#     x += 10
#     print('x - function - ', x)
#
#
# x = 1000
# summator(10, 20)
# print('modul x -', x)

import time


# def is_even(n: int) -> bool:
#     # if n % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     # return n % 2 == 0
#     return not n % 2
#
# def choice_even(x, y):
#     for i in range(x, y + 1):
#         if is_even(i):
#             print(i, end=' ')
#
# print(is_even(6))
# choice_even(100, 140)
#
# def nums2(n):
#     if n > 1:
#         nums2(n - 1)
#     print(n)
#
#
# def nums1(n):
#     if n > 1:
#         nums2(n - 1)
#     print(n)
#
#
# def nums(n):  # рекурсия
#     if n > 1:
#         nums(n - 1)
#     print(n)
import time
#Факториал
# """
# 3! = 1 * 2 * 3 = 3 * 2!
# 2! = 1 * 2     = 2 * 1!
# 1! = 1
# n! = n * (n - 1)!
#
# # """
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))#120
# print(fact(6))#720
#
# """ 0 1 1 2 3 5 8 13 21 34 55 """ #ряд Фибоначи
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(5))#5
# print(fib(10))#55

# def name(nm):
#     cnt = 0
#     def surname(snm):
#         nonlocal cnt
#         cnt += 1
#         print(cnt, nm, snm)
#     return surname
# cnt = 1000
# zam = name('Mary')  # замыкание
# # zam = (name('Mary')
# zam('Ivanova')
# zam('Romanova')
# zam('Andreeva')
#
# zam1 = name('Sasha')
# zam1('Ivanova')
# zam1('Romanova')


