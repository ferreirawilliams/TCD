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
		lista_de_Produtos.append([nome, quantidade, preço])
		Arquivo_Mercadoria.write('Nome: ' + nome +' | ' + 'Quantidade: '+ quantidade + ' | ' + 'Preço: '+ preço + '\n')
	Arquivo_Mercadoria.close()
	return adiciona

#Função que modifica dados do estoque se ele optar por modificar
def modificar():
	Arquivo_Mercadoria = open('Arquivo_Mercadoria.txt', 'r', encoding='UTF-8')
	quant_produto = int(input('Digite a Quantidade de tipos de produtos que deseja modificar: '))
	#Aqui cada linha do arquivo vira um indice da lista criada no readlines
	lista_de_Produtos = Arquivo_Mercadoria.readlines()
	
	# Esse 'for' pega cada linha da lista e cria indices de cada elemento da linha separado por virgula
	for i in lista_de_Produtos:
		lista = i.split()
		print(lista)
	"""print('OK!')
	for i in range(quant_produto):
		nome = input('Digite o nome do produto que deseja modificar: ').title()
		modificar_ = input('OK! O que deseja modificar em ' + nome + ':' ).lower()
		if modificar_ == 'nome': 
			new_name = input('Digite um novo nome: ')
			lista.pop(1)
			lista.insert(1,new_name)
			
		if modificar_ == 'quantidade':
			new_quant = input('Digite uma nova quantidade: ')
			lista.pop(4)
			lista.insert(4,new_quant)
			print(lista)
			
		if modificar_ == 'preço':
			new_prec = input('Digite o novo preço: ')
			lista.pop(7)
			lista.insert(7,new_prec)
			print(lista)
		
	
		print(lista_modificada)"""
	Arquivo_Mercadoria.close()
	#Arquivo_Mercadoria = open('Arquivo_Mercadoria.txt', 'w', encoding='UTF-8')
	#for i in lista_modificada:
	#	Arquivo_Mercadoria.write(i)
	return modificar

if pergunta == 'a':
	adiciona()

if pergunta == 'm':
	modificar()
