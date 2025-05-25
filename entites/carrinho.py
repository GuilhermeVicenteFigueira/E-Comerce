class No:
    def __init__(self, produto_id, quantidade):
        # Nó que representa um produto no carrinho, com id e quantidade.
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.proximo = None  # Próximo nó na lista ligada

class Carrinho:
    def __init__(self):
        # Inicializa o carrinho vazio (lista ligada sem elementos).
        self.head = None
    
    def adicionar(self, produto_id, quantidade):
        # Se o produto já está no carrinho, soma a quantidade.
        atual = self.head
        while atual:
            if atual.produto_id == produto_id:
                atual.quantidade += quantidade
                return
            atual = atual.proximo
        
        # Caso contrário, cria um novo nó e insere no início da lista.
        novo_no = No(produto_id, quantidade)
        novo_no.proximo = self.head
        self.head = novo_no
    
    def listar(self):
        # Retorna lista com (produto_id, quantidade) de todos os itens do carrinho.
        itens = []
        atual = self.head
        while atual:
            itens.append((atual.produto_id, atual.quantidade))
            atual = atual.proximo
        return itens
    
    def limpar(self):
        # Remove todos os itens do carrinho.
        self.head = None
    
    def esta_vazio(self):
        # Retorna True se o carrinho estiver vazio, False caso contrário.
        return self.head is None
