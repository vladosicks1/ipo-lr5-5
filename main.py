string = str(input("Введите строку: ")) #ввод строки


for i in range(len(string)): #проверка, вывод индексов
    if string[i]=="е":
        print(i)