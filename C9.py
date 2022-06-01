#Faça um programa que leia três notas e imprima: "Aprovado", se a nota for maior ou igual a sete. "Prova Final", se a nota for menor que 7.

nota1 = float(input('Informe a primeira nota\n'))
nota2 = float(input('Informe a segunda nota\n'))
nota3 = float(input('Informe a terceira nota\n'))

if nota1 >= 7 and nota2 >= 7 and nota3 >= 7:
  print('APROVADO!')
else:
  print('REPROVADO!')
  

