#Vamos fazer um sistema de ingressos de Cinema. Pergunte a idade até que a pessoa digite 0 para sair. Se a pessoa tiver menos que 10 anos ou mais que 60 informe "Meia Entrada" se não, informe "Inteira". Ao terminar imprima: "Total de x ingressos vendidos, sendo y meia entrada"
x = 0
y = 0
while True:
  idade = float(input('Digite a sua idade:\n'))
  if idade == 0:
    break
  x += 1
  if idade <= 10 or idade >= 60:
    y += 1
    print('Meia entrada!')
  else:
    print('Interia!')

print(f'O total de ingressos vendidos foram de {x} ingressos, sendo {y} meias entradas.')