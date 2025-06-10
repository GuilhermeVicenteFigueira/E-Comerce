def criar_produtos():
    return {
        1: {"nome": "Smartphone", "preco": 800.00, "estoque": 10, "categoria": "Eletrônicos"},
        2: {"nome": "Notebook", "preco": 2000.00, "estoque": 5, "categoria": "Eletrônicos"},
        3: {"nome": "Fone", "preco": 150.00, "estoque": 20, "categoria": "Acessórios"},
        4: {"nome": "Mouse", "preco": 50.00, "estoque": 15, "categoria": "Acessórios"},
        5: {"nome": "Teclado", "preco": 120.00, "estoque": 8, "categoria": "Acessórios"}
    }

def adicionar_produto(produtos, categorias):
    """Adiciona um novo produto ao dicionário de produtos"""
    try:
        print("\n--- ADICIONAR NOVO PRODUTO ---")
        novo_id = max(produtos.keys()) + 1
        
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço: R$ "))
        estoque = int(input("Estoque inicial: "))
        
        print(f"\nCategorias disponíveis: {', '.join(categorias)}")
        categoria = input("Categoria: ").strip()
        
        if preco <= 0 :
            print("Erro: Preço deve ser positivo")
            return False
        if estoque < 0:
            print("Erro: Estoque não pode ser negativo!")
            return False
        if categoria not in categorias:
            print("Erro: Categoria inválida!")
            return False
            
        produtos[novo_id] = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque,
            "categoria": categoria
        }
        
        print(f"\n✅ Produto '{nome}' adicionado com sucesso! ID: {novo_id}")
        return True
        
    except ValueError:
        print("Erro: Valores inválidos para preço ou estoque!")
        return False

def mostrar_produtos(produtos):
    print("\n PRODUTOS: ")
    print("ID | Nome         | Preço     | Estoque | Categoria")
    print("-" * 60)
    for produto_id, dados in produtos.items():
        print(f"{produto_id:<3}| {dados['nome']:<12} | R$ {dados['preco']:<6.2f} | {dados['estoque']:<7} | {dados['categoria']}")

def produto_existe(produtos, produto_id):
    return produto_id in produtos

def tem_estoque(produtos, produto_id, quantidade):
    return produtos[produto_id]["estoque"] >= quantidade

def atualizar_estoque(produtos, produto_id, quantidade):
    produtos[produto_id]["estoque"] -= quantidade