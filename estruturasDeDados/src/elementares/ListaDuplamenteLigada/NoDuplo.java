package elementares.ListaDuplamenteLigada;

public class NoDuplo {
    public int dado;
    public NoDuplo proximo;
    public NoDuplo anterior; // A grande diferença!


    public NoDuplo(int dado) {
        this.dado = dado;
        this.proximo = null;
        this.anterior = null;
    }
}
