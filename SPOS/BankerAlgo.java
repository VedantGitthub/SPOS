import java.util.Scanner;

public class BankerAlgo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of processes: ");
        int processCount = scanner.nextInt();
        System.out.print("Enter the number of resources: ");
        int resourceCount = scanner.nextInt();

        int max[][] = new int[processCount][resourceCount];
        int allocation[][] = new int[processCount][resourceCount];
        int need[][] = new int[processCount][resourceCount];
        int available[] = new int[resourceCount];

        System.out.println("Enter the maximum resource matrix:");
        for (int i = 0; i < processCount; i++) {
            System.out.print("Process " + i + ": ");
            for (int j = 0; j < resourceCount; j++) {
                max[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Enter the allocation matrix:");
        for (int i = 0; i < processCount; i++) {
            System.out.print("Process " + i + ": ");
            for (int j = 0; j < resourceCount; j++) {
                allocation[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Enter the available resources:");
        for (int j = 0; j < resourceCount; j++) {
            available[j] = scanner.nextInt();
        }

        for (int i = 0; i < processCount; i++) {
            for (int j = 0; j < resourceCount; j++) {
                need[i][j] = max[i][j] - allocation[i][j];
            }
        }

        System.out.println("Need Matrix:");
        for (int i = 0; i < processCount; i++) {
            for (int j = 0; j < resourceCount; j++) {
                System.out.print(need[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("Available Resources:");
        for (int j = 0; j < resourceCount; j++) {
            System.out.print(available[j] + " ");
        }
        System.out.println();

        boolean[] finish = new boolean[processCount];
        int[] work = available.clone();
        int[] safeSequence = new int[processCount];
        int count = 0;

        while (count < processCount) {
            boolean progressMade = false;
            for (int i = 0; i < processCount; i++) {
                if (!finish[i]) {
                    int j;
                    for (j = 0; j < resourceCount; j++) {
                        if (need[i][j] > work[j]) {
                            break;
                        }
                    }
                    if (j == resourceCount) {
                        for (int k = 0; k < resourceCount; k++) {
                            work[k] += allocation[i][k];
                        }
                        finish[i] = true;
                        safeSequence[count++] = i;
                        progressMade = true;
                    }
                }
            }
            if (!progressMade) {
                System.out.println("System is in an unsafe state.");
                return;
            }
        }

        System.out.println("Safe Sequence:");
        for (int i = 0; i < processCount; i++) {
            System.out.print("P" + safeSequence[i] + " ");
        }
        System.out.println();

        System.out.println("New Available Resources:");
        for (int j = 0; j < resourceCount; j++) {
            System.out.print(work[j] + " ");
        }
        System.out.println();

        scanner.close();
    }
}
