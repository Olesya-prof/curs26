import json
#
#
# d = {'black': 'чёрный',
#      'white': 'белый'}
# with open("dic.json", 'w', encoding='utf-8') as f:
#     json.dump(d, f, indent=2)
with open("dic.json",'r',encoding= 'utf-8')as f:
      d = json.load(f)
while True:
    word = input('Введите слово для перевод: ')
    if word in d:
        print(f'{word} - {d[word]}')
    elif word == 'q':
        break
    else:
        transl = input(f'Введите перевод слова-{word}: ')
        d[word] = transl
        with open ("dic.json", 'w',encoding= 'utf-8')as f:
            json.dump(d,f,indent=2)
