class BibliotecaView:
    def __init__(self, viewmodel):
        self.viewmodel = viewmodel

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

    def start(self):
        while True:
            self.exibir_menu()
            escolha = self.recuperar_dados_usuario("Escolha uma opção: ")

            if escolha == "1":
                titulo = self.recuperar_dados_usuario("Digite o título do livro: ")
                autor = self.recuperar_dados_usuario("Digite o autor do livro: ")
                result = self.viewmodel.adicionar_livros(titulo, autor)
                self.exibir_mensagem(result)

            elif escolha == "2":
                livros_info = self.viewmodel.listar_livros()
                self.exibir_livros(livros_info)

            elif escolha == "3":
                titulo_busca = self.recuperar_dados_usuario("Digite o título para buscar: ")
                livros_info = self.viewmodel.search_books(titulo_busca)
                self.exibir_livros(livros_info)

            elif escolha == "4":
                self.exibir_mensagem("Saindo do sistema. Até logo!")
                break

            else:
                self.exibir_mensagem("Opção inválida. Tente novamente.")
