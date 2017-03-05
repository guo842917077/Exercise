package guo.orange.com.eventbustest;

/**
 * Created by apple on 2017/3/1.
 */

public class MessageEvent {
    public Object message;
    public int what;

    public Object getMessage() {
        return message;
    }

    public void setMessage(Object message) {
        this.message = message;
    }

    public int getWhat() {
        return what;
    }

    public void setWhat(int what) {
        this.what = what;
    }
}
