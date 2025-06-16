class No:
    def __init__(self, produto_id, quantidade):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.proximo = None  

class Carrinho:
    def __init__(self):
        self.head = None
    
    def adicionar(self, produto_id, quantidade):
        atual = self.head
        while atual:
            if atual.produto_id == produto_id:
                atual.quantidade += quantidade
                return
            atual = atual.proximo
        
        novo_no = No(produto_id, quantidade)
        novo_no.proximo = self.head
        self.head = novo_no
    
    def listar(self):
       
        itens = []
        atual = self.head
        while atual:
            itens.append((atual.produto_id, atual.quantidade))
            atual = atual.proximo
        return itens
    
    def limpar(self):
        self.head = None
    
    def esta_vazio(self):
        return self.head is None