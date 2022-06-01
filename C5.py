#Faça um código que leia um número inteiro e imprima "É múltiplo de 3" ou "Não é múltiplo de 3".

valor = float(input('Digite um número:\n'))

if valor % 3 == 0:
  print('O valor é múltiplo de 3')
else:
  print('O valor NÃO é múltiplo de 3')