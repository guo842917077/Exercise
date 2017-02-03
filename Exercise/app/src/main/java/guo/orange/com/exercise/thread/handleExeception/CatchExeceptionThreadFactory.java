package guo.orange.com.exercise.thread.handleExeception;

import java.util.concurrent.ThreadFactory;

/**
 * 使用线程池的方式定义启动线程，并且为每一个线程添加捕获异常的方法，
 * 需要给线程池提供一个线程工厂。
 */

public class CatchExeceptionThreadFactory implements ThreadFactory{
    @Override
    public Thread newThread(Runnable runnable) {
        //对传入进来的线程进行改造
        Thread  thread=new Thread(runnable);
        thread.setUncaughtExceptionHandler(new UncatchExeceptionHandler());
        return null;
    }
}
