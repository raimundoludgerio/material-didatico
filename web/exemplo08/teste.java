public static int somatorio2(int n) {
    int soma = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            soma += i;
        }
    }
    return soma;
}