from random import choice
verdades = ['Já fez algo que se arrepende?', 'Já tirou o BV?', 'Você tem alguma história inesquecível?', 'Como foi sua primeira vez?']
desafios = ['Imite uma galinha', 'Imite um porco', 'Me dá um beijo', 'Você agora está com o poder!']
option = 'sim'
while option == 'sim':
    chose = str(input('Qual você escolhe? '))

    if(chose == 'v'):
        print('Você escolheu verdade!\nE a pergunta é: {}'.format(choice(verdades)))
    else:
        print('Você escolher desafio!\nE o desafio é: {}'.format(choice(desafios)))
    
    option = input('Você deseja continuar jogando?\nDigite sim, se quiser: ')
