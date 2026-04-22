package elementares.ListaLigada;

public class No {
    int dado;
    No proximo; // Referência para o próximo nó

    public No(int dado) {
        this.dado = dado;
        this.proximo = null;
    }
}
