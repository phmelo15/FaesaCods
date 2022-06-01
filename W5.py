#Faça um código que leia valores até que seja digitado 0. Imprima o maior valor digitado
valorAux = []

while True:
  valor = float(input('Digte um valor:\n'))
  valorAux.append(valor)
  if valor == 0:
    break

maiorValor = max(valorAux)
print(f'O maior valor dos que foram digitados é igual a: {maiorValor}')