package guo.orange.com.exercise;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import guo.orange.com.exercise.asyncthread.thread.handleExeception.CatchExeceptionThreadFactory;

public class MainActivity extends AppCompatActivity {
    /**
     * 线程
     */
    ExecutorService mExecutor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.btnCanvas).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, CanvasTestActivity.class));
            }
        });

    }

    private void test() {
        testUncatchExeception();
    }

    /**
     * 捕获异常的线程练习
     */
    private void testUncatchExeception() {
        mExecutor = Executors.newCachedThreadPool(new CatchExeceptionThreadFactory());
        mExecutor.execute(new Thread());
    }

}
