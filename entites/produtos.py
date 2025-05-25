def criar_produtos():
    # Cria e retorna um dicionário com produtos da loja.
    # Cada produto tem: nome, preço e estoque.
    return {
        1: {"nome": "Smartphone", "preco": 800.00, "estoque": 10},
        2: {"nome": "Notebook", "preco": 2000.00, "estoque": 5},
        3: {"nome": "Fone", "preco": 150.00, "estoque": 20},
        4: {"nome": "Mouse", "preco": 50.00, "estoque": 15},
        5: {"nome": "Teclado", "preco": 120.00, "estoque": 8}
    }

def mostrar_produtos(produtos):
    # Exibe os produtos disponíveis na loja com seus dados formatados.
    print("\n PRODUTOS: ")
    print("ID | Nome         | Preço     | Estoque")
    print("-" * 40)
    for produto_id, dados in produtos.items():
        print(f"{produto_id:<3}| {dados['nome']:<12} | R$ {dados['preco']:<6.2f} | {dados['estoque']}")

def produto_existe(produtos, produto_id):
    # Verifica se um produto com o ID informado está cadastrado.
    return produto_id in produtos

def tem_estoque(produtos, produto_id, quantidade):
    # Verifica se o estoque do produto é suficiente para a quantidade desejada.
    return produtos[produto_id]["estoque"] >= quantidade

def atualizar_estoque(produtos, produto_id, quantidade):
    # Subtrai a quantidade vendida do estoque do produto.
    produtos[produto_id]["estoque"] -= quantidade
