from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
jog = int(input('''
      Qual a sua Jogada??
      [0] Pedra
      [1] Papel
      [2] Tesoura
      '''))
if(jog <= 0) and (jog > 3):
    print('Nº inválido!!!')
else:
    print('''
        O Computador escolheu {}
        O Jogador escolheu {}
    '''.format(itens[pc], itens[jog]))
    if(jog == pc):
        print('Empate!!!')
    elif(jog == 0) and (pc == 1):
        print('Você Perdeu!!!')
    elif(jog == 0) and (pc == 2):
        print('Você Venceu!!!')
    elif(jog == 1) and (pc == 0):
        print('Você Venceu!!!')
    elif(jog == 1) and (pc == 2):
        print('Você Perdeu!!!')
    elif(jog == 2) and (pc == 0):
        print('Você Perdeu!!!')
    elif(jog == 2) and (pc == 1):
        print('Você Venceu!!!')
    else:
        print('Ta jogando oq?')