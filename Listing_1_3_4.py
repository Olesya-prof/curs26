def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return 'Ошибка: Деление на ноль'
    return x / y


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5) )
print(divide(10, 5))

#Добавим выбор пользователем операции и ввод чисел

print('Выберите операцию: ')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')

choise = input('Введите номер операции ( 1/2/3/4 ):')

num1 = int(input('Введите первое число :') )
num2 = int(input('Введите второе число :') )
if choise == '1':
    print(f'Результат: {num1} + {num2} = {add(num1, num2)}')
elif choise == '2':
    print(f'Результат: {num1} - {num2} = {subtract(num1, num2) }')
elif choise == '3':
    print(f'Результат: {num1} * {num2} = {multiply(num1, num2) }')
elif choise == '4':
    result = divide(num1, num2)
    # print(f'Результат: {num1} / {num2} = {divide(num1, num2) }')8

    if isinstance(result, str):
        print(result )
    else:
        print(f'Результат: {num1} / {num2} = {result}')
else:
    print('Неверный ввод')


def get_number(promt):
    while True:
        value = input(promt )
        if value.isdigit() :
            return int(value )
        else:
            print('Это не целое число. Пожалуйста,введите целое число.')

num1 = get_number('Введите первое число:')
num2 = get_number('Введите второе число.')

#Надо добавить проверку на отрицательые числа

def get_number(promt):
    while True:
        value = input(promt )
        if value.lstrip('-').isdigit() :
            return int(value )
        else:
            print('Это не целое число. Пожалуста,введите целое ччисло.')

valid_choices =['1', '2', '3', '4']
choice = None


while choice not in valid_choices :
    choice = input('Введите номер операции (1/2/3/4):')
    if choice not in valid_choices :
        print('Неверный ввод.Пожалуйста,выберите 1, 2, 3 или 4.')
num1 = get_number('Введите первое число:')
num2 = get_number('Введите второе число.')
print(f'Результат: {num1} / {num2} = {result:.4f}')#оставим только 4 знака после запятой

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: 'Ошибка: Деление на ноль' if y == 0 else x / y

#функция для получения числа от пользователя остаётся без изменений
def get_number(promt):
    while True:
        value = input(promt )
        if value.lstrip('-').isdigit():
            return int(value )
        else:
            print('Это не целое число. Пожалуйста,введите целое число')
#остальная часть программы

print('Выберите операцию: ')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')

valid_choices = ['1', '2', '3','4']
choice = None

while choice not in valid_choices:
    choice = input('Введите номер опреации (1/2/3/4')
    if choice not in valid_choices:
        print('Неверный код. Пожалуйста,выберите 1, 2, 3 или 4')

num1 = get_number('Введите первое число: ')
num2 = get_number('Введите второе число: ')

if choice == '1':
    print(f'Результат:{num1} + {num2 } = {add(num1 , num2 )}')
elif choise == '2':
    print(f'Результат:{num1} - {num2} = {subtract(num1, num2) }')
elif choise == '3':
    print(f'Результат:{num1} * {num2} = {multiply(num1, num2) }')
elif choise == '4':
    result = divide(num1 , num2 )
    if isinstance(result , str):
        print(result )
    else:
        print(f'Результат:{num1} / {num2 } = {result :.4f}')
else:
    print('Неверный ввод')





