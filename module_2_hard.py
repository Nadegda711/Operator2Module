def number (n):
    num =[]
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i+j) == 0:
                num += str(i) + str(j)
    return num
print('Введите число: ')
print(number(int(input())))



















