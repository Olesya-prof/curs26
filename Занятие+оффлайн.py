# #Задача1
# st = 'Python-современный язык программирования! Многие начинают изучать Python! Мы уже пишем код на Python!!!'
# new_st = st.replace('Python','Java')
# new_st = new_st.replace('!','')
# print(new_st.upper() )
#
# #Задача2
# while True:
#     password = input ('Введите пароль:')
#     has_upper = False
#     has_digit = False
#
#     for i in password :
#         if i.isupper() :
#             has_upper = True
#         if i.isdigit() :
#             has_digit = True
#
#     if len(password ) >= 8 and has_upper and has_digit :
#         print('Пароль принят!')
#         break
#     else:
#         print('Пароль не соответствует требованиям!')
from itertools import count

#Задача 3

# numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]
# s = numbers [::2]
# print(s)
# s1 = numbers[::-1]
# print(s1)
# s2 = [i for i in numbers if i % 3 != 0]
# print(s2)
# print(numbers [5:7])

#Задача4

# fruits = ('яблоко','банан','груша','апельсин','банан','киви','банан','слива')
# index = fruits.index('банан')
# print(index )
# count = fruits .count('банан')
# print(count )
# new_fruits = tuple(индекс for индекс in fruits for _ in range(2))
# print(new_fruits)

# fruits1 = ()
# for i in fruits:
#     fruits1 += (i, i)
# print(fruits1 )

#Задача5
# set1 = {2, 4, 6, 8, 10, 12}
# set2 = {6, 8, 10, 14, 16, 18}
#
# set3 = set1.intersection(set2) #set1 & set2
# print(set3)
#
# set4 = set1.union(set2)  # set1 | set2
# print(set4)
#
# set5 = set1.discard(set2)  # set1 - set2
# print(set5)
#
# set6= set1.issubset(set2)
# print(set6)
#Задача6
# d = {'Иван': [5, 4, 5], 'Пётр': [3, 4, 4], 'Мария': [5, 5, 4],'Ольга': [4, 5, 5]}
#
# d['Анна'] = [5, 5, 5]
# print(d)
#
# del d ['Пётр']
# print(d)
#
#
# d2 = {'Елена': [5, 4, 5], 'Дмитрий': [4, 3, 5], 'Сергей': [5, 5, 5]}
# d.update(d2)
# print(d)
#
#
# for k, v in d.items() :
#     average = round(sum(v) /len(v), 2)
#     print(k, average)

import random



# secret_number = random.randint(1, 100)
# print(secret_number)
# count = 0
#
# while True:
#     you_number = int(input("Введите ваше число!:"))
#     count += 1
#     if you_number < secret_number :
#         print('Больше')
#     elif you_number > secret_number :
#         print('Меньше')
#     else:
#         print(f'Поздравляю! Вы угадали число{secret_number} с {count } попытки! ')
#         break

st = input('Введите строку для исследования:')
vowels = 'а, е, ё, и, о, у, ы, э, ю, я'
print(type(vowels ))

vowels = [i.strip() for i in vowels .split(',') ]
print(vowels )

count_vowels = 0
count_con = 0
count_digit = 0

for i in st:
    if i in vowels :
        count_vowels += 1
    elif i.isalpha() :
        count_con += 1
    elif i.isdigit() :
        count_digit += 1
max_count = 0
max_ch = ""
count = 0

for i in st:
    if i != " ":
        count = st.count(i)
    if count > max_count :
        max_count = count
        max_ch = i

print(count_vowels , count_con , count_digit, max_count , max_ch  )

#Введите строку для исследования:12345 я иду искать
# <class 'str'>
# ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# 5 5 5

print(f'Количество гласных букв {count_vowels}\n количество согласных букв {count_con } \n количество цифр {count_digit}\n самый встречающийся символ {max_ch} \nвстречается в строке {max_count} раза')