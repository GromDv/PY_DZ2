# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

num = int(input('Введиите натуральное число: '))

numbers = dict()
for i in range(1,num+1):
    numbers[i] = round((1+1/i)**i,2)

print(numbers)

sum = 0
for i in range(1,len(numbers)+1):
    sum += numbers[i]

print(sum)