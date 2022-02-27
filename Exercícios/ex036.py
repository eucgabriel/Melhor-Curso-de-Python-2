ksa = float(input('Qual o valor da Casa?'))
sal = float(input('Qual o valor do seu salário?'))
anos = float(input('Em quantos anos pretende pagar essa casa?'))
result = (ksa/12)/anos
if(result >= ((30/100)*sal)):
    print('''
Seu salário não condiz com o quanto vc
quer pagar por mês nessa residência
          ''')
else:
    print('Vc consegue pagar essa casa')