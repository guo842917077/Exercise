package guo.orange.com.exercise.blockqueue;

import android.util.Log;

import java.util.Random;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

/**
 * 阻塞队列的实践，阻塞队列可以解决同步的问题。
 */

public class BlockingQueueTest {
    /**
     * 制作吐司
     */
 static class Toast{
        String status="普通";
        private final int id;
        public Toast(int nid) {
            id=nid;
        }
        public void butter(){
            status="涂油";
        }
        public void jam(){
            status="果酱";
        }
        public int getId(){
            return id;
        }
        @Override
        public String toString() {
            return "吐司 ："+id+" "+status;
        }
    }

    /**
     * 负责生产吐司
     */
 static   class Toaster implements Runnable{
        private  LinkedBlockingQueue<Toast> toastQueue;
         int count=0;
        Random random=new Random(47);
         public Toaster(LinkedBlockingQueue<Toast> toastQueue) {
             this.toastQueue=toastQueue;
         }

         @Override
         public void run() {
             while (!Thread.interrupted()) {
                 try {
                     TimeUnit.MILLISECONDS.sleep(100+random.nextInt(500));
                     //制作toast
                     Toast t = new Toast(count++);
                     toastQueue.put(t);
                 } catch (InterruptedException e) {
                     e.printStackTrace();
                 }
             }
            System.out.println("吐司出炉");
         }
     }
  static  class Butter implements Runnable{
        LinkedBlockingQueue<Toast> dryQueue,butterQueue;
        public Butter(LinkedBlockingQueue<Toast> dryQueue,LinkedBlockingQueue<Toast> butterQueue){
            this.butterQueue=butterQueue;
            this.dryQueue = dryQueue;
        }
        @Override
        public void run() {
            while (!Thread.interrupted()) {
                try {
                    //将制作好的吐司涂油
                    Toast t = dryQueue.take();
                    t.butter();
                    butterQueue.put(t);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("吐司上油完毕");
        }
    }

    /**
     * 果酱线程，负责给吐司添加果酱
     */
  static  class Jammer implements Runnable{
        LinkedBlockingQueue<Toast> finishQueue,butterQueue;
        public Jammer(LinkedBlockingQueue<Toast> butterQueue,LinkedBlockingQueue<Toast> finishQueue){
            this.butterQueue=butterQueue;
            this.finishQueue = finishQueue;
        }
        @Override
        public void run() {
            while (!Thread.interrupted()) {
                try {
                    //最后将涂好黄油的吐司，添加果酱
                    Toast t = butterQueue.take();
                    t.jam();
                    finishQueue.put(t);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("吐司加入果酱完毕");
        }
    }

    /**
     * 消费者 负责消费finishQueue中的吐司
     */
  static  class Costomer implements Runnable{
        LinkedBlockingQueue<Toast> finishQueue;
        int count=0;
        public Costomer( LinkedBlockingQueue<Toast> finishQueue){
            this.finishQueue=finishQueue;
        }
        @Override
        public void run() {
            while (!Thread.interrupted()){
                try {
                    //最后将涂好黄油的吐司，添加果酱
                    Toast t = finishQueue.take();
                    if (t.getId()!=count++||!t.status.equals("果酱")){
                        System.exit(1);
//                        Log.d("tag","你的制作流程出错啦"+t.getId()+t.status+count);
                        System.out.print("取出吐司出现问题");
                    }else{
                        System.out.println("吐司吃掉了");
                    }
//                    Log.d("tag","吐司制作完毕");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
  public static void main(String[] args) throws Exception{
      LinkedBlockingQueue<Toast> toastQueue=new LinkedBlockingQueue<>(),
              butterQueue=new LinkedBlockingQueue<>(),
              finishQueue=new LinkedBlockingQueue<>();
      ExecutorService mExecutor= Executors.newCachedThreadPool();
      mExecutor.execute(new Toaster(toastQueue));
      mExecutor.execute(new Butter(toastQueue,butterQueue));
      mExecutor.execute(new Jammer(butterQueue,finishQueue));
      mExecutor.execute(new Costomer(finishQueue));
      TimeUnit.SECONDS.sleep(2);
      mExecutor.shutdownNow();
  }
}
