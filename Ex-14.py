# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите вещественное число: ')
strN = n.split(",")

sum1 = 0
for i in range(len(strN[0])):
    sum1 += int(strN[0][i])
sum2 = 0
for i in range(len(strN[1])):
    sum2 += int(strN[1][i])

print(sum1+sum2)

