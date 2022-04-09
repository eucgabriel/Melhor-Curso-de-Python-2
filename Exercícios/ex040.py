n1 = float(input('Qual a sua nota do 1º Bimestre?'))
n2 = float(input('Qual a sua nota do 2º Bimestre?'))
if((n1<0) or (n1>10)) or ((n2<0) or (n2>10)):
    print('Carai, tu é o bichão msm hein doido!')
else:
    media = (n1 + n2) / 2
    if (media < 0) and (media < 5):
        print('Vc foi reprovado!!!')
    elif(media >= 5) and (media <7):
        print('Vc ta de Recuperação!!!')
    elif(media >= 7) and (media <= 10):
        print('''Vc passou com {} de média sendo:
            1º Bimestre: {}
            2º Bimestre: {}'''.format(media, n1, n2))