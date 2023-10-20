'''
fruta = ''

while fruta != 'abacate':
    fruta = input('Qual a fruta: ')
print('Congrats! You answer is right!')
'''


while True:
    fruta = input('Qual a fruta: ')
    if fruta.lower() == 'abacate':
        break
print('Congrats! You answer is right!')
