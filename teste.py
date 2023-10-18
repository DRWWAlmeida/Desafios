# Desafio Calculadora de IMC - Indice de Massa Corporal

'''
Dados do usuario:
    - Altura em cm
    - Peso em kg

Parametros:
    Menor que 18,5 = MAGREZA
    Entre 18,5 e 24,9 = NORMAL
    Entre 25,0 e 29,9 = SOBREPESO
    Entre 30,0 e 39,9 = OBESIDADE
    Maior que 40,0 = OBESIDADE GRAVE
'''

def imc(a, p):
    imc = round(p/((a**2)/10000), 2)
    print(imc)
    if imc <= 18.5:
        print('MAGREZA')
    elif 18.5 < imc <= 24.9:
        print('NORMAL')
    elif 25 < imc <= 29.9:
        print('SOBREPESO')
    elif 30 < imc <= 39.9:
        print('OBESIDADE')
    elif 40 <= imc:
        print('OBESIDADE GRAVE!')
    else:
        ('Quebrou a balança!')


altura = float(input('Qual a sua altura em centimetros: '))
peso = float(input('Qual o seu peso em kg: '))
imc(altura, peso)










