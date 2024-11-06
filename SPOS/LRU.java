import java.io.*;
import java.util.*;

public class LRU {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter the number of frames: ");
        int frames = Integer.parseInt(br.readLine());

        System.out.print("Enter the length of the reference string: ");
        int ref_len = Integer.parseInt(br.readLine());

        int[] reference = new int[ref_len];
        int[] buffer = new int[frames];
        ArrayList<Integer> stack = new ArrayList<>();
        int pointer = 0, hit = 0, fault = 0;
        boolean isFull = false;

        // Initialize buffer to -1, representing empty frames
        Arrays.fill(buffer, -1);

        System.out.println("Enter the reference string: ");
        for (int i = 0; i < ref_len; i++) {
            reference[i] = Integer.parseInt(br.readLine());
        }

        // Process each page in the reference string
        for (int i = 0; i < ref_len; i++) {
            int page = reference[i];

            // If page is already in stack, move it to the end to mark as recently used
            if (stack.contains(page)) {
                stack.remove((Integer) page);
            }
            stack.add(page);

            boolean isHit = false;
            for (int j = 0; j < frames; j++) {
                if (buffer[j] == page) {
                    hit++;
                    isHit = true;
                    break;
                }
            }

            // Handle page fault
            if (!isHit) {
                if (isFull) {
                    int lruPage = stack.get(0); // Least Recently Used page is at the front of the stack
                    for (int j = 0; j < frames; j++) {
                        if (buffer[j] == lruPage) {
                            pointer = j;
                            break;
                        }
                    }
                }

                buffer[pointer] = page;
                fault++;
                pointer = (pointer + 1) % frames;
                isFull = pointer == 0; // Mark as full when pointer wraps around
            }

            // Display current buffer state
            System.out.print("Buffer state: ");
            for (int j = 0; j < frames; j++) {
                System.out.print((buffer[j] == -1 ? "-" : buffer[j]) + " ");
            }
            System.out.println();
        }

        // Display final results
        System.out.println("Total hits: " + hit);
        System.out.println("Total faults: " + fault);
        System.out.println("Hit ratio: " + (float) hit / ref_len);
    }
}


