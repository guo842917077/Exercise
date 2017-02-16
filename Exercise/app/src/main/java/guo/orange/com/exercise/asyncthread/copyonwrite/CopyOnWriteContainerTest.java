package guo.orange.com.exercise.asyncthread.copyonwrite;

import java.util.concurrent.CopyOnWriteArrayList;

/**
 * CopyOnWrite容器的练习
 * CopyOnWrite 容器是一种即时复写容器，通俗的理解是当我们将一个元素加入容器前，不直接加入，而是将当前容器复制出一个
 * 新的容器对象，然后新添加的元素加入到该容器，然后将旧容器的索引指向新容器。这样做可以通过不加锁的方式对容器进行并发
 * 的读取
 */

public class CopyOnWriteContainerTest {
    public static void main(String[] args) {
        //1.在一个线程中进行加入操作
        final CopyOnWriteArrayList<Integer>  mList=new CopyOnWriteArrayList<>();
        mList.add(1);
        new Thread(new Runnable() {
            int count=2;
            @Override
            public void run() {
                while (true){
                    mList.add(count++);
                    if (count>10)
                        break;
                }
            }
        }).start();
        try {
            Thread.currentThread().sleep(3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        for (int i:mList){
            System.out.println("i : "+i+" mlist hascode : "+mList.hashCode());
        }
    }
}
