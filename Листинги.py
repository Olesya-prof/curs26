import string
# n = input('Введите число: ')
# n = int(n)
#
# if n > 0:
#     print('Число положительное')
#
# n = int(input('Введите число: '))
# if n < 0:
#     print('Число отрицательное')

# n = int(input('Введите число:'))
# if n > 0:
#     print('Число положительное')
# else:
#     print('Число отрицательное')
#
# n = int(input('Введите число:'))
# if n > 0:
#     print('Число положительное')
# elif n < 0:
#     print('Число отрицательное')
# else:
#     print('Число ноль')
#
# n = int(input('Введите число:'))
# if n % 2 == 0:
#     print(f'Число {n} является чётным.')
# else:
#     print(f'Число {n} является нечётным.')

# s = input('Введите число: ')
# print(s.isdigit())
# if s.isdigit() :
#     print(f'Вы ввели число {s}')
# else:
#     print(f'{s} - это не число!')
# age = int(input('Введите ваш возраст:'))
# if 0 < age < 18:
#     print('Вы несовершеннолетний.')
# elif 18 <= age < 70:
#     print('Вы взрослый.')
# elif 70 <= age < 108:
#     print('Солидный возраст.')
# elif 108 <= age <120:
#     print('Вы долгожитель.')
# elif 120 <=age:
#     print('Вы гигантская черепаха.')
# else:
#     print('Вы ещё не родились.')
# s = input('Введите время года (лето, весна, осень, зима):')
# s = s.lower()
# if s == 'лето':
#     print('Отличное время для отдыха на пляже!')
# elif s == 'осень':
#     print('Прекрасное время для прогулок.')
# elif s == 'весна':
#     print('Время пробуждения природы.')
# elif s == 'зима':
#     print('Замечательное вреям для катания на лыжах.')
# else:
#     print('Вы ввели не время года.')
# if s == 'лето':
#     print('Отличное время для отдыха на пляже!')
# elif s == 'осень':
#     print(f'{s}- это прекрасное время для прогулок.')
# elif s == 'весна':
#     print(f'{s}- это время пробуждения природы.')
# elif s == 'зима':
#     print(f'{s}- этл замечательное вреям для катания на лыжах.')
# else:
#     print(f'{s}-это не время года.')
#индексы элементов строки

# Name = input('Введите имя') #Валера
# print(Name [0] ) # В
# print(Name [1] ) # а
# print(Name [2] ) # л
# print(Name [3] ) # е
# print(Name [-1] ) # а
# print(Name [-2] ) # р
# print(Name [-3] ) # е
# text = 'Пример текстовой строки'
# s = text[8:15]
# print(s) #екстово
# text = 'Python это круто'
# s = text[-7:-2]
# print(s)  #о кру
# text = "Привет,как дела ?"
# s = text[:6]
# print(s) #Привет
# text = "Это последние символы"
# s = text[-5:]
# print(s) #мволы
# text = "12345678"
# s = text[::2]
# print(s)
# text= "Аргентина манит негра"
# s = text [::-1]
# print(s) #Перевёрнутая строка
# text = "Разделить строку"
# x = 9
# p_1 = text[:x]
# p_2 = text[x:]
# print(p_1, p_2)
#
# k = (1, 2, 3, 4, 5)
# a = 4
# if a in k:
#     i = k.index(a)
#     print(f'Индекс {a} в кортеже:{i}') #возвращает индекс первого вхождения элемента
# else:
#     print(f'Элемент {a} не найден в кортеже.')
#
# s1 = [2, 64, 80, 4, 32, 16]
# print(max(s1))
# k = (2, 64, 80, 4, 32, 160)
# print(max(k))
# s1 = ['Буря', 'мглою', 'небо', 'кроет']
# print(max(s1))
# print(min(s1))
#
# s = [-2, 64, 80, 4, 32, 16]
# print(min(s))
# url = "https://example.com/path/to/file.txt"
# f = url.split("/")[-1]
# print(f"Имя файла из URL: {f}")


# k = (10, 20, 30, 40, 50) #перебор кортежа в цикле
# for i in k:
#     print(i / 2)
# s1 = [1, 2, 3, 4, 5]  #перебор списка в цикле
# for i in s1:
#     print(i * 10)
# s = ['Буря', 'мглою', 'небо', 'кроет']
# for i in s:
#     print(i)
# s = ['Буря', 'мглою', 'небо', 'кроет']
# for i in s:
#     if i == 'небо':
#         continue
#     print(i)
s = ['Буря', 'мглою', 'небо', 'кроет']
i = 0 #инициализация счётчика
while i < len(s): #условие продолжения цикла len(s)= 4
    print(s[i]) #вывод элемента по текущему индексу
    i += 1 #увеличение счётчика на 1

# s = ['Буря', 'мглою', 'небо', 'кроет']
# i = 0
# while i < len(s):
#     if s[i] == 'мглою':
#         i += 1
#         continue
#     print(s[i])
#     i += 1
# print('00000000011111111112222222222')
# print('***\t***\t***\t***')
# print('100\t100500\t1000\t10')
# print('Winter\tSpring\tSummer\tAutumn')
#
# print('Зима\tВесна\tЛето\tОсень')
import random

# print("-" * 13) #табличка со случайными числами от 0 до 9
# for i in range(10):
#     a = str(random.randint(0,9))
#     b = str(random.randint(0,9))
#     c = str(random.randint(0,9))
#     print(f"| {a} | {b} | {c} |")
# print("-" * 13)

import random
# print("-" * 18) #табличка со случайными числами от 0 до 10000 с пробелами и без \t
# for i in range(10):
#     a = str(random.randint(0, 99))
#     b = str(random.randint(0, 999))
#     c = str(random.randint(0, 9999))
#     print(f"| {a} | {b} | {c} |")
# print("-" * 18)
# print("-" * 25) #Табличка со случайными числами от 0 до 10000 с табуляцией \t.
# for i in range(10):
#     a = str(random.randint(0, 99))
#     b = str(random.randint(0, 999))
#     c = str(random.randint(0, 9999))
#     print(f"| {a} \t| {b} \t| {c} \t|")
# print("-" * 25)
# print("-" * 25) #Выравнивание чисел по правому краю
# for i in range(10):
#     a = str(random.randint(0, 99))
#     b = str(random.randint(0, 999))
#     c = str(random.randint(0, 9999))
#     print(f"| {a:>2} \t| {b:>3} \t| {c:>4} \t|")
# print("-" * 25)
# print("-" * 25) #Выравнивание чисел по правому краю с отступом в 2 пробела от вертикальной черты
# for i in range(10):
#     a = str(random.randint(0, 99))
#     b = str(random.randint(0, 999))
#     c = str(random.randint(0, 9999))
#     print(f"| {a:>4} \t| {b:>4} \t| {c:>4} \t|")
# print("-" * 25)
import random


# Множества с различными частями фраз
#Школьные отмазки

# p = {"сражение котов", "вторжение инопланетян", "нашествие грызунов","затопление"}
# d = {"заставило меня спасать всех","задержало меня", "сорвало мои планы"}
# m = {"на школьном дворе", "в парке", "по пути в школу", "в автобусе"}
# o_p = random.choice(list(p))
# o_d = random.choice(list(d))
# o_m = random.choice(list(m))
# print(f"Я опоздал, потому что {o_p} {o_d} {o_m}")
d = {"name": "Алиса", "age": 15}
if "name" in d:
    print("Name is in the dictionary")
d = {"name": "Алиса", "age": 15}
for i in d:
    print(i)
dossier = {'name': 'Алексей',
           'age': 30,
           'profession': 'программист',
           'hobbies': ['туризм','велосипед','чтение'],
           'education': 'МГУ',
           'languages': ['русский', 'английский'],
           }
for key, value in dossier.items() :
    if isinstance(value, list):
        value = ','.join(value )
    print(f'{key.capitalize()}: \t{value}')