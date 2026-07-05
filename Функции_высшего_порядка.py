from functools import reduce

lst = [22, 33, 44, 55]
lss = [2, 3, 4, 5]
res = map(str, lst)
print(next(res ) ) #22

res = list(map(str, lst))
print(res) #['22', '33', '44', '55']

def power(n):
    return n ** 2
res = list(map(power, lst))
print(res)#[484, 1089, 1936, 3025]

res1 = [power(i)for i in lst ]
print(res1)#[484, 1089, 1936, 3025]

res = list(map(lambda n: n ** 2, lst))
print(res)
res = list(map(lambda n, m: n - m, lst, lss))
print(res)#[20, 30, 40, 50]
res = list(map(lambda n, m: n > m, lst, lss))
print(res)#[True, True, True, True]
res = list(filter(lambda n: n % 2 == 0, lst))
print(res)#[22, 44]
city = ['У', 'ф', 'а','-',4, 5]
res = reduce(lambda x, y: str(x) + str(y),city)
print(res)#Уфа-45

def conc(x, y):
    print('X-', x)
    print('Y-', y)
    print('X + Y', str(x) + str(y))
    return str(x) + str(y)
res = (reduce(conc, city) )
print(res)
res = reduce(lambda x, y: x + y, lst)
print(res) #154