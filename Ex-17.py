# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = 10
spisok = []
for i in range(-n, n+1):
    spisok.append(i)

print(spisok)

mltpl = 1
f = open("file.txt", "r")
for line in f:
    mltpl *= spisok[int(line)]
    print(spisok[int(line)], end=" ")
f.close()
print("\n Произведение = ",mltpl)

