# 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
b = 0
while b < 5:
    print(str(b+1) + ' 00000000000000000000000000000000000000')
    b += 1

# 2. Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
count = 0
for i in range(10):
    numbers = int(input('Enter any number '))
    if numbers == 5:
        count += 1
print(count)

# 3. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
sum = 0
for i in range(1, 101):
    sum +=i
print(sum)

# 4. Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# Также можно импортировать модуль math и воспользоваться функцией factorial - math.factorial(10)
product = 1
for i in range(1, 11):
    product *= i
print(product)

# 5. Вывести цифры числа на каждой строчке.
number = int(input('Enter any number '))
while number > 0:
    print(number % 10)
    number //= 10

# 5.1 Вывести цифры числа на каждой строчке.
# В этом варианте я использовал хитрость языка Python и вывел каждый символ как строковую переменную.
number = input('Enter any number ')
for i in range(len(number)):
    print(number[i])