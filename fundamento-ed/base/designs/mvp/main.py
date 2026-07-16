from model import BibliotecaModel
from view import BibliotecaView
from presenter import BibliotecaPresenter

def main():
    model = BibliotecaModel()
    view = BibliotecaView()
    presenter = BibliotecaPresenter(model, view)
    view.start()

if __name__ == "__main__":
    main()
