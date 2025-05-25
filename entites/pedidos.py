from collections import deque
from datetime import datetime

class FilaPedidos:
    def __init__(self):
        # Cria a fila de pedidos usando deque (estrutura rápida para fila).
        self.fila = deque()
    
    def adicionar_pedido(self, total, itens):
        # Adiciona um pedido novo com ID sequencial, total, itens (cópia) e data/hora atual.
        pedido = (
            len(self.fila) + 1,
            total,
            itens.copy(),
            datetime.now()
        )
        self.fila.append(pedido)  # Coloca no final da fila
        return pedido[0]          # Retorna o ID do pedido
    
    def processar_proximo(self):
        # Remove e retorna o próximo pedido da fila; retorna None se estiver vazia.
        if not self.fila:
            return None
        return self.fila.popleft()
    
    def ver_todos(self):
        # Retorna uma lista com todos os pedidos que estão na fila.
        return list(self.fila)
    
    def esta_vazia(self):
        # Retorna True se a fila estiver vazia, False caso contrário.
        return len(self.fila) == 0
