package guo.orange.com.exercise.asyncthread.component.readwritelock;

import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * 测试读取
 */

public class ReaderWriterTest {
    static ExecutorService mServices = Executors.newCachedThreadPool();
    private final static int size = 20;
    private final static Random mRandom = new Random(47);
    private static ReaderWriterList<Integer> mlockList = new ReaderWriterList<>(size, 1);

    private static class Write implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < 10; i++) {
                mlockList.set(i, mRandom.nextInt());
                try {
                    TimeUnit.MILLISECONDS.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

        }
    }
    private static class Reader implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < 10; i++) {
                mlockList.get(i);
                try {
                    TimeUnit.MILLISECONDS.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

        }
    }
    public static void main(String[] args) {

    }
}
