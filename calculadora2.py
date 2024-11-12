
# Solicitando os 2 valores
contador = 'não'
while contador == 'não':

  valora = float(input('Digite um valor:'))
  valorb = float(input('Digite outro valor:'))
  operador = input('Digite a operação matemática:')

# Designando os operadores
  if operador == 'soma' or operador == '+':
    soma = valora + valorb 
    print('O resultado é:',soma)

  elif operador == 'subtração' or operador == '-':
    subtracao = valora - valorb
    print('O resultado é:',subtracao) 

  elif operador == 'divisão' or operador == '/':
    divisao = valora / valorb
    print('O resultado é:',divisao)

  elif operador == 'multiplicação' or operador == '*':
    multiplicacao = valora * valorb
    print('O resultado é:',multiplicacao)

# Criando o loop (repetir a operação)
  contador = input('Deseja sair do programa?')
 
else:
    print('Obrigado por usar a calculadora!')