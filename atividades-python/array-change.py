# A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. 
# Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

lista_produtos[1] = "rímel"
print(lista_produtos)
lista_produtos[4] = "cremes hidratantes"
print(lista_produtos)

lista_produtos.pop()
print(lista_produtos)

# Como desafio, adicione dois novos produtos da sua escolha à lista. 

lista_produtos.append("liptint")
lista_produtos.append("paleta de cores")
print(lista_produtos)

