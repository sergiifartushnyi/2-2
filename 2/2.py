number = int(input('Введіть 5-значне число:'))

reversed_number = 0

while number > 0:
    digit = number % 10
    number = number // 10

    reversed_number = reversed_number * 10 + digit

print('Перевернуте значення:', (reversed_number))