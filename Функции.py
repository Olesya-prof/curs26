""" подпрограмма,которая.ждёт вызова для работы """

# def proba():  #параметры функции, пишутся в начале программы
#     print('Ura-ura') #тело функции  ...процедура
#
# proba()
#
# def summator(x, y):  #x,y -параметры функции summator
#
#     z = x * y / 10  #тело функции
#     return z   #возврат результатов
#
#
# n = summator(20, 15) #передача аргументов при вызове функции
# print(n)
# print(summator(20, 15) ) #только видим результат
# #если n = summator. присваивается переменная и может использоваться в программе
#
# def summator(x:int, y:int):
#     """ Описание функции"""
#     z = x + y
#     return str(z)
# n = summator(20, 15)
# print(n)
# print(summator(20, 20) )
# print(__doc__)

# square = []
# for i in range (10, 20):
#     square.append(i ** 2)
# print(square )
#
# square [0] * 10
# for i in range (10):
#     square [i] = (i + 10) ** 2
# print(square )
#
# power = [i ** 2 for i in range (10,20)]
# n = 5 if power[0] > 0 else None
# print(square) #[100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# #лист компрехейшен предполагает цикл внутри то,что перед циклом,будет добавлено в цикл
#
# power = [i ** 3 for i in range (-10, 0)]
# n = 5 if power[0] > 0 else None
# print(n, type(n)) #None <class 'NoneType'>

# def adding(x, y = 15):
#     return x + y
# print(adding(2, 15) )
# print(adding(2) )
# print(adding(2, 14) )

# def adding(x =4, y = 15):
#     return x + y
# print(adding() )#19
# print(adding(3) )#18
# print(adding(y = 30) )#34

def adding(x =4, y = 15, z = 16, q = 33):
    return x + y
# print(adding(y = 30, z = 1) ) #34
#
# n = 7
# print(n, type(n)) #7 <class 'int'>
# n = 7, 5, 12
# print(n, type(n))#(7, 5, 12) <class 'tuple'>
#
# n, m, *z = 7, 5, 12, 77, 88, 99
# print(n, type (n), m) #7 <class 'int'> 5
# print(z, type(z)) #[12, 77, 88, 99] <class 'list'>
#
# n, *z = 7, 5, 12, 77, 88, 99
# print(z, type (z)) #[5, 12, 77, 88, 99] <class 'list'>
# print(*z) #5 12 77 88 99

# d = {}
# n = 3
# for _ in range (n):
#     name, *marks = input('>').split()
#     marks = [int(m) for m in marks ]
# #перевели строковые оценки в целочисленные
#     d[name] = round(sum(marks )/len (marks ), 2) #round округляет значение
#     print(d)

# def adding(*args):
#     print(args )#(2, 15)
#     return sum(args )
# print(adding(2, 15) )#17
# print(adding() )#() 0

def adding(*args, **kwargs):  # разное количество позиционных и ключевых аргументов
    print(args)
    print(kwargs, list(kwargs.values()))
    sumkw = sum(list(kwargs.values()))
    # return sum(args), sumkw
    return sum(list(args) + list(kwargs.values()))

print(adding(2, 15, 17, 33, x=12, y=33, z=18))
print(adding())










