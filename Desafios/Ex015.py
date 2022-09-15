from re import X


km = (float)(input('Quantos km você percorreu: '))
dias = (int)(input('Quantos dias você ficou com o carro? '))

preco = (km*0.15)+(dias*60)

print('VOcê deve pagar : R${:.2f}'.format(preco))