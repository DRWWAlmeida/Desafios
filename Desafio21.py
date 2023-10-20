states = {'RJ', 'SP', 'MG'}
print(type(states))

res = input('Qual o estado: ')
if res.upper() in states:
    print('City Found!')
else:
    print('City not Found!')