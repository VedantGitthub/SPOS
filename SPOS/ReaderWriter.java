import java.util.concurrent.Semaphore;

public class ReaderWriter {
    static Semaphore readLock = new Semaphore(1);
    static Semaphore writeLock = new Semaphore(1);
    static int readCount = 0;

    // Class representing a reader thread
    static class Read implements Runnable {
        @Override
        public void run() {
            try {
                // Acquire Section
                readLock.acquire();       // Lock for readCount update
                readCount++;              // Increase count of active readers
                if (readCount == 1) {     // First reader acquires writeLock to block writers
                    writeLock.acquire();
                }
                readLock.release();       // Release readLock so other readers can access

                // Reading section
                System.out.println("Thread " + Thread.currentThread().getName() + " is READING");
                Thread.sleep(1500);       // Simulate reading process
                System.out.println("Thread " + Thread.currentThread().getName() + " has FINISHED READING");

                // Releasing section
                readLock.acquire();       // Lock again to update readCount
                readCount--;              // Decrement active reader count
                if (readCount == 0) {     // Last reader releases writeLock to allow writers
                    writeLock.release();
                }
                readLock.release();       // Release readLock
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    // Class representing a writer thread
    static class Write implements Runnable {
        @Override
        public void run() {
            try {
                writeLock.acquire();      // Acquire writeLock to ensure exclusive access
                System.out.println("Thread " + Thread.currentThread().getName() + " is WRITING");
                Thread.sleep(2500);       // Simulate writing process
                System.out.println("Thread " + Thread.currentThread().getName() + " has finished WRITING");
                writeLock.release();      // Release writeLock to allow other writers/readers
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    public static void main(String[] args) throws Exception {
        // Instantiate Read and Write objects
        Read read = new Read();
        Write write = new Write();

        // Create threads with appropriate names
        Thread t1 = new Thread(read); t1.setName("thread1");
        Thread t2 = new Thread(read); t2.setName("thread2");
        Thread t3 = new Thread(write); t3.setName("thread3");
        Thread t4 = new Thread(read); t4.setName("thread4");

        // Start threads
        t1.start();
        t3.start();
        t2.start();
        t4.start();
    }
}
