n1 = int(input('Diga o 1º nº:'))
n2 = int(input('Diga o 2º nº:'))
if(n1 > n2) or (n2 > n1):
    num = [n1, n2]
    print('''
    O nº {} é maior que o nº {}
          '''.format(max(num), min(num)))
else:
    print('Os nºs são iguais!!!')