# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculator(num_one, num_two, operation):
  if operation == "+":
    return num_one + num_two
  elif operation == "-":
    return num_one - num_two
  elif operation == "*":
    return num_one * num_two
  elif operation == "/":
    return num_one / num_two
  else:
    return 0

# print(calculator(244, 2, "-"))

# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair
# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.
# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

def calculator_input():
  running = True
  while running:
    print("Digite a operação")
    print("1: Soma \
            2: Subtração \
            3: Multiplicação \
            4: Divisão \
            0: Sair")
    operation = int(input())
    if operation == 0:
      running = False
      break
    if operation > 4:
      print("Essa opção não existe.")
    else: 
      print("Digite o primeiro número:")
      num_one = int(input())
      print("Digite o segundo número:")
      num_two = int(input())

    if operation == 1:
        print(f"O resultado da operação é: {num_one + num_two}")
    elif operation == 2:
      print(f"O resultado da operação é: {num_one - num_two}")
    elif operation == 3:
      print(f"O resultado da operação é: {num_one * num_two}")
    elif operation == 4:
      if num_two == 0:
        print("Não é possível dividir por zero.")
      else: 
        print(f"O resultado da operação é: {num_one / num_two}")

# calculator_input()