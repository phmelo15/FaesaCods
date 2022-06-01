#Faça um programa que leia dois números inteiros e imprima a média ponderada dos dois, considere os pesos 3 e 4

valor1 = float(input('Digite o primeiro valor:\n'))
valor2 = float(input('Digite o segundo valor:\n'))

soma = valor1*3 + valor2*4
media = soma / 2
print(f'A média dos dois valores é igual a: {media}')