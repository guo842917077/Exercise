package guo.orange.com.exercise.component.semphoretest;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.ThreadFactory;

/**
 * Semaphore是一个计数信号量，它的内部维护了一个信号量集合，
 * 每当有任务需要执行时，需要查询集合中是否有“信号”，拿到信号才可以执行后续的任务。否则要等待前边的任务释放信号。
 * 例如：食堂吃放时，只有3个窗口，却有5个人才排队，那么有2个人必须等待前面3个人有人打完饭后才能打饭。
 */

public class SemphoreTest {
    public static void main(String[] args){
        final Semaphore semaphore=new Semaphore(3);
        final ExecutorService service= Executors.newFixedThreadPool(3);
        for (int i=0;i<5;i++){
            service.submit(new Runnable() {
                @Override
                public void run() {
                    try {
                        //发起请求
                        semaphore.acquire();
                        System.out.println("当前有"+(semaphore.availablePermits()+1)+"个窗口可以打饭");
                        Thread.sleep(2000);//打饭花去2秒钟
                        semaphore.release();//打完饭
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                }
            });
        }
    }
}
