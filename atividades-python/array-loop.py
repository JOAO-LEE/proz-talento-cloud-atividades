# Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram. O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

# Como desafio opcional, tente imprimir cada produto com a frase "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!"). 

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

lista_produtos_tamanho = len(lista_produtos)
contador_um = 0
contador_dois = 0

# Com laço `while`:
while contador_um < lista_produtos_tamanho:
  print(lista_produtos[contador_um])
  contador_um +=1

# Com laço `while` e com a frase pedida:
while contador_dois < lista_produtos_tamanho:
  print(f"Temos {lista_produtos[contador_dois]} à venda!")
  contador_dois += 1

# Com laço `for`:
for index in range(lista_produtos_tamanho):
  print(lista_produtos[index])

# Com laço `for` com a frase pedida:
for index in range(lista_produtos_tamanho):
  print(f"Temos {lista_produtos[index]} à venda!")