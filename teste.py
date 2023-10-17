# Desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede.
O usuario devera fornencer as seguintes informações: Rendimento, Altura, e Largura.
O programa deve mostrar na tela a mensagem "Voce precisa de X latas de tinta."
'''


def rend(a, b, c):
    x = c*b/a
    print(f'Você necessita de {x} latas de tinta!')


rendimento = int(input('Qual o rendimento da lata de tinta? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual a largura da parede? '))
rend(rendimento, altura, largura)











