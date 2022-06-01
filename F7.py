#Faça um código, usando dois loops for, que imprima o triangulo abaixo, dica: procure pelo parametro end do print
valores = []
for i in range(9, 0, -1):
  valores.append(i)

while len(valores) >= 1:
  print(valores)
  del valores[0]