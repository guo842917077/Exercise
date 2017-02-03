package guo.orange.com.exercise.thread.handleExeception;

/**
 * 负责捕获线程的异常
 */

public class UncatchExeceptionHandler implements Thread.UncaughtExceptionHandler{
    @Override
    public void uncaughtException(Thread thread, Throwable throwable) {
        System.out.print(thread.currentThread()+" ： "+throwable);
    }
}
