package elementares;

public class Vetores {
    public static void main(String[] args) {
        // Declaração e inicialização de um array com tamanho fixo (5)
        int[] numeros = new int[5];

        // Inserção O(1)
        numeros[0] = 10;
        numeros[1] = 20;
        numeros[2] = 30;
        numeros[3] = 40;
        numeros[4] = 50;

        // Acesso O(1)
        System.out.println("Elemento no índice 2: " + numeros[2]); // Saída: 30

        // Percorrendo o array O(n)
        System.out.print("Elementos do Array: ");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print(numeros[i] + " ");
        }
    }
}
