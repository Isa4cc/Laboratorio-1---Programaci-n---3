import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el tamaño del arreglo: ");
        int size = scanner.nextInt();

        // Generar arreglo con números enteros aleatorios (rango 0 – size*10)
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(size * 10);
        }

        System.out.println("\nArreglo generado:");
        System.out.println(Arrays.toString(array));

        // Elegir un elemento aleatorio que si exista en el arreglo como objetivo
        int target = array[random.nextInt(size)];
        System.out.println("\nElemento a buscar: " + target);

        // Búsqueda Lineal (sobre el arreglo original)
        System.out.println("\n--- Búsqueda Lineal ---");
        int linearSteps = linearSearch(array, target);

        // Ordenar el arreglo para la búsqueda binaria
        int[] sortedArray = Arrays.copyOf(array, size);
        Arrays.sort(sortedArray);

        System.out.println("\nArreglo ordenado (para búsqueda binaria):");
        System.out.println(Arrays.toString(sortedArray));

        // Búsqueda Binaria (sobre el arreglo ordenado)
        System.out.println("\n--- Búsqueda Binaria ---");
        int binarySteps = binarySearch(sortedArray, target);

        // Resumen comparativo
        System.out.println("\n========== RESUMEN ==========");
        System.out.println("Tamaño del arreglo : " + size);
        System.out.println("Elemento buscado   : " + target);
        System.out.println("Pasos (Lineal)     : " + linearSteps);
        System.out.println("Pasos (Binaria)    : " + binarySteps);
        if (linearSteps<binarySteps){
            System.out.println("Búsqueda lineal es mejor.");
        } else if (linearSteps>binarySteps) {
            System.out.println("Búsqueda binaria es mejor.");
        }else {
            System.out.println("Ambas tienen los mismos pasos.");
        }
        System.out.println("==============================");
    }

    // ── Búsqueda Lineal ──────────────────────────────────────────────────────
    static int linearSearch(int[] array, int target) {
        int pasos = 0;
        for (int i = 0; i < array.length; i++) {
            pasos++;
            if (array[i] == target) {
                System.out.println("  [Lineal] Elemento " + target + " encontrado en índice " + i);
                System.out.println("  [Lineal] Pasos realizados: " + pasos);
                return pasos;
            }
        }
        System.out.println("  [Lineal] Elemento " + target + " NO encontrado.");
        System.out.println("  [Lineal] Pasos realizados: " + pasos);
        return pasos;
    }

    static int binarySearch(int[] sortedArray, int target) {
        int pasos = 0;
        int inicio = 0;
        int fin = sortedArray.length - 1;

        while (inicio <= fin) {
            pasos++;
            int mid = inicio + (fin - inicio) / 2;

            if (sortedArray[mid] == target) {
                System.out.println("  [Binaria] Elemento " + target + " encontrado en índice " + mid);
                System.out.println("  [Binaria] Pasos realizados: " + pasos);
                return pasos;
            } else if (sortedArray[mid] < target) {
                inicio = mid + 1;
            } else {
                fin = mid - 1;
            }
        }
        System.out.println("  [Binaria] Elemento " + target + " NO encontrado.");
        System.out.println("  [Binaria] Pasos realizados: " + pasos);
        return pasos;
    }

}
