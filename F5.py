#Faça um código que imprima todos os números primos de 2 até 100
num = 100
i = 1
cont = 0
for x in range(2, 101):
  cont = 0
  i = 1
  while i <= x:
    
    if x % i == 0:
      
      cont += 1
      
    i += 1

  if cont == 2:
    print(f'O número {x} é primo!')
  
  
    
      
      