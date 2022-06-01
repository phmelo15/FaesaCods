#Faça um código que leia dois números inteiros, efetue a adição e caso o resultado seja maior que 20 imprima o valor somado a 8

valor1 = int(input('Digite o primeiro valor:\n'))
valor2 = int(input('Digite o segundo valor:\n'))

adicao = valor1 + valor2

if adicao > 20:
  print(f'O valor da adição somado a 8 é igual a {adicao+8}')
else:
  print('Fim do programa!')