import java.io.*;

public class FIFO {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter the number of frames: ");
        int frames = Integer.parseInt(br.readLine());
        
        System.out.print("Enter the length of the reference string: ");
        int ref_len = Integer.parseInt(br.readLine());

        int[] reference = new int[ref_len];
        int[] buffer = new int[frames];
        int pointer = 0, hit = 0, fault = 0;

        // Initialize buffer to represent empty frames
        for (int i = 0; i < frames; i++) buffer[i] = -1;

        System.out.print("Enter the reference string: ");
        for (int i = 0; i < ref_len; i++) {
            reference[i] = Integer.parseInt(br.readLine());
        }

        // Process each page in the reference string
        for (int i = 0; i < ref_len; i++) {
            boolean isHit = false;

            // Check if the page is already in the buffer (hit)
            for (int j = 0; j < frames; j++) {
                if (buffer[j] == reference[i]) {
                    isHit = true;
                    hit++;
                    break;
                }
            }

            // If no hit, replace the oldest page (FIFO)
            if (!isHit) {
                buffer[pointer] = reference[i];
                fault++;
                pointer = (pointer + 1) % frames;  // Move pointer for FIFO
            }

            // Display current state of buffer
            System.out.print("Buffer state: ");
            for (int j = 0; j < frames; j++) {
                System.out.print((buffer[j] == -1 ? "-" : buffer[j]) + " ");
            }
            System.out.println();
        }

        // Display results
        System.out.println("Total hits: " + hit);
        System.out.println("Total faults: " + fault);
        System.out.println("Hit ratio: " + (float) hit / ref_len);
    }
}
