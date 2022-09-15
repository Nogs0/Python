n = (int)(input('Digite um numero cujo queria obter a tabuada: '))
aux = 10
while(aux >=0):
    tab = n * aux
    print('{} * {} = {}'.format(n, aux, tab ))
    aux-=1
