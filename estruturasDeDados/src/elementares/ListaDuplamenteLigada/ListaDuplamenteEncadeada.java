package elementares.ListaDuplamenteLigada;

import elementares.ListaLigada.ListaEncadeada;
import elementares.ListaLigada.No;

public class ListaDuplamenteEncadeada {
    NoDuplo cabeca;

    public void adicionar(int dado) {
        NoDuplo novoNo = new NoDuplo(dado);
        if (cabeca == null) {
            cabeca = novoNo;
            return;
        }
        NoDuplo atual = cabeca;
        while (atual.proximo != null) {
            atual = atual.proximo;
        }
        atual.proximo = novoNo;
        novoNo.anterior = atual; // Configura a volta
    }

    public void imprimir() {
        NoDuplo atual = cabeca;
        while (atual != null) {
            System.out.print(atual.dado + " <-> ");
            atual = atual.proximo;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        ListaDuplamenteEncadeada lista = new ListaDuplamenteEncadeada();
        lista.adicionar(5);
        lista.adicionar(15);
        lista.adicionar(25);
        lista.imprimir(); // Saída: 5 <-> 15 <-> 25 <-> null
    }
}
