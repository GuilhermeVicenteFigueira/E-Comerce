from entites.carrinho import Carrinho
from entites.produtos import criar_produtos, produto_existe, tem_estoque, atualizar_estoque
from entites.historico import Historico
from entites.pedidos import FilaPedidos
from entites.favoritos import ListaFavoritos
from entites.mais_vendidos import MaisVendidos

class ECommerce:
    def __init__(self):
        self.produtos = criar_produtos()
        self.vendas_por_produto = {}
        self.categorias = {"Eletrônicos", "Acessórios"}
        self.info_loja = ("TechStore", "2025", "1.0")

        self.carrinho = Carrinho()
        self.historico = Historico()
        self.pedidos = FilaPedidos()
        self.favoritos = ListaFavoritos()
        self.mais_vendidos = MaisVendidos()

    def adicionar_favorito(self, produto_id):
        if not produto_existe(self.produtos, produto_id):
            print("Produto não existe para adicionar aos favoritos.")
            return
        self.favoritos.adicionar(produto_id)
        print(f"Produto {produto_id} adicionado aos favoritos.")

    def remover_favorito(self, produto_id):
        if self.favoritos.remover(produto_id):
            print(f"Produto {produto_id} removido dos favoritos.")
        else:
            print("Produto não estava na lista de favoritos.")

    def listar_favoritos(self):
        ids = self.favoritos.listar()
        if not ids:
            print("Nenhum favorito adicionado.")
            return
        print("Produtos favoritos:")
        for pid in ids:
            print(f"ID {pid}: {self.produtos[pid]['nome']}")

    def adicionar_ao_carrinho(self, produto_id=None, quantidade=None):
        if produto_id is None:
            try:
                produto_id = int(input("Digite o ID do produto para adicionar ao carrinho: "))
                quantidade = int(input("Digite a quantidade: "))
            except ValueError:
                print("ID ou quantidade inválidos!")
                return
        
        if not produto_existe(self.produtos, produto_id):
            print("Produto não encontrado!")
            return
        if not tem_estoque(self.produtos, produto_id, quantidade):
            print("Estoque insuficiente!")
            return
        self.carrinho.adicionar(produto_id, quantidade)
        self.historico.adicionar(f"Adicionado: {self.produtos[produto_id]['nome']}")
        print("Produto adicionado ao carrinho!")

    def ver_carrinho(self):
        print("\n=== CARRINHO ===")
        if self.carrinho.esta_vazio():
            print("Carrinho vazio!")
            return 0

        total = 0
        print("Produto      | Qtd | Preço   | Subtotal")
        print("-" * 40)
        for produto_id, quantidade in self.carrinho.listar():
            produto = self.produtos[produto_id]
            subtotal = produto["preco"] * quantidade
            total += subtotal
            print(f"{produto['nome']:<12} | {quantidade:<3} | R${produto['preco']:<6.2f} | R$ {subtotal:.2f}")
        print("-" * 40)
        print(f"TOTAL: R$ {total:.2f}")
        return total

    def finalizar_compra(self, confirmar=True):
        total = self.ver_carrinho()
        if total == 0:
            return
        if total >= 500:
            desconto = 50.00
            total -= desconto
            print(f"\nVocê ganhou um desconto de R$ {desconto:.2f}!")
        print(f"Valor total: R$ {total:.2f}")
        if confirmar:
            for produto_id, quantidade in self.carrinho.listar():
                atualizar_estoque(self.produtos, produto_id, quantidade)
                self.mais_vendidos.registrar_venda(produto_id, quantidade)
            pedido_id = self.pedidos.adicionar_pedido(total, self.carrinho.listar())
            self.historico.adicionar(f"Compra finalizada - R$ {total:.2f}")
            self.carrinho.limpar()
            print(f"\nCompra feita com sucesso! Seu pedido é o #{pedido_id}.")
        else:
            print("Compra cancelada.")

    def ver_mais_vendidos(self):
        print("\n=== Produtos Mais Vendidos ===")
        self.mais_vendidos.listar_mais_vendidos(self.produtos)

    def ver_historico(self):
        print("\n=== Histórico de ações ===")
        acoes = self.historico.ver_ultimas()
        if not acoes:
            print("Nenhuma ação registrada.")
            return
        for i, acao in enumerate(acoes, 1):
            print(f"{i}. {acao}")

    def processar_pedido(self):
        print("\n=== Processar pedidos ===")
        if self.pedidos.esta_vazia():
            print("Nenhum pedido pendente.")
            return
        pedido = self.pedidos.processar_proximo()
        pedido_id, total, itens, data = pedido
        print(f"Processando pedido #{pedido_id} no valor de R$ {total:.2f}...")
        self.historico.adicionar(f"Processado: Pedido #{pedido_id}")

    def ver_info_sistema(self):
        print("\n=== Informação da loja ===")
        nome_loja, ano, versao = self.info_loja
        print(f"Loja: {nome_loja}")
        print(f"Ano de fundação: {ano}")
        print(f"Versão do sistema: {versao}")
        print(f"Categorias disponíveis: {', '.join(self.categorias)}")
        print(f"Total de produtos cadastrados: {len(self.produtos)}")
        print(f"Pedidos pendentes: {len(self.pedidos.ver_todos())}")