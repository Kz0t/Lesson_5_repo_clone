"""Пользователь вводит две переменных.
С помощью f-строк, вывести наименьшее из них."""


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

min_number = min(a, b)

print(f'Наименьшее число: {min_number}')

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

min_value = a if a < b else b

print(f"Наименьшее число: {min_value}")

