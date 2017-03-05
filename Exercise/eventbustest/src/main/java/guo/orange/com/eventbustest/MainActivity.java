package guo.orange.com.eventbustest;

import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

/**
 * Event Bus 是一个消息总线库，它简化了组件与组件，组件与后台线程通信的流程。
 * 1.注册 初始化
 * 2.订阅一个事件
 */
public class MainActivity extends AppCompatActivity {
    private EventBus mEventBus;
    private Button mButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mEventBus=EventBus.getDefault();
        mEventBus.register(this);
        mButton= (Button) this.findViewById(R.id.button);
        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this,SecondActivity.class));
            }
        });
    }

    /**
     * sticky 粘性的接收，即：即使当发布者发布消息时当前类没有订阅，在发布之后才订阅，也可以接收到消息没有eventbus订阅，
     */
    @Subscribe(threadMode = ThreadMode.MAIN,sticky = true,priority = 20)
    public void handlerMessage(MessageEvent message){
        if (message.what==1001){
            Toast.makeText(MainActivity.this,"event bus 接收到消息 ："+message.getMessage(),Toast.LENGTH_SHORT).show();
        }
    }


    @Override
    protected void onDestroy() {
        super.onDestroy();
        mEventBus.unregister(this);
    }
}
