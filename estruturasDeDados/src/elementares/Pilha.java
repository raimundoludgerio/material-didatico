package elementares;

public class Pilha {
    private int[] elementos;
    private int topo;

    public Pilha(int capacidade) {
        elementos = new int[capacidade];
        topo = -1; // Pilha vazia
    }

    public void push(int dado) { // Empilhar
        if (topo == elementos.length - 1) {
            System.out.println("Erro: Pilha cheia (Stack Overflow)");
            return;
        }
        elementos[++topo] = dado;
    }

    public int pop() { // Desempilhar
        if (topo == -1) {
            System.out.println("Erro: Pilha vazia");
            return -1;
        }
        return elementos[topo--];
    }
}
