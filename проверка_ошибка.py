try:
    n = int(input('>'))
    if n == 100:
        raise ValueError('запрещённое значение')
except ValueError as err:
    print('Error', err)
except TypeError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
else:
    print('выполняется при отсутствии ошибки')
finally:
    print('выполняется всегда')