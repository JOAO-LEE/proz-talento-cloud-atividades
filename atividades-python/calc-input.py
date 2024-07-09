def calc_input():
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

calc_input()