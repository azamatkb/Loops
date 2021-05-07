#4 Написать код выводящий языки с нумерацией:
languages = ['go','java','php','python','javascript','ruby']
for i in range(len(languages)):
    if i % 1 == 0:
        print(i, languages[i])
