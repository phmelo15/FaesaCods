#Faça um programa que leia dois números inteiros e imprima a média ponderada dos dois, pergunte os pesos ao usuário

valor1 = float(input('Digite o primeiro valor:\n'))
peso1 = int(input('Digite o peso do primeiro valor:\n'))
valor2 = float(input('Digite o segundo valor:\n'))
peso2 = int(input('Digite o peso do segundo valor:\n'))

media = (valor1*peso1) + (valor2*peso2) / 2
print(f'A média ponderada do primeiro e do segundo valor é igual a: {media}!')

