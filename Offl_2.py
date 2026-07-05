import random
from datetime import datetime, date, timedelta, time, UTC
from datetime import date
from itertools import count



#задача1
#
# def process_list(lst):
#     if not isinstance(lst, list):
#         print('Неверный тип данных')
#         return
#
#
#
#     # new_list = [i ** 2 if i % 2 == 0 else i ** 3 for i in lst]
#     # return new_list
#
#     # for i in lst:
#     #     if i % 2 == 0:
#     #         new_list.append(i ** 2)
#     #     else:
#     #        new_list.append(i ** 3)
#     # return new_list
#
#     new_list = list(map(lambda i: i ** 2 if i % 2 == 0 else i ** 3, lst))
#     return new_list
#
#
# print(process_list([2, 3, 4, 9]))
# print(process_list([3, 6, 2, 8, 4]))
# print(process_list('Hello world!'))



#Задача 2
#
# choices = ['камень','ножницы','бумага']
#
# while True:
#     user_choice = input('Введите одно из значений: камень,ножницы или бумага или выход :').lower()
#
#     if user_choice == 'выход':
#         print('Игра окончена!')
#         break
#
#     if user_choice not in choices:
#         print('Выберите из списка!')
#         continue
#
#     computer_choice = random.choice(choices )
#
#     print(f'Компьютер выбрал: {computer_choice }')
#     print(f'Вы выбрали: {user_choice }')
#
#     if user_choice == computer_choice :
#         print('Ничья!')
#     elif ((user_choice == 'ножницы' and computer_choice == 'бумага')
#         or (user_choice == 'бумага' and computer_choice == 'камень')
#         or (user_choice == 'камень' and computer_choice == 'ножницы')):
#         print('Вы выиграли!')
#     else:
#         print('Компьютер выиграл!')

# choices = ['камень','ножницы','бумага']
#
# def get_user_choice():
#     choices = ['камень', 'ножницы', 'бумага']
#     user = input('Введите одно из значений: камень,ножницы или бумага или выход :').lower()
#
#     if user == 'выход':
#         return user
#     if user not in choices :
#         raise ValueError ('Такого варианта нет')
#         #print('Такого варианта нет')
#
#     return user
#
#
#
# def get_computer_choice():
#     choices = ['камень', 'ножницы', 'бумага']
#     computer = random.choice(choices)
#     return computer
#
# def check_winner (user, computer):
#     if user == computer:
#         return 'ничья!'
#     elif ((user == 'ножницы' and computer == 'бумага')
#         or (user == 'бумага' and computer == 'камень')
#         or (user == 'камень' and computer == 'ножницы')):
#         return 'Вы выиграли!'
#     return 'Компьютер выиграл!'
#
# while True:
#     try:
#         choices = ['камень', 'ножницы', 'бумага']
#         user = get_user_choice()
#         if user == 'выход':
#             print('Игра окончена!')
#             break
#
#         if user not in choices :
#             print('Такого варианта нет')
#
#         print(f'Вы выбрали : {user}')
#
#         computer = get_computer_choice()
#         print(f'Компьютер выбрал: {computer }')
#
#         result = check_winner(user , computer )
#         print(result )
#
#
#     except Exception as e:
#         print('Ошибка:', e)

#Задача 3

# file = open('log.txt', 'r', encoding = 'utf-8')
# s = file.read()
# print(s)
#
# def analyze_log(s):
#     counts = {'ERROR': 0, 'INFO': 0, 'WARNING': 0}
#     dates = []
#     try:

# count_error = 0
# count_info = 0
# count_warning = 0
#
# dates = []
#
# with open('log.txt', 'r', encoding = 'utf-8') as file:
#     for i in file:
#         parts = i.split()
#         #print(parts )
#         print(parts[0], parts[1])
#
#
#         date_str = parts[0]
#         log_type = parts[1]
#
#         dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
#
#         if log_type == 'ERROR':
#             count_error +=1
#         elif log_type == 'INFO':
#             count_info +=1
#         elif log_type == 'WARNING':
#             count_warning +=1
#
# print(f'Количество записей типа "ERRORf" - {count_error} ' )
# print(f'Количество записей типа "INFO" - {count_info }')
# print(f'Количество записей типа "Warning" -{count_warning }')
# print(f'Самая рання дата {min(dates).date()}')
# print(f'Самая поздняя дата {max(dates).date()}')
#
#
# print(f'Самая рання дата: {min(dates).date()}')
# print(f'Самая поздняя дата: {max(dates).date()}')


#Задачf4

try:
    birth_date = input('Введите дату вашего рождения в формате(DD.MM.YYYY):')
    birth_date = datetime.strptime(birth_date ,'%d.%m.%Y')
    current_date = datetime (2026, 6, 19)
    age = current_date.year - birth_date.year
    print(f'Вам {age} лет')


except Exception as e:
    print("Error", e)













