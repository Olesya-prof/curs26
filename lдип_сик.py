def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y


def log(result):
    with open("calculations.txt", "a") as file:
        file.write(result + "\n")


def show_history():
    try:
        with open("calculations.txt", "r") as file:
            history = file.readlines()
            if not history:
                print("История вычислений пуста.")
            else:
                print('\nИстория вычислений:')
                for line in history:
                    print(line.strip())


    except FileNotFoundError:
        print("История вычислений пуста (файл не найден).")

def main():
    while True:
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Просмотр истории вычислений")

        choice = input("Введите номер операции (1/2/3/4/5/): ")

        if choice == '5':
            show_history()
            continue

        if choice not in ['1', '2', '3', '4']:
            print("Неверный ввод. Пожалуйста, выберите операцию от 1 до 5.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Введите корректное число.")
            continue

        if choice == '1':
            r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
            print(r)
            log(r)
        elif choice == '2':
            r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
            print(r)
            log(r)
        elif choice == '3':
            r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
            print(r)
            log(r)
        elif choice == '4':
            result = divide(num1, num2)
            r = f"Результат: {num1} / {num2} = {result}"
            print(r)
            log(r)


if __name__ == "__main__":
    main()




















