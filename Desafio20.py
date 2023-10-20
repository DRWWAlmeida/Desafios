#num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = list(range(1,11))


for x in num:
    if x%2 == 0:
        print(f'O numero {x} é par')
    else:
        print('O numero {} é impar'.format(x))
