#Leia duas notas de um aluno, informe a sua média. Seu programa deve forçar ao usuário a digitar notas na faixa de 0 a 10, informando "Valor inválido" no caso de nota inválida.

while True:
  nota1 = float(input('Digite sua nota de 0 a 10:\n'))
  nota2 = float(input('Digite sua nota de 0 a 10:\n'))
  if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    break
  print('Notas inválidas!')
  
media = (nota1 + nota2) / 2

print(f'A média das notas é igual a: {media}')
    

  
  
  