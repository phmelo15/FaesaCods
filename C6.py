#Faça um código que leia um número e informar se ele é divisível por 10, por 7, por 5, por 3, por 2 ou se não é divisível por nenhum destes.

valor = float(input('Digite um número:\n'))

if valor % 10 == 0 or valor % 7 == 0 or valor % 5 == 0 or valor % 3 == 0 or valor % 2 == 0:
  print('O valor é divisível por 10 ou 7 ou 5 ou 3 ou 2!')
else:
  print('O valor não é divisível por nenhum destes números!')