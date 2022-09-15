from curses.ascii import isspace


a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(a)))
print('Contém somente espaços? {}'.format(a.isspace()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Contém apenas números? {}'.format(a.isnumeric()))
print('Contém apenas letras? {}'.format(a.isalpha()))
print('Contém apenas letras maiúsculas? {}'.format(a.isupper()))
print('Contém apenas letras minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))
