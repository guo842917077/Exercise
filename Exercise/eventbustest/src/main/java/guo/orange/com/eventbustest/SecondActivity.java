package guo.orange.com.eventbustest;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

/**
 * 如果没有使用@subscribe标签订阅方法，不要使用Register方法，否则会报错
 */
public class SecondActivity extends AppCompatActivity {
    private EventBus mEventBus;
    private Button mButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        mEventBus=EventBus.getDefault();
        mButton= (Button) this.findViewById(R.id.button2);
        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                MessageEvent event=new MessageEvent();
                event.setMessage("second 通过event bus 发送消息");
                event.setWhat(1001);
                mEventBus.post(event);
            }
        });
    }


    @Override
    protected void onDestroy() {
        super.onDestroy();
       
    }
}
