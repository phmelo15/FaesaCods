#A fórmula de Leibniz pode ser utilizada para calcular um valor aproximado de Pi. Faça um código que leia um valor N e calcule o valor de Pi seguindo a série: Pi = 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 ...). Dica: para inverter o sinal você pode usar (-1) elevado a N

N = int(input('Digite um valor para N\n'))
denominador = 1
pi = 0

for i in range(N):
  if i % 2 == 0:
    pi += 4/denominador
    denominador += 2
  else:
    pi -= 4/denominador
    denominador += 2

print(f'O valor de pi aproximado é {pi}')