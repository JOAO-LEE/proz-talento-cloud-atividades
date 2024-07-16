# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def calc_age():
  running = True
  while running:
    try:
      print("Insira seu nome:")
      name = input()
      print("Insira o seu ano de nascimento:")
      birth = int(input())
      if birth < 1922 or birth > 2021:
        print("Ano deve ser maior que 1922 e menor que 2021")
      else: 
        print(f"Seu nome é {name} e você fará {2022 - birth} em 2022")
    except:
      print("O ano deve ser um valor numérico válido!")

# calc_age()


# for i in range(5, 0, -1):
  # print(f"Regando planta {i}")




# counter = 5
# while counter >= 0:
#   print(f"Regando planta {counter}")
#   counter -= 1


# def tabuada(num):
#   counter = 0
#   while counter <= 10:
#     print(f"{num} X {counter} = {num * counter}")
#     counter += 1
# tabuada(2)


# def mostrarNumero():
#   numero_valido = False
#   while(numero_valido == False):
#     try:
#       num = int(input())
#       if num % 2 == 1:
#         print("Número não é par :/")
#       elif num % 3 > 0 or num == 2:
#         print("Número não é divísivel por três")
#       else:
#         numero_valido= True
#         print(f"O número {num} é par e divísivel por 3 :D")
#     except:
#       print("Precisa digitar um número par")

# mostrarNumero()