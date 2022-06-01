#Vamos fazer um menu de caixa eletrônico, executando em loop até que o usuário peça para sair. Suponha que o saldo inicial seja R$1000. O usuário deverá digitar qual item do menu para prossegir. Imprima: """
saldo = 1000
while True:
  
  while True:
    escolha = int(input('[1] - Ver saldo atual\n[2] - Sacar dinheiro\n[3] - Depositar dinheiro\n[4] - Sair\n'))
    if escolha != 1 or escolha != 2 or escolha != 3 or escolha != 4:
      break
      
  if escolha == 1:
    print(f'O seu saldo atual é {saldo}')
    
  elif escolha == 2:
    while True:
      sacarDinheiro = float(input('Digite o saldo que deseja sacar:\n'))
      if sacarDinheiro <= saldo:
        print(f'Você sacou R${sacarDinheiro}')
        saldo -= sacarDinheiro
        break
      print('Seu saldo não é o suficiente')
        
  elif escolha == 3:
    depositarDinheiro = float(input('Digite o valor que deseja colocar:\n'))
    print(f'Você depositou R${depositarDinheiro}!')
    saldo += depositarDinheiro
    
  elif escolha == 4:
    print('Fim da operação!')
    break
  
    