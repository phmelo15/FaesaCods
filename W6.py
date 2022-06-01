#Faça um código que leia valores até que seja digitado 0. Imprima o menor valor digitado

valorAux = []

while True:
  valor = float(input('Digte um valor:\n'))
  if valor == 0:
    break
  valorAux.append(valor)

maiorValor = min(valorAux)
print(f'O maior valor dos que foram digitados é igual a: {maiorValor}')