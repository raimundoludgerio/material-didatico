class BibliotecaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.exibir_menu()
            escolha = self.view.recuperar_dados_usuario("Escolha uma opção: ")
            if escolha == "1":
                title = self.view.recuperar_dados_usuario("Digite o título do livro: ")
                author = self.view.recuperar_dados_usuario("Digite o autor do livro: ")
                self.model.adicionar_livro(title, author)
                self.view.exibir_mensagem("Livro adicionado com sucesso!")
            elif escolha == "2":
                books = self.model.recuperar_livros()
                self.view.exibir_livros(books)
            elif escolha == "3":
                search_title = self.view.recuperar_dados_usuario("Digite o título para buscar: ")
                books = self.model.procurar_livro_pelo_titulo(search_title)
                self.view.exibir_livros(books)
            elif escolha == "4":
                self.view.exibir_mensagem("Saindo do sistema. Até logo!")
                break
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.")
