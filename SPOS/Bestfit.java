public class Bestfit {

    static void Best (int blocksize[] , int m , int processSize[] , int n){

        int allocation [] = new int [n];

        for (int i=0 ; i< allocation.length; i++)
            allocation[i] = -1;

        for (int i = 0; i< n ; i++){
            int bestIdx = -1;

            for (int j= 0; j<m ; j++){

                if (blocksize[j] >= processSize[i]){
                    if(bestIdx == -1){
                        bestIdx = j;
                    }
                    else if(blocksize[bestIdx] > blocksize[j]){
                        bestIdx = j;
                    }
                }
            }

            if (bestIdx != -1){
                allocation[i] = bestIdx;

                blocksize[bestIdx] -= processSize[i];
            }
        }

       System.out.println("\nProcess No\tProcess Size\t\tBlock No");
       for (int i = 0; i<n ; i++){
        System.out.print(" "+ (i+1) +"\t\t" + processSize[i]+"\t\t");
        if(allocation[i] != -1){
            System.out.print(allocation[i] + 1);
        }
        else {
            System.out.print("-");
        }
        System.out.println();
    } 
    }
    public static void main(String[] args) {
        // Size of blocks and processes
        int blockSize[] = {100, 500, 200, 300, 600};  // Array representing block sizes
        int processSize[] = {212, 417, 112, 426};     // Array representing process sizes
        int m = blockSize.length;  // Number of blocks
        int n = processSize.length; // Number of processes

        // Call the bestFit method to allocate memory to processes
        Best(blockSize, m, processSize, n);
}
}
