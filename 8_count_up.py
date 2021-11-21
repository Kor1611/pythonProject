def count_digits(x):  # Сумма цифр числа
    sum = 0;
    while x > 0:
        sum += x % 10
        x = round(x / 10)
    return sum


y = int(input('Input number:'))
print('Sum digits of number = ', count_digits(y))

