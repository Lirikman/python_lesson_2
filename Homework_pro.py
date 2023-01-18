#6. Найти сумму цифр числа.
number = int(input('Enter any number '))
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10
print(sum)

#7. Найти произведение цифр числа.
number = int(input('Enter any number '))
product = 1
while number > 0:
    product *= number % 10
    number = number // 10
print(product)

#8. Дать ответ на вопрос: есть ли среди цифр числа 5?
number = int(input('Enter any number '))
count = 0
while number > 0:
    num_temp = number % 10
    if num_temp == 5:
        count += 1
        break
    else:
        number //= 10

if count > 0:
    print('Yes')
else:
    print('No')

#9. Найти максимальную цифру в числе
number = int(input('Enter any number '))
max_num = 0

while number > 0:
    num_temp = number % 10
    if num_temp > max_num:
        max_num = num_temp
        number //= 10
    else:
        number //= 10
print(max_num)

#10. Найти количество цифр 5 в числе

number = int(input('Enter any number '))
count = 0
while number > 0:
    num_temp = number % 10
    if num_temp == 5:
        count += 1
        number //= 10
    else:
        number //= 10
print('Количество цифр 5 в числе: ', count)