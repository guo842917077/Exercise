package guo.orange.com.exercise;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import guo.orange.com.exercise.thread.handleExeception.CatchExeceptionThreadFactory;

public class MainActivity extends AppCompatActivity {
    /**
     * 线程
     */
    ExecutorService mExecutor;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }
    /**
     * 捕获异常的线程练习
     */
    private void testUncatchExeception(){
        mExecutor= Executors.newCachedThreadPool(new CatchExeceptionThreadFactory());
        mExecutor.execute(new Thread());
    }

}
