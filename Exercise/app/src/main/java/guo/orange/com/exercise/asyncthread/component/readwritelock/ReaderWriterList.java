package guo.orange.com.exercise.asyncthread.component.readwritelock;

import java.util.Collections;
import java.util.List;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 *  ReadWrite lock 适合对不频繁向集合中写入，但是有多个线程读取集合中的数据时很好友
 */

public class ReaderWriterList<T>{
    private List<T> mLockList;
    ReentrantReadWriteLock mReentranLock=new ReentrantReadWriteLock(true);
    public ReaderWriterList(int size,T initValue){
        mLockList= Collections.nCopies(size,initValue);
    }
    public T set(int index,T value){
        Lock wLock=mReentranLock.writeLock();//获取写入锁
        wLock.lock();
        try {
            return mLockList.set(index,value);
        }finally {
            wLock.unlock();
        }
    }
    public T get(int index){
        Lock rLock=mReentranLock.readLock();//获取读取锁
        rLock.lock();
        try {
            return mLockList.get(index);
        }finally {
            rLock.unlock();
        }
    }
}
