'''tuple ''' #упорядоченный набор неизменяемых объектов

#
# tuple = [33, 'Vasiliy', True, [1, 2]]
tp = (33, 'Vasiliy', True, (1, 2))
tp1 = tp [:3]
print(tp1)
for i in tp:
    print(i)

PI = 3,1415926 #константу задаём как кортеж с единственным элементом
print(PI)
print(PI[0]) #значение константы вытаскивается только по индексу 0


tp = ('login','password')
print(id(tp ))
buf = list(tp ) #преобразовали в список изменили
buf [-1] = 'new password' #обратно в кортеж преобразовываем
tp  = tuple (buf) #новый другой объект , tuple пересоздаётся
print(tp)
print(id(tp))

tp_sort = sorted(tp, reverse=True) #при сортировке кортежа возвращается список
print(id(tp_sort))
print(tp_sort )
print(type(tp_sort))
