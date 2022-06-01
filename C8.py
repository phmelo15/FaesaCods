#Faça um programa que leia três números e imprima o maior deles.

valor1 = float(input('Informe o primeiro valor:\n'))
valor2 = float(input('Informe o segundo valor:\n'))
valor3 = float(input('Informe o terceiro valor:\n'))

if valor1 >= valor2 and valor1 >= valor3:
  print(f'O maior valor informado é o: valor1')

if valor2 >= valor1 and valor2 >= valor3:
  print(f'O maior valor informado é o: valor2')

if valor3 >= valor2 and valor3 >= valor1:
  print(f'O maior valor informado é o: valor3')
