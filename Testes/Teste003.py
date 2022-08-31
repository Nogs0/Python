tipo = input("Enter with something")


if(tipo.isalnum()):
    print('A string digitada é alfanumérica?')
    print('Sim')

if(tipo.isnumeric()):
    print('A string digitada é um número?')
    print('Sim')

if(tipo.isalpha()):
    print('A string digitada é uma letra?')
    print('Sim')
if(tipo.isalpha()):
    print('A string digitada é composta por letras maiúsculas?')
    if(tipo.isupper()):
        print('Sim')
    else:
        print('Não')