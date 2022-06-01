#Faça um programa para ler o salário bruto e imprima o valor devido do imposto. Salário Bruto * Alíquota - Valor a deduzir

salarioBruto = float(input('Informe o seu salário bruto:\n'))

if salarioBruto <= 1903.98:
  print(f'Salário liquido de {salarioBruto}, isento e 0 valor a deduzir')
elif salarioBruto <= 2826.65:
  imposto = salarioBruto * 0.07 - 142.80
  print(f'O imposto relacionado ao salario de {salarioBruto} é {imposto}')
elif salarioBruto <= 3751.05:
  imposto = salarioBruto * 0.15 - 354.80
  print(f'O imposto relacionado ao salario de {salarioBruto} é {imposto}')
elif salarioBruto <= 4664.68:
  imposto = salarioBruto * 22.5 - 636,13
  print(f'O imposto relacionado ao salario de {salarioBruto} é {imposto}')
else:
  imposto = salarioBruto * 27.5 - 869,36
  print(f'O imposto relacionado ao salario de {salarioBruto} é {imposto}')