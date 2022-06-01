#Faça um código que pergunte a altura e peso do usuário e imprima o IMC.

pesoPessoa = float(input('Digite o seu peso atual:\n'))
alturaPessoa = float(input('Digite a sua altura atual em metros:\n'))

imc = pesoPessoa / (alturaPessoa**2)

print(f'O seu imc atual é de {imc}')


