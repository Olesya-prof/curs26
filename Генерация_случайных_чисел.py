import random
import random as rd
from string import ascii_letters

# nums = [22, 33, 44, 55,66,77,88,99 ]
# names = ['Dasha', 'Sasha', 'Glasha', 'Masha','Andre']

# print('Random-', rd.random ())
# print('Uniform-', rd.uniform (0, 1))
# print('Uniform-', rd.uniform (10, 21))
# print('Uniform-', rd.uniform (-10, -1 ))
# print('Randint-', rd.randint (0,10))
# print('Randrange-', rd.randrange (2, 100, 2))
# print('Choice-', rd.choice (nums))
# print('Choice-', rd.choice (range (1, 11, 2)))
# print('Choice-', rd.choice (names))
# print('Choices-', rd.choices (nums, k = 20))
# print('Sample-', rd.sample (nums, 3))
# print( ascii_letters )
# password = rd.choices ( ascii_letters, k = 8)
# password = rd.sample ( ascii_letters, 8)
# print(' '. join(password ))

#List comprehension
# l = [22, 33, 44]
# res = []
# for i in l:
#     res.append(i ** 2)
# print(res)
#
# res = [i ** 2 for i in l]
# print(res)
#
# res = []
# for i in l:
#     if i ** 2 % 2 == 0:
#         res.append(i ** 2)
# print(res)
#
# res = [ i ** 2 for i in l if i ** 2 % 2 == 0]
# print(res)
#
# l = [22, 33, 44, 55, 77, 88, 200]
# res = [i ** 2 for i in l if i % 2 == 0]
# print(res)
#
# res = []
# for i in l:
#     if i % 2 == 0:
#         res.append(i ** 2)
# print(res)
#
# res = []
# for i in l:
#     if i % 2 == 0:
#         if i > 55:
#             res.append(100)
#         else:
#             res .append(i ** 2)
# print(res)
#
# res = [i ** 2 if i < 55 else 100 for i in l if i % 2 == 0]
# print(res)

#Задача - Ведомость с зарплатой для работников

# salary = [[60, 80, 70], [99, 102, 122]]
#
# workers = 6
# months = 3
# salary = [rd.choices (range (60, 151,5), k = months) for _ in range (workers)]
# for w in range (workers ):
#     salary.append(rd.choices (range (60, 151, 5), k = months ))
#     for n in range (months):
#         salary[w].append(random.randint(60, 150))
# print(salary )
#
# print(f'{chr(2926)}{'-' * 11}{chr(2930)}{'-'*22}{chr(2930)}{'-'*7}{chr(2930)} ')
# print(f'{chr(2930)} Работники{chr(2930)}, end=')
#
# for i in range(months):
#     print(f'{i + 1} мес', end = chr(2930)+' ')
#     print(f'{ 'Итого '}{2930}')
#     print(f'{chr(2930)}{'-'*11}{chr(2930)}{'-'*22}{chr(2930)}{'-'*7}{chr(2930)}')
# itog = [0] * months
# for k, i in enumerate(salary):
#     print(f'{chr(2930)}{k + 1}сотр.',end = chr(2930) + ' ')
#     for n, j in enumerate (i):
#         itog [n] += j
#         print(f'{j:4}', end= chr(2930) + ' ')
#     print(f'{sum(i):5}{chr(2930)}')
# for i in itog:
#     print(f'{i:5}', end= chr(2930)+' ')
# print(f'{sum(itog)}{chr(2930)}')


# for w in range (workers):
#     salary.append([])
#     for m in range (months):
#         salary[w].append(random.randint (60, 150))
# print(salary)
#
# for w in range(workers):
#     salary.append(rd.choices (range(60, 151,5), k = months))
# print(salary)


workers = 6
months = 3
salary = [rd.choices(range(60, 151, 5), k=months) for _ in range(workers)]
# for w in range(workers):
#     salary.append(rd.choices(range(60, 151, 5), k=months))
#     for m in range(months):
#         salary[w].append(rd.randint(60, 150))
# print(salary)
print(f'{chr(2926)}{'-' * 11}{chr(2930)}{'-'* 22}{chr(2930)}{'-'* 7} {chr(2930)}')
print(f'{chr(2930)}  Работники {chr(2930)} ', end='')
for i in range(months):
    print(f'{i + 1} мес.', end=chr(2930) + ' ')
print(f'{' Итого'} {chr(2930)}')
print(f'{chr(2926)}{'-' * 11}{chr(2930)}{'-'* 22}{chr(2930)}{'-'* 7} {chr(2930)}')
itog =[0]* months
for k, i in enumerate(salary):
    print(f'{chr(2930)}   {k+1} сотр.  ', end=chr(2930) + ' ')
    for n, j in enumerate(i):
        itog[n] += j
        print(f' {j:4} ', end=chr(2930) + ' ')
    print(f'{sum(i):5} {chr(2930)}')
print(f'{chr(2930)}    Итого   {chr(2930)} ', end='')
for i in itog:
    print(f'{i: 5} ', end=chr(2930) + ' ')
print(f' {sum(itog)} {chr(2930)}')














