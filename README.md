# TechStore - Sistema de E-commerce em Python

Este projeto desenvolve um sistema de e-commerce simples em Python, operando via
terminal e fundamentado em Programação Orientada a Objetos (POO) e estruturas de dados
clássicas. O principal objetivo é fornecer um ambiente controlado para experimentação
e aplicação prática de conceitos acadêmicos em um contexto de loja virtual.

## 1. Objetivos
1.1. Modularizar o código em componentes coesos e independentes.
1.2. Implementar estruturas de dados como pilha (para histórico) e fila (para pedidos).
1.3. Aplicar os princípios de encapsulamento, herança e polimorfismo da POO.
1.4. Simular operações de uma loja virtual: consulta, adição, remoção, finalização.
1.5. Gerenciar estoque e descontos com regras de negócio definidas.

## 2. Organização do Projeto
O repositório apresenta a seguinte estrutura:
```
e-commerce/
├── entities
├── main.py # Ponto de entrada da aplicação, interface via terminal
├── sistema.py # Classe ECommerce, orquestra os módulos
├── carrinho.py # Classe Carrinho: adicionar, listar, limpar itens
├── produtos.py # Funções para criar catálogo, validar e atualizar estoque
├── historico.py # Classe Historico: armazena ações recentes em pilha
├── pedidos.py # Classe FilaPedidos: gerencia fila FIFO de pedidos
├── favoritos.py # Gerencia lista ligada de produtos favoritos
└── README.md # Documentação detalhada do projeto
```

### 2.1 main.py
- Responsável por apresentar o menu de opções ao usuário.
- Recebe entradas de teclado e aciona métodos da classe ECommerce.

### 2.2 carrinho.py
- Gerencia operações do carrinho de compras:
  - adicionar(produto_id, quantidade)
  - listar() retorna lista de tuplas (id, qtd)
  - esta_vazio() verifica se há itens
  - limpar() esvazia o carrinho

### 2.3 produtos.py
- Contém funções utilitárias:
  - criar_produtos() retorna dicionário inicial de produtos
  - mostrar_produtos() exibe catálogo formatado
  - produto_existe() valida ID
  - tem_estoque() verifica disponibilidade
  - atualizar_estoque() decrementa estoque após venda

### 2.4 historico.py
- Importa a bilioteca datetime para verificar o tempo no historico 
- Implementa histórico com pilha:
  - adicionar(acao) empilha ação
  - ver_ultimas() retorna sequência de ações

### 2.5 pedidos.py
- Importa a biblioteca datetime para veririfcar o tempo do pedido
- Implementa fila FIFO para pedidos:
  - adicionar_pedido(valor, itens) enfileira dados
  - esta_vazia() verifica se há pedidos pendentes
  - processar_proximo() dequeues e retorna tupla(pedido_id, total, itens, data)

## 3. Funcionalidades
3.1 Ver produtos
- Visualização de lista completa com filtros por categoria (potencial).
- Exibição de atributos: ID, nome, categoria, preço e estoque.

3.2 Adicionar ao Carrinho
- Entrada de ID e quantidade via CLI.
- Validação imediata de existência e estoque.
- Registro da ação no histórico.

3.3 Ver Carrinho
- Impressão de tabela com colunas: produto, quantidade, preço unitário, subtotal.
- Cálculo e exibição do total acumulado.

3.4 Finalizar Compra
- Cálculo de desconto fixo (R$ 50) para compras ≥ R$ 500.
- Solicitação de confirmação ao usuário.
- Atualização de estoque e geração de pedido na fila.
- Limpeza do carrinho e registro da ação.

3.5 Histórico de Ações
- Visualização das últimas N ações em ordem LIFO.
- Auxilia em auditoria de operações do usuário.

3.6 Processar Pedidos
- Operação manual que simula atendimento FIFO.
- Atualização do histórico após processamento.

3.7 Informações do Sistema
- Exibição de metadados: nome da loja, ano, versão.
- Estatísticas: número total de produtos e pedidos pendentes.

3.8 favoritos.py
Gerencia os produtos favoritos do usuário usando uma lista ligada.

- NoFavorito: representa um item da lista com o ID do produto.
- ListaFavoritos: controla a lista com funções para:
 - adicionar(produto_id) — colocar produto no final da lista.
 - remover(produto_id) — tirar produto da lista.
 - listar() — mostrar todos os produtos favoritos na ordem.

3.0 Sair
- Retorna mensagem de logout do sistema.

3.X Erro
- Retrona mesagem de erro.

## 4. Exemplo de Execução
```
$ python main.py
=== MENU ===
1. Ver produtos
2. Adicionar ao carrinho
3. Ver carrinho
4. Finalizar compra
5. Ver histórico
6. Processar pedido
7. Informações do sistema
8. Adicionar produto aos favoritos
9. Remover produto dos favoritos
10.Listar favoritos
0. Sair

# Escolha 1 para listar produtos
# Escolha 2 e informe ID e quantidade
# Saiba que versões futuras podem incluir mais opções
```

## 5. Requisitos e Instalação
- Python >= 3.8
- Dependências padrão da biblioteca Python (sem pacotes externos)

### Passos para execução
1. Clonar repositório: `git clone <url>`
2. Navegar até a pasta: `cd e-commerce`
3. Executar: `python main.py`

## 6. Aplicações Acadêmicas
- Ferramenta de estudo de POO para disciplinas de graduação
- Exemplo prático de uso de pilha e fila em Python
- Exemplo de estrutura da dados simples ao internmediario
- Base para trabalhos de laboratório e exercícios de programação
- Exposição de boas práticas de modularização e documentação

## 7. Possibilidades de Expansão
- Persistência com SQLite (Banco de dados)
- Autenticação e autorização de usuários
- API RESTful para integração externa
- Interface web com Django
- Relatórios de vendas e dashboard de estoque
- Sistema de cupons e promoções avançadas
- Internacionalização e suporte a múltiplas moedas
- Testes unitários e cobertura com pytest
- Containerização com Docker
- Implementação de CI/CD
- Monitoramento de logs e métricas

## 8. Conclusão
Este projeto demonstra a aplicação integrada de conceitos fundamentais da ciência
da computação e análise desenvolvimento de sistemas, proporcionando um exemplo "realista" de sistema de e-commerce.
A abordagem modular e orientada a objetos facilita a manutenção e evolução do código,
enquanto o uso de pilha e fila evidencia a importância de estruturas de dados eficientes.
Como material acadêmico, o sistema serve de base para atividades de laboratório e
projetos de extensão, além de oferecer subsídios para estudo de padrões de projeto
e boas práticas do desenvolvimento de software.

## Autor
Guilherme Vicente Figueira: RA 1992017
Gabriel Forconi: RA 1990563
Issac Castro Moreira Cavalcante: RA 1993141
João Pedro Messias: RA 1993720

## Fluxograma

https://excalidraw.com/#json=-_-MHWMRl9NoS3OISSlgz,N65q3L9wvBy0Mja54ReNMQ
