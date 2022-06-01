#Faça um programa que leia dois números e imprima o maior deles

valor1 = float(input('Digite o primeiro valor:\n'))
valor2 = float(input('Digite o segundo valor:\n'))

if valor1 > valor2:
  print(f'O primeiro valor é maior que o segundo!')

elif valor1 == valor2:
  print(f'Os valores são iguais!')
  
else:
  print('O segundo valor é maior que o primeiro!')