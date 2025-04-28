class BibliotecaView:
    def exibir_menu(self):
        print("\n--- Biblioteca ---")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Buscar livro por título")
        print("4. Sair")

    def recuperar_dados_usuario(self, mensagem):
        return input(mensagem)

    def exibir_livros(self, livros):
        if not livros:
            print("Nenhum livro encontrado.")
        else:
            print("\nLivros:")
            for livro in livros:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}")

    def exibir_mensagem(self, mensagem):
        print(mensagem)
