# Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram. O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

# Como desafio opcional, tente imprimir cada produto com a frase "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!"). 

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

lista_produtos_tamanho = len(lista_produtos)

# Com laço `while`:
contador = 0
while contador < lista_produtos_tamanho:
  print(f"Temos {lista_produtos[contador]} à venda!")
  contador += 1

# Com laço `for`:
for index in range(lista_produtos_tamanho):
  print(f"Temos {lista_produtos[index]} à venda!")