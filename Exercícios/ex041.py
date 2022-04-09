from datetime import datetime
nasc = int(input('Qual o ano que vc nasceu?'))
atual = int(datetime.today().strftime('%Y'))
data = int(atual - nasc)
if(data < 0):
    print('Parabéns, vc é a 1ª pessoa com idade negativa')
else:
    if(data < 9):
        print('A pessoa indicada é Mirim!!!')
    elif(data >=9) and (data < 14):
        print('A pessoa indicada é Infantil!!!')
    elif(data == 19):
        print('A pessoa indicada é Júnior!!!')
    elif(data == 20):
        print('A pessoa indicada é Sênior!!!')
    else:
        print('A pessoa indicada é Master!!!')

        