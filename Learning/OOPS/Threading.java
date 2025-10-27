class MyThread extends Thread {
    private String message;
    private int interval;

    public MyThread(String message, int interval) {
        this.message = message;
        this.interval = interval;
    }

    public void run() {
        try {
            while (true) {
                System.out.println(message);
                Thread.sleep(interval); // Pauses the thread for 'interval' milliseconds
            }
        } catch (InterruptedException e) {
            System.out.println(message + " thread interrupted");
        }
    }
}

public class Threading {
    public static void main(String[] args) {
        MyThread t1 = new MyThread("Good Morning", 1000);  // 1 second
        MyThread t2 = new MyThread("Hello", 2000);         // 2 seconds
        MyThread t3 = new MyThread("Welcome", 3000);       // 3 seconds

        t1.start();
        t2.start();
        t3.start();
    }
}
