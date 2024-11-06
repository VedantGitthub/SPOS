import java.util.Scanner;

class FCFS {

    // Function to find the waiting time for all processes
    static void findWaitingTime(int n, int bt[], int wt[]) {
        // Waiting time for first process is 0
        wt[0] = 0;

        // Calculating waiting time for each process
        for (int i = 1; i < n; i++) {
            wt[i] = bt[i - 1] + wt[i - 1];
        }
    }

    // Function to calculate turn around time
    static void findTurnAroundTime(int n, int bt[], int wt[], int tat[]) {
        // Calculating turnaround time by adding bt[i] + wt[i]
        for (int i = 0; i < n; i++) {
            tat[i] = bt[i] + wt[i];
        }
    }

    // Function to calculate average waiting and turnaround times
    static void findavgTime(int n, int bt[]) {
        int wt[] = new int[n], tat[] = new int[n];
        int total_wt = 0, total_tat = 0;

        // Finding waiting time of all processes
        findWaitingTime(n, bt, wt);

        // Finding turnaround time for all processes
        findTurnAroundTime(n, bt, wt, tat);

        // Display processes along with all details
        System.out.printf("Process Burst Time Waiting Time Turnaround Time\n");

        // Calculate total waiting time and total turnaround time
        for (int i = 0; i < n; i++) {
            total_wt += wt[i];
            total_tat += tat[i];
            System.out.printf(" %d       %d           %d              %d\n", (i + 1), bt[i], wt[i], tat[i]);
        }

        float avg_wt = (float) total_wt / n;
        float avg_tat = (float) total_tat / n;
        System.out.printf("Average waiting time = %.2f\n", avg_wt);
        System.out.printf("Average turnaround time = %.2f\n", avg_tat);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input number of processes
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        // Input burst times
        int burst_time[] = new int[n];
        System.out.println("Enter burst times for each process:");
        for (int i = 0; i < n; i++) {
            System.out.printf("Process %d: ", (i + 1));
            burst_time[i] = sc.nextInt();
        }

        // Calculate average time
        findavgTime(n, burst_time);

        sc.close();
    }
}
