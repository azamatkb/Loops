#5 порядок цифр от 1 до 10 и обратно
#Решение №1 с одним циклом, но топорно получилось.
for i in range (1,11):
    print(i, end = ",")
if i == 10:
    i = i - 1
    print(i, end = ",")
    if i <= 10:
        i = i - 1
        print(i, end = ",")
        if i <= 10:
            i = i - 1
            print(i, end = ",")
            if i <= 10:
                i = i - 1
                print(i, end = ",")
                if i <= 10:
                    i = i - 1
                    print(i, end = ",")
                    if i <= 10:
                        i = i - 1
                        print(i, end = ",")
                        if i <= 10:
                            i = i - 1
                            print(i, end = ",")
                            if i <= 10:
                                i = i - 1
                                print(i, end = ",")
                                if i <= 10:
                                    i = i - 1
                                    print(i, end = ",")
print("Конец.")


#5 порядок цифр от 1 до 10 и обратно
#Решение №2 грамотное, но нарушено условие, использованы два цикла.
"""for i in range(1,11):
    print(i,end=',')
    if i == 10:
        for i in range(9,0,-1):
            print(i,end=',')
print("Конец.")"""
