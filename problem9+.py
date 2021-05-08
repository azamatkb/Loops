#9 Генерация 200 чисел и сортировка
n = 0
for numbers in range(-100,101,1):
    if numbers % 13 == 0 and numbers % 2 == 0:
        if numbers != 0:
            n = n + 1
            print (numbers ** 2, end=',')
print ('\n', 'Итого, кол-во цифр четных и делимых на 13 без остатка составляет: ',n)

n2 = 0           
for numbers2 in range(-100,101,7):
    if numbers2 % 2 != 0:    
        n2 = n2 + 1
        print (numbers2, end=',')
print ('\n', 'Итого, кол-во каждой седьмой не чётной цифры составляет: ',n2)
