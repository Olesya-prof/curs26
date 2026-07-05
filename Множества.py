""" Set-неупорядоченный набор уникальных объектов
#Значение--> Хэш --> Функция --> Хэш-код --> Хэш-таблица
'Значение 1'
'Значение 2'


1 = 'Значение 1'
2 = 'Значение 2'


1 = 'Значение2'
5 = 'Значение1'

Поиск в списке - 0(n) линейный
Поиск в множестве - 0(1) константный, единичная операция 

объекты множества - любой неизменяемый тип данных, может быть кортеж, 
множество и словарь 
"""
st = {12, 20, 1, 33, 1}
print(st)
st = {22, 33, 44}
print(st)
st = {22, 33, 44, 44}
st.clear() # Очистить множество, получаем пустое множество
print(st)
st = set() # создание пустого множества
print(st)
ls = [22, 33, 44, 44]
st = set(ls)
st.add(100) # метод добавления в множество объекта
print(st)
st.update([1, 2])# Добавление в множество объектов ЭЛЕМЕНТОВ из (списка, множества, кортежа)
print(st)
st.add((100,)) # метод добавления в множество кортежа
## st.add([100,200]) # Список не можем добавить в множество,->ОШИБКА
print(st)

n = st.pop()# удаляем первый объект множества
print(st,n)
n = st.pop() # удаляем след.первый объект множества
print(st, n)
st.remove(2) # удаление из множества указанного по ЗНАЧЕНИЮ объекта
print(st)    # !!!не по индексу (отсутствие объекта -> ошибка)
st.discard(2) # тоже что и remove, но не выдает ошибку в случае
            #  отсутствия объекта по указанному индексу
print(st)


st1 = {1, 2, 33}
st2 = {1, 2, 44}
# res = st1.union(st2)# Объединение, результат: {1, 2, 33, 44}
# print(res)
# res = st1| st2# тоже самое что и union()
# print(res)

res = st1.intersection(st2) # пересечение множеств
print('Пересечение множеств:',res)
res = st1 & st2
print('Пересечение множеств:',res)

res = st1.difference(st2) # вычитание множеств
print(res)
res = st1 - st2
print('Вычитание множеств',res)
res = st1.symmetric_difference(st2)# симметричная разница множеств
res = st1 ^ st2
print('Симметричная разность: ', res)
st3 = {1, 2}
print(st1.issuperset(st3)  )# является ли st1 надмножеством st3 - True
print(st3.issubset(st2)) # является ли st3 подмножеством st2 - True

# res = st1.difference(st2)
# print(res)
# print(st1)
# print(st2)
# st1.difference_update(st2)
# print(st1)
# print(st2)

# ice_cream = ['клубника', 'малина', 'банан', 'клубника']
# result = []
# for n in ice_cream:
#     if n not in result:
#         result.append(n)
# print(result)
# # result = [n for n in ice_cream if n not in result]  # так нельзя
# stt = set(ice_cream)
# result = [n for n in set(ice_cream)]
# print(result)

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'
# выписать вторую строку без слов в первой строке
a = a.replace(',', '')
sta = set(a.split())
stb = set(b.split())
print(' '.join(list(stb - sta)))

la = a.split()
lb = b.split()
res = [w for w in lb if w not in sta]
# res = []
# for w in lb:
#     if w not in la:
#         res.append(w)
print(' '.join(res))





