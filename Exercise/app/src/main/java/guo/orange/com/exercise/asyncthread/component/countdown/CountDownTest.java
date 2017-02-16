package guo.orange.com.exercise.asyncthread.component.countdown;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * 使用类库中的构建来实现阻塞。
 */

public class CountDownTest {



    public static void main(String[] args) throws Exception{
        CountDownLatch countDownLatch=new CountDownLatch(2);
        ExecutorService mExecutor=Executors.newCachedThreadPool();
        //countDownLatch.await();  不可以写在这里会阻塞后续代码的执行
        mExecutor.execute(new Work1(countDownLatch));
        mExecutor.execute(new Work2(countDownLatch));
        countDownLatch.await();
        mExecutor.shutdownNow();
        System.out.println("work1 和  work2 已经执行完毕");
    }
}
