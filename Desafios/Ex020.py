from random import choice, shuffle

a = [] 
n=0

while(n<4):
    a.append(str(input('Insira o nome do aluno: ')))
    n+= 1
shuffle(a)

print('A ordem será: - {}\n'.format(a))