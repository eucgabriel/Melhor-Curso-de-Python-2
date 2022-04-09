valor = float(input('Qual o valor do produto que vc quer adquirir?'))
condpag = int(input('''
    Qual a condição de pagamento???
    [0] Dinheiro/Cheque
    [1] Cartão à vista
    [2] 2x no cartão
    [3] 3x ou mais no cartão
    '''))
if(condpag < 0) or (condpag > 3):
    print('Não é uma condição de pagamento')
else:
    if(condpag == 0):
        valfinal = valor - (valor * 10/100)
        print('''
        Você irá pagar R$ {:.2f}
              '''.format(valfinal))
    elif(condpag == 1):
        valfinal = valor - (valor * 5/100)
        print('''
        Você irá pagar R$ {:.2f}
              '''.format(valfinal))
    elif(condpag == 2):
        valfinal = valor/2
        print('''
        Você irá pagar 2x R$ {:.2f}
        Com o valor final de R$ {:.2f}
              '''.format(valfinal, valor))
    elif(condpag == 3):
        vez = int(input('Quantas vzs vc vai dividir no cartão acima de 3x?'))
        if(vez >= 3):
            valfinal = valor + (valor * 20/100)
            valfinaldiv = valfinal/vez
            print('''
            Você irá pagar {}x de R$ {:.2f}
            Com o valor final de R$ {:.2f}
                '''.format(vez, valfinaldiv, valfinal))
        else:
            print('Reseta o programa!!!')
    else:
        print('valor inválido!!!')