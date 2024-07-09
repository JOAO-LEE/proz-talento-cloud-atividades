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
        raise Exception("Ano deve ser maior que 1922 e menor que 2021")
      else: 
        print(f"Seu nome é {name} e você fará {2022 - birth} em 2022")
    except Exception as error:
      print(error)

calc_age()