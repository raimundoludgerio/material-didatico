class BibliotecaPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_presenter(self)

    def enviar_escolha_usuario(self, escolha):
        if escolha == "1":
            titulo = self.view.recuperar_dados_usuario("Digite o título do livro: ")
            autor = self.view.recuperar_dados_usuario("Digite o autor do livro: ")
            self.model.adicionar_livro(titulo, autor)
            self.view.exibir_mensagem("Livro adicionado com sucesso!")

        elif escolha == "2":
            books = self.model.recuperar_livros()
            self.view.exibir_livros(books)

        elif escolha == "3":
            titulo_procura = self.view.recuperar_dados_usuario("Digite o título para buscar: ")
            books = self.model.procurar_livro_pelo_titulo(titulo_procura)
            self.view.exibir_livros(books)

        elif escolha == "4":
            self.view.exibir_mensagem("Saindo do sistema. Até logo!")
            exit()

        else:
            self.view.exibir_mensagem("Opção inválida. Tente novamente.")
