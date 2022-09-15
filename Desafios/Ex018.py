import imp
from math import cos, sin, tan

angulo = (int)(input('Digite um ângulo: '))


angulo = (3.1415926 / 180) * angulo


seno = sin(angulo)
coseno = cos(angulo)
tangente = tan(angulo)

print('Seno: {:.3f}\nCoseno: {:.3f}\nTangente: {:.3f}'.format(seno,coseno,tangente))