class BibliotecaViewModel:
    def __init__(self, model):
        self.model = model

    def adicionar_livro(self, title, author):
        self.model.adicionar_livro(title, author)
        return "Livro adicionado com sucesso!"

    def listar_livros(self):
        livros = self.model.recuperar_livros()
        if not livros:
            return "Nenhum livro encontrado."
        return [(livros.titulo, livro.autor) for livro in livros]

    def procurar_livros(self, procura_titulo):
        livros = self.model.procurar_livro_pelo_titulo(procura_titulo)
        if not livros:
            return "Nenhum livro encontrado."
        return [(livros.titulo, livro.autor) for livro in livros]
