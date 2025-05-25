from datetime import datetime

class Historico:
    def __init__(self):
        # Inicializa a lista que funciona como pilha para armazenar o histórico de ações.
        self.pilha = []
    
    def adicionar(self, acao):
        # Registra uma nova ação no histórico, adicionando a descrição junto com o horário atual (HH:MM).
        timestamp = datetime.now().strftime("%H:%M")
        self.pilha.append(f"{acao} - {timestamp}")
    
    def ver_ultimas(self, quantidade=5):
        # Retorna as últimas 'quantidade' ações registradas, do mais recente para o mais antigo.
        # Se o histórico estiver vazio, retorna uma lista vazia.
        if not self.pilha:
            return []
        return list(reversed(self.pilha[-quantidade:]))
    
    def desfazer_ultima(self):
        # Remove e retorna a última ação registrada no histórico.
        # Se não houver ações, retorna None.
        if self.pilha:
            return self.pilha.pop()
        return None
