from random import choice
nomes = []
n = 0
while(n <= 3):
    nomes.append(str(input('Digite o aluno {}'.format(n+1))))
    n+=1

print('O aluno sorteado foi {}'.format(choice(nomes)))