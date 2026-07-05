file = open('text.txt', 'r', encoding = 'utf-8')

# s = file.read(10)
# print(s)
# s = file.read(10)
# print(s)
# s = file.read()
# print(s)
# file.close()

s = file.readline()
print(s)
file.close()

for i in open('text.txt', 'r', encoding= 'utf-8'):
    print(i)
    print(i.strip() )

with open('text.txt', 'r', encoding= 'utf-8') as file :
    s = file.read().title()
    ls = s.split()
    print(s)
    ls.sort()
    print(ls)
with open('text1.txt','a',encoding= 'utf-8' ) as file :
    for k, i in enumerate(ls,1):
        file.write(f'{k},{i} \n')