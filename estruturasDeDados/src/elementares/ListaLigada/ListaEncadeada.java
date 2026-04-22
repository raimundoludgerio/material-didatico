package elementares.ListaLigada;

public class ListaEncadeada {
    No cabeca; // Primeiro elemento da lista

    // Método para adicionar no final da lista
    public void adicionar(int dado) {
        No novoNo = new No(dado);
        if (cabeca == null) {
            cabeca = novoNo;
            return;
        }
        No atual = cabeca;
        while (atual.proximo != null) {
            atual = atual.proximo;
        }
        atual.proximo = novoNo; // Último nó aponta para o novo
    }

    public void imprimirLista() {
        No atual = cabeca;
        while (atual != null) {
            System.out.print(atual.dado + " -> ");
            atual = atual.proximo;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        ListaEncadeada lista = new ListaEncadeada();
        lista.adicionar(5);
        lista.adicionar(15);
        lista.adicionar(25);
        lista.imprimirLista(); // Saída: 5 -> 15 -> 25 -> null
    }
}
