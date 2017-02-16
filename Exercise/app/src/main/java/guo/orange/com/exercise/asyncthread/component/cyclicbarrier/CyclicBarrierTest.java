package guo.orange.com.exercise.asyncthread.component.cyclicbarrier;

import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * 循环栅栏的练习，当多个线程互相等待时，直到达到指定的屏障点，后续任务才进行时，可以使用该方法。
 * 例如：
 */

public class CyclicBarrierTest {
    public static void main(String[] args) throws Exception{
        final CyclicBarrier mCyclicBarrier=new CyclicBarrier(3, new Runnable() {
            @Override
            public void run() {
                System.out.println("启动");
            }
        });
        ExecutorService mExecutor= Executors.newFixedThreadPool(3);
        mExecutor.execute(new Runner(mCyclicBarrier,"1"));
        mExecutor.execute(new Runner(mCyclicBarrier,"2"));
        mExecutor.execute(new Runner(mCyclicBarrier,"3"));
        mExecutor.shutdownNow();
    }
   static class Runner implements Runnable{
       private CyclicBarrier barrier;
       private String name;
       public Runner(CyclicBarrier barrier,String name) {
           this.barrier=barrier;
           this.name=name;
       }

        @Override
        public void run() {
            System.out.println(name+"号选手准备完毕");
            try {
                barrier.await();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (BrokenBarrierException e) {
                e.printStackTrace();
            }
            System.out.println(name+"号选手起跑");
        }
    }
}
