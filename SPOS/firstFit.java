class firstfit {
    
    // Method to allocate memory to blocks as per First Fit algorithm
    static void first(int blockSize[], int m, int processSize[], int n) {
        // Stores block id of the block allocated to a process
        int allocation[] = new int[n];
        
        // Initially no block is assigned to any process
        for (int i = 0; i < allocation.length; i++)
            allocation[i] = -1;
        
        // Pick each process and find suitable blocks according to its size
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (blockSize[j] >= processSize[i]) {
                    // Allocate block j to process i
                    allocation[i] = j;
                    
                    // Reduce available memory in this block
                    blockSize[j] -= processSize[i];
                    break;
                }
            }
        }
        
        // Display allocation results
        System.out.println("\nProcess No.\tProcess Size\tBlock no.");
        for (int i = 0; i < n; i++) {
            System.out.print(" " + (i+1) + "\t\t" + processSize[i] + "\t\t");
            if (allocation[i] != -1)
                System.out.print(allocation[i] + 1);
            else
                System.out.print("Not Allocated");
            System.out.println();
        }
    }

    // Driver Code
    public static void main(String[] args) {
        int blockSize[] = {100, 500, 200, 300, 600};
        int processSize[] = {212, 417, 112, 426};
        int m = blockSize.length;
        int n = processSize.length;
        
        first(blockSize, m, processSize, n);
    }
}
