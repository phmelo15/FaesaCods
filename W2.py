#Faça um código que leia uma altura mas só aceite valores maiores que 0 e menores que 3. Imprima "Valor Inválido" ou o valor

while True:
  altura = float(input('Digite a sua altura:\n'))
  if altura >= 0 and altura <= 3:
    print('Valor válido!')
    break
  else:
    print('Valor inválido!')