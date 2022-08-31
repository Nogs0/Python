Nome = input('Enter with your name: ')
Idade = int(input('Enter with your age: '))
Id = int(input('Enter with your id: '))

if(Id <= 100):
    print('Seu id é {}, operário: {}, {} anos'.format(Id, Nome, Idade))
elif(Id <= 200):
    print('Seu id é {}, analista: {}, {} anos'.format(Id, Nome, Idade))
elif(Id == 201):
    print('Ooolá, chefe!')