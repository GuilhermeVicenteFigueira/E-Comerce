class NoFavorito:
    def __init__(self, produto_id):
        # Nó que guarda o id do produto favorito e aponta para o nó anterior e o próximo na lista.
        self.produto_id = produto_id
        self.anterior = None  # referência para o nó anterior
        self.proximo = None   # referência para o próximo nó

class ListaFavoritos:
    def __init__(self):
        # Lista duplamente ligada inicialmente vazia (sem primeiro e último elemento).
        self.inicio = None
        self.fim = None

    def adicionar(self, produto_id):
        # Cria um novo nó para o produto e o adiciona no fim da lista.
        novo = NoFavorito(produto_id)
        if not self.inicio:
            # Se a lista está vazia, o novo nó é o início e o fim.
            self.inicio = self.fim = novo
        else:
            # Liga o último nó atual ao novo e atualiza o fim da lista.
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo
        print(f"Produto {produto_id} adicionado aos favoritos.")

    def remover(self, produto_id):
        # Percorre a lista para encontrar o nó com o produto e remove-o, ajustando os links.
        atual = self.inicio
        while atual:
            if atual.produto_id == produto_id:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    # Se for o primeiro nó, atualiza o início da lista.
                    self.inicio = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    # Se for o último nó, atualiza o fim da lista.
                    self.fim = atual.anterior

                print(f"Produto {produto_id} removido dos favoritos.")
                return
            atual = atual.proximo
        print("Produto não está na lista de favoritos.")

    def listar(self):
        # Retorna uma lista com os ids dos produtos favoritos na ordem em que foram adicionados.
        favoritos = []
        atual = self.inicio
        while atual:
            favoritos.append(atual.produto_id)
            atual = atual.proximo
        return favoritos
