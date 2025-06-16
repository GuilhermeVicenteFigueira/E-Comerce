class MaisVendidos:
    def __init__(self):
        self.vendas_por_produto = {}

    def registrar_venda(self, produto_id, quantidade):
        if produto_id in self.vendas_por_produto:
            self.vendas_por_produto[produto_id] += quantidade
        else:
            self.vendas_por_produto[produto_id] = quantidade

    def listar_mais_vendidos(self, produtos, limite=5):
        if not self.vendas_por_produto:
            print("Nenhuma venda registrada ainda.")
            return

        print(f"\n=== Top {limite} Produtos Mais Vendidos ===")
        mais_vendidos = sorted(self.vendas_por_produto.items(), key=lambda item: item[1], reverse=True)

        for i, (produto_id, total_vendido) in enumerate(mais_vendidos[:limite], start=1):
            nome = produtos[produto_id]["nome"]
            print(f"{i}. {nome} - {total_vendido} unidades vendidas")