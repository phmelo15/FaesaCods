#Faça um código que leia idades até que seja digitado 0. Calcule a média de idades de quem possui mais que 21 anos e imprima
soma = 0
i = 0
while True:
  idade = float(input('Digite a sua idade:\n'))
  if idade == 0:
    break
  if idade >= 21:
    i += 1
    soma += idade

media = soma / i
print(f'A média das pessoas que possuem mais de 21 anos é igual a: {media}')