package guo.orange.com.exercise.asyncthread.component.exchange;

import java.util.concurrent.Exchanger;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * ExChange Test
 * Exchager 负责在成对的线程中交换数据
 */

public class ExChangeText {
    private static boolean isDone=true;
    static class Runnable1 implements Runnable{
        Exchanger<Integer> mExchange;
        int data;
        public Runnable1(Exchanger<Integer> exchanger,int data){
            this.mExchange=exchanger;
            this.data=data;
        }
        @Override
        public void run() {
            for (int i=1;i<=3;i++){

                try {
                    TimeUnit.SECONDS.sleep(1);
                    data=i;
                    System.out.println("生产者交换前的数据 "+data);
                    data=mExchange.exchange(data);
                    System.out.println("生产者交换后的数据 "+data);
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
        }
    }
    static class Runnable2 implements Runnable{
        Exchanger<Integer> mExchange;
        int data=0;
        public Runnable2(Exchanger<Integer> exchanger,int data){
            this.mExchange=exchanger;
            this.data=data;
        }
        @Override
        public void run() {
            while (isDone){
                data=0;
                System.out.println("消费者交换前的数据 "+data);
            try {
                TimeUnit.SECONDS.sleep(1);
                data=mExchange.exchange(data);
            }catch (Exception e){
                e.printStackTrace();
            }
                System.out.println("消费者交换后的数据 "+data);
            }
        }
    }
    public static void main(String[] args){
        Exchanger<Integer> exchanger=new Exchanger<Integer>();
        ExecutorService mService= Executors.newFixedThreadPool(2);

        mService.execute(new Runnable1(exchanger,0));
        mService.execute(new Runnable2(exchanger,0));
    }
}
