#Faça um código que leia uma nota mas só aceite valores acima ou igual a 0 e menores ou iguais a 10. Imprima "Valor Inválido" ou o valor

nota = float(input('Digite a sua nota:\n'))

if nota >= 0 and nota <= 10:
  print('Valor válido!')
else:
  print('Valor inválido!')