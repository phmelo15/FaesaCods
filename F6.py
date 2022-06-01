#Faça um código que leia um número e imprima a tabuada do número de 1 a 9

valor = int(input('Digite um valor:\n'))

for i in range(1, 10):
  res = valor * i
  print(f'{valor} * {i} = {res}')
  