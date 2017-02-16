package guo.orange.com.exercise.asyncthread.component.countdown;

import java.util.concurrent.CountDownLatch;

/**
 * Created by apple on 2017/2/4.
 */

public class Work2 implements Runnable{
    CountDownLatch countDownLatch;
    public Work2(CountDownLatch countDownLatch){
        this.countDownLatch=countDownLatch;
    }
    @Override
    public void run() {
        dowork();
    }
    public void dowork(){
        System.out.println("work 2 执行完毕");
        countDownLatch.countDown();
    }
}
