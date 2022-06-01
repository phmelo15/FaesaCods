#Faça um código que leia dois números inteiros, efetue a adição e caso o resultado seja maior ou igual a 10 imprima "Soma maior ou igual a 10"

valor1 = float(input('Digite o primeiro valor:\n'))
valor2 = float(input('Digite o segundo valor:\n'))

somaValores = valor1 + valor2

if somaValores >= 10:
  print('Soma maior ou igual a 10!')
else:
  print('Soma menor do que 10!')