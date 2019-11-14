print('Olá')
pergunta = input('Voce deseja adicionar ou modificar seu estoque [A] ou [M]: ').lower()

#Função que adiciona dados no estoque se ele optar por adicionar 
def adiciona():
	Arquivo_Mercadoria = open('Arquivo_Mercadoria.txt', 'a', encoding='UTF-8')
	quant_produto = int(input('Digite a Quantidade de tipos de produtos que deseja adicionar: '))

	lista_de_Produtos = []
	print('OK!')	
	for i in range(quant_produto):
		nome = input('Digite o nome do produto que deseja adicionar: ').title()
		quantidade = input('Digite a Quantidade de ' + nome +'s' + ' que deseja adicionar: ')
		preço = input('Digite o preço de ' + nome + ':')
		print('OK!')
		lista_de_Produtos.append([nome, quantidade])
		Arquivo_Mercadoria.write('Nome: ' + nome +'|' + 'Quantidade: '+ quantidade + '|' + 'Preço: '+ preço + '\n')
	Arquivo_Mercadoria.close()
	return adiciona

#Função que modifica dados do estoque se ele optar por modificar
def modificar():
	Arquivo_Mercadoria = open('Arquivo_Mercadoria.txt', 'r', encoding='UTF-8')
	quant_produto = int(input('Digite a Quantidade de tipos de produtos que deseja modificar: '))
	
	lista_de_Produtos = Arquivo_Mercadoria.readlines()
	print('OK!')
	for i in range(quant_produto):
		nome = input('Digite o nome do produto que deseja modificar: ').title()
		modificar_ = input('OK! O que deseja modificar em ' + nome + ':' ).lower()
		if modificar_ == 'nome': 
			new_name = input('Digite um novo nome: ')

		if modificar_ == 'quantidade':
			new_quant = input('Digite uma nova quantidade: ')

		if modificar_ == 'preço':
			new_prec = input('Digite o novo preço: ')

	Arquivo_Mercadoria = open('Arquivo_Mercadoria.txt', 'w', encoding='UTF-8')
	for j in lista_de_Produtos:
		Arquivo_Mercadoria.write(j + '\n')

	Arquivo_Mercadoria.close()
	Arquivo_Mercadoria.close()
	return modificar

if pergunta == 'a':
	adiciona()

if pergunta == 'm':
	modificar()
