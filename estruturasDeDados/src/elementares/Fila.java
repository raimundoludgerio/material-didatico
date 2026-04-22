package elementares;

import elementares.ListaDuplamenteLigada.NoDuplo;
import elementares.ListaLigada.No;

public class Fila {
    NoDuplo frente, tras; // Ponteiros para o início e fim da fila

    public void enqueue(int dado) { // Entrar na fila
        NoDuplo novoNo = new NoDuplo(dado);
        if (tras == null) {
            frente = tras = novoNo;
            return;
        }
        tras.proximo = novoNo;
        tras = novoNo;
    }

    public int dequeue() { // Sair da fila
        if (frente == null) {
            System.out.println("Fila vazia");
            return -1;
        }
        int dado = frente.dado;
        frente = frente.proximo;
        if (frente == null) tras = null;
        return dado;
    }
}
