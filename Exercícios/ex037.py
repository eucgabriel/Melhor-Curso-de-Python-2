num = int(input('Qual o nº em decimal?'))
base = int(input('''
    Indique a base que você quer:
    [ 1 ] BINÁRIO
    [ 2 ] OCTAL
    [ 3 ] HEXADECIMAL
                 '''))
if(base == 1): 
    print('''
    Seu nº {} foi transformado em {} na base binária
          '''.format(num, bin(num)[2:]))
elif(base == 2): 
    print('''
    Seu nº {} foi transformado em {} na base octal
          '''.format(num, oct(num)[2:]))
elif(base == 3): 
    print('''
    Seu nº {} foi transformado em {} na base hexadecimal
          '''.format(num, hex(num)[2:]))
else:
    print('ERROR 404!!!!!')
