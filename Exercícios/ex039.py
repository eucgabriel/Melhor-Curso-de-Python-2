anos = int(input('Qual a sua idade em anos?'))
if(anos < 18):
    print('''
          Se prepare que daqui {} ano(s) você vai se alistar
          '''.format(18-anos))
elif(anos == 18):
    print('Ta na época de se alistar, hein!')
elif(anos <= 0):
    print('Pq sua idade é abaixo de 0?')
else:
    print('Já passou da época de se alistar')
    alistar = int(input('Vc já se alistou ent?(0 para não e 1 para sim)'))
    if(alistar == 0):
        print('Faz {} q era para vc ter se alistado'.format(anos-18))
    elif(alistar == 1):
        print('Então td bem')
    else:
        print('Oq vc ta fznd aq ent?')
