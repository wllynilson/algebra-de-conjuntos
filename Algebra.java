/**
 * Matemática Discreta
 * Algebra de Conjuntos
 */
class Algebra {

    public static void main(String[] args) {
        //System.out.println("testando!!");
        int[] A = new int[]{2, 3, 5, 7, 11};
        int[] B = new int[]{13, 17};

        adicionarElemento(A, 9);
        System.out.println(A[0]);
    }

    public static int[] adicionarElemento(int[] conjunto, int elemento) {
        if (conjunto.length == 0) {
            conjunto = new int[1];
            conjunto[0] = elemento;
            return conjunto;
        } else {
            int[] a = new int[conjunto.length + 1];
            for (int i = 0; i < a.length; i++) {
                if (i < conjunto.length)
                    a[i] = conjunto[i];
                else
                    a[i] = elemento;
            }
            return a;
        }
    }
}
