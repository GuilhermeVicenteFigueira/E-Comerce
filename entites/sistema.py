from .carrinho import Carrinho
from .produtos import criar_produtos, mostrar_produtos, produto_existe, tem_estoque, atualizar_estoque
from .historico import Historico
from .pedidos import FilaPedidos
from .favoritos import ListaFavoritos

class ECommerce:
    def __init__(self):
        # Inicializa os dados principais da loja
        self.produtos = criar_produtos()
        self.categorias = {"Eletrônicos", "Acessórios"}
        self.info_loja = ("TechStore", "2025", "1.0")

        # Instancia os módulos principais do sistema
        self.carrinho = Carrinho()
        self.historico = Historico()
        self.pedidos = FilaPedidos()
        self.favoritos = ListaFavoritos()

    def adicionar_favorito(self, produto_id):
        # Adiciona produto aos favoritos, se existir
        if not produto_existe(self.produtos, produto_id):
            print("Produto não existe para adicionar aos favoritos.")
            return
        self.favoritos.adicionar(produto_id)
        print(f"Produto {produto_id} adicionado aos favoritos.")

    def remover_favorito(self, produto_id):
        # Remove produto dos favoritos
        if self.favoritos.remover(produto_id):
            print(f"Produto {produto_id} removido dos favoritos.")
        else:
            print("Produto não estava na lista de favoritos.")

    def listar_favoritos(self):
        # Lista todos os produtos favoritos
        ids = self.favoritos.listar()
        if not ids:
            print("Nenhum favorito adicionado.")
            return
        print("Produtos favoritos:")
        for pid in ids:
            print(f"ID {pid}: {self.produtos[pid]['nome']}")

    def adicionar_ao_carrinho(self):
        # Adiciona um produto ao carrinho, se existir e houver estoque
        mostrar_produtos(self.produtos)
        try:
            produto_id = int(input("\nID do produto: "))
            quantidade = int(input("Quantidade: "))
            if not produto_existe(self.produtos, produto_id):
                print("Produto não encontrado!")
                return
            if quantidade <= 0:  # CORREÇÃO pos prova: Verifica se quantidade é positiva
                print("Quantidade inválida! Deve ser maior que zero.")
                return
            if not tem_estoque(self.produtos, produto_id, quantidade):
                print("Estoque insuficiente!")
                return
            self.carrinho.adicionar(produto_id, quantidade)
            self.historico.adicionar(f"Adicionado: {self.produtos[produto_id]['nome']}")
            print("Produto adicionado ao carrinho!")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    def ver_carrinho(self):
        # Exibe o conteúdo do carrinho e calcula o total
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

    def finalizar_compra(self):
        # Finaliza a compra, aplica desconto e atualiza estoque
        total = self.ver_carrinho()
        if total == 0:
            return
        nome_loja, _, _ = self.info_loja
        if total >= 500:
            desconto = 50.00
            total -= desconto
            print(f"\nVocê ganhou um desconto de R$ {desconto:.2f}!")
        print(f"Valor total: R$ {total:.2f}")
        confirmar = input("Quer finalizar a compra? (s/n): ").lower()
        if confirmar == 's':
            for produto_id, quantidade in self.carrinho.listar():
                atualizar_estoque(self.produtos, produto_id, quantidade)
            pedido_id = self.pedidos.adicionar_pedido(total, self.carrinho.listar())
            self.historico.adicionar(f"Compra finalizada - R$ {total:.2f}")
            self.carrinho.limpar()
            print(f"\nCompra feita com sucesso! Seu pedido é o #{pedido_id}.")
        else:
            print("Compra cancelada.")

    def ver_historico(self):
        # Exibe as últimas ações realizadas pelo usuário
        print("\n=== Histórico de ações ===")
        acoes = self.historico.ver_ultimas()
        if not acoes:
            print("Nenhuma ação registrada.")
            return
        for i, acao in enumerate(acoes, 1):
            print(f"{i}. {acao}")

    def processar_pedido(self):
        # Processa o próximo pedido na fila
        print("\n=== Processar pedidos ===")
        if self.pedidos.esta_vazia():
            print("Nenhum pedido pendente.")
            return
        pedido = self.pedidos.processar_proximo()
        pedido_id, total, itens, data = pedido
        print(f"Processando pedido #{pedido_id} no valor de R$ {total:.2f}...")
        self.historico.adicionar(f"Processado: Pedido #{pedido_id}")

    def ver_info_sistema(self):
        # Exibe informações da loja
        print("\n=== Informação da loja ===")
        nome_loja, ano, versao = self.info_loja
        print(f"Loja: {nome_loja}")
        print(f"Ano de fundação: {ano}")
        print(f"Versão do sistema: {versao}")
        print(f"Categorias disponíveis: {', '.join(self.categorias)}")
        print(f"Total de produtos cadastrados: {len(self.produtos)}")
        print(f"Pedidos pendentes: {len(self.pedidos.ver_todos())}")
