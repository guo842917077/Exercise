package guo.orange.com.exercise.component.countdown;

import java.util.concurrent.CountDownLatch;

/**
 * Created by apple on 2017/2/4.
 */

public class Work1 implements Runnable{

    CountDownLatch countDownLatch;
    public Work1(CountDownLatch countDownLatch){
        this.countDownLatch=countDownLatch;
    }
    @Override
    public void run() {
        dowork();
    }
    public void dowork(){
        System.out.println("work 1 执行完毕");
        countDownLatch.countDown();
    }
}
