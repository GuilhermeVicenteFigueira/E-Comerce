from entites.sistema import ECommerce

def main():
    loja = ECommerce()
    
    print("=== BEM-VINDO À TECHSTORE ===")
    
    while True:
        print("\n=== MENU ===")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Ver histórico")
        print("6. Processar pedido")
        print("7. Info do sistema")
        print("8. Adicionar produto aos favoritos")
        print("9. Remover produto dos favoritos")
        print("10. Listar favoritos")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            from entites.produtos import mostrar_produtos
            mostrar_produtos(loja.produtos)
        elif opcao == '2':
            loja.adicionar_ao_carrinho()
        elif opcao == '3':
            loja.ver_carrinho()
        elif opcao == '4':
            loja.finalizar_compra()
        elif opcao == '5':
            loja.ver_historico()
        elif opcao == '6':
            loja.processar_pedido()
        elif opcao == '7':
            loja.ver_info_sistema()
        elif opcao == '8':
            try:
                pid = int(input("Digite o ID do produto para adicionar aos favoritos: "))
                loja.adicionar_favorito(pid)
            except ValueError:
                print("ID inválido!")
        elif opcao == '9':
            try:
                pid = int(input("Digite o ID do produto para remover dos favoritos: "))
                loja.remover_favorito(pid)
            except ValueError:
                print("ID inválido!")
        elif opcao == '10':
            loja.listar_favoritos()
        elif opcao == '0':
            print("Obrigado por usar nossa loja!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()