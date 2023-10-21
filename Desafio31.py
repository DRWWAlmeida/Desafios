user_num = int(input('Digite um numero: '))

imp_par = lambda num: "Par" if num%2 == 0 else 'Impar'

print(imp_par(user_num))