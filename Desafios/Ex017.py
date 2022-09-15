from math import sqrt,pow
catetoOposto = (float)(input('Entre com o cateto oposto: '))
catetoAdjacente = (float)(input('Entre com o cateto adjacente: '))

hipotenusa = sqrt(pow(catetoOposto,2) + pow(catetoAdjacente, 2))
print('A hipotenusa desse triângulo retângulo é: {:.5f}'.format(hipotenusa))