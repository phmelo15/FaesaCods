#Faça um programa que leia um valor inteiro N calcule a soma da série: S = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/N
soma = 0

while True:
  N = int(input('Digite o valor de um número inteiro:\n'))
  if N < 0:
    break
  for i in range(1, N + 1):
    soma += 1 / i
  
  print(soma)

print('Fim da aplicação!')