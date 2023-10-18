num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))


def calculos(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    exponeciacao = n1 ** n2
    result = []
    result.append(soma)
    result.append(subtracao)
    result.append(multiplicacao)
    result.append(divisao)
    result.append(exponeciacao)
    print(result)

calculos(num1, num2)



