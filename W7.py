#Faça um código que leia idades até que seja digitado 0. Imprima quantas idades maiores ou iguais a 18 foram digitadas
idadeMaior = 0
while True:
  idade = float(input('Digite a sua idade:\n'))
  if idade == 0:
    break
  if idade >= 18:
    idadeMaior += 1

print(f'Foram digitadas {idadeMaior} idades maiores que 18!')