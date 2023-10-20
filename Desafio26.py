def cal(x, y=2):
    cal = x**y
    return cal

v1 = int(input('Digite a base: '))
v2 = input('Digite o expoente: ')

if v2:
    print(f'O resultado é: {cal(v1, int(v2))}')
else:
    print(f'O resultado é: {cal(v1)}')
