#Faça um código que leia a altura e peso do usuário, calcule IMC e imprima a facha do peso. (Até 18.5 abaixo do peso, de 18.5 até 25 peso normal, de 25 até até 30 acima do peso e acima de 30 obeso)

altura = float(input('Informe a sua altura:\n'))
peso = float(input('Informe o seu peso:\n'))

imc = peso / (altura**2)

if imc <= 18.5:
  print('Abaixo do peso')
elif imc <= 25:
  print('Peso normal')
elif imc <= 30:
  print('Acima do peso')
else:
  print('Obeso')

print(f'Seu imc é {imc}')