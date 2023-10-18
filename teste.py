# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionarios que tem carro e trabalha a noite
Lista2 = Funcioanrios que tem carro e trabalha durante o dia
Lista2 = Funcionarios que não tem carro
'''


funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

'''set_funcionarios = set(funcionarios)
set_turno_dia = set(turno_dia)
set_turno_noite = set(turno_noite)
set_tem_carro = set(tem_carro)

print(f'Funcionarios que tem carro e trabalha a noite:{set_tem_carro & set_turno_noite}')
print(f'Funcionarios que tem carro e trabalha de dia:{set_tem_carro & set_turno_dia}')
print(f'Funcionarios que não tem carro:{set_funcionarios ^ set_tem_carro}')'''

#resolução professor

lista1 = set(tem_carro).intersection(turno_noite)
print(f'Funcionarios que tem carro e trabalha a noite:{lista1}')

lista2 = set(tem_carro).intersection(turno_dia)
print(f'Funcionarios que tem carro e trabalha de dia:{lista2}')

lista3 = set(funcionarios).difference(tem_carro)
print(f'Funcionarios que não tem carro:{lista3}')




