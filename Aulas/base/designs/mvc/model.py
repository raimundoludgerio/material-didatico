class Livro:
    def __init__(self, title, author):
        self.titulo = title
        self.autor = author
class BibliotecaModel:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)

    def recuperar_livros(self):
        return self.livros

    def procurar_livro_pelo_titulo(self, titulo_procura):
        return [livro for livro in self.livros if titulo_procura.lower() in livro.titulo.lower()]