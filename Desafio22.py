dados = {
    'brasil': 'Brasilia',
    'eua': 'Washington DC',
    'frança': 'Paris',
    'china': 'Pequim',
    'holanda': 'Amesterdã'
}

res = input('Qual o pais: ')
if res.lower() in dados.keys():
    print(f'A capital de {res} é {dados[res]}')
else:
    print('Desculpe, não temos informações sobre a capital desse pais!')


