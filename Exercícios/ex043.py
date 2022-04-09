peso = float(input('Qual o seu peso?'))
altura = float(input('Qual sua altura em metros?'))
imc = peso/(altura^2)
if(imc <= 0):
    print('Vlw Haitiano(a)')
else:
    if(imc < 18.5):
        print('Você ta abaixo do peso!!!')
    elif(imc >= 18.5) and (imc < 25):
        print('Você ta no peso ideal!!!')
    elif(imc >= 25) and (imc < 30):
        print('Você ta com Sobrepeso!!!')
    elif(imc >= 30) and (imc < 40):
        print('Você ta com Obesidade!!!')
    elif(imc >= 40) e (imc <70):
        print('Você ta com Obesidade Mórbida')
    else:
        print('Você morreu e não sabe!!!1')