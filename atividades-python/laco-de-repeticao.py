# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

for andar in range(20):
  if andar == 13:
    continue
  # print("Andar -", andar)

andar_counter = 0
while andar_counter < 20:
  andar_counter += 1
  if andar_counter == 13:
    continue
  # print("Andar -", andar_counter)

# Desafio 
for andar_reversed in range(20, 0, -1):
  if andar_reversed == 13:
    continue
  # print("Andar -", andar_reversed)