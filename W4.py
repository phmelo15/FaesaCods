#Faça um código que leia valores até que seja digitado 0. Imprima quantos itens foram lidos e qual a média dos valores
soma = 0
i = 0
while True:
  valor = float(input('Digite um valor:\n'))
  if valor == 0:
    break
  soma += valor
  i += 1
media = soma / i
print(f'A média das notas foi igual a: {media}')
