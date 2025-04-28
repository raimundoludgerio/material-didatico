from model import BibliotecaModel
from view import BibliotecaView
from controller import BibliotecaController

def main():
    model = BibliotecaModel()
    view = BibliotecaView()
    controller = BibliotecaController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
