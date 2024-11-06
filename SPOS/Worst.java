public class Worst {

    static void worstfit(int blockSize[] , int m, int processSize[], int n){
        int allocation [] = new int[n];

        for (int i = 0 ; i< allocation.length; i++){
            allocation [i] = -1;
        }

        for (int i =0; i< n ; i++){
            int wrtIdx = -1;

            for (int j =0; j< m ;j ++){

                if (blockSize[j] >= processSize[i]){
                    if (wrtIdx == -1){
                        wrtIdx =j;
                    }
                    else if(blockSize[wrtIdx] < blockSize[j]){
                        wrtIdx = j;
                    }
                }
            }

            if (wrtIdx != -1){

                allocation[i] = wrtIdx;

                blockSize[wrtIdx] -= processSize[i];
            }
        }

        System.out.println("\nProcess No\tProcess Size \t\tBlock No");
        for(int i =0; i< n; i++){
            System.out.print(" " + (i+1)+"\t\t"+processSize[i]+"\t\t");
            if (allocation[i] != -1){
                System.out.print(allocation[i]+1);
            }
            else {
                System.out.print("Not allocated");
            }
            System.out.println();
        }

    }

    public static void main(String[] args) {
        int blockSize[] = {100, 500, 200, 300, 600};  // Array representing block sizes
        int processSize[] = {212, 417, 112, 426};     // Array representing process sizes
        int m = blockSize.length;  // Number of blocks
        int n = processSize.length; // Number of processes

        // Call the worstFit method to allocate memory to processes
        worstfit(blockSize, m, processSize, n);
    }
    
}
