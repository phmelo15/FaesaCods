#Faça um código para ler um número e imprimi-lo caso seja múltiplo de 5

num1 = float(input('Digite um número:\n'))

if num1 % 5 == 0:
  print(f'O número {num1}, é múltiplo de 5!')
else:
  print(f'O número {num1}, NÃO é multiplo de 5!')