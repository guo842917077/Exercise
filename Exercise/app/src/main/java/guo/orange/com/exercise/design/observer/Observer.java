package guo.orange.com.exercise.design.observer;

/**
 *  观察者
 */

public class Observer {
    private Subscribe mSubscribe;
    public Observer(){

    }
    //持有被观察者
    public void subscribe(Subscribe subscribe){
        this.mSubscribe=subscribe;
        //调用被观察的注册方法，使被观察者也持有观察者
        subscribe.register(this);
    }
    //收到通知
    public void recieveNotiy(){
        System.out.println("收到通知 : "+mSubscribe.getThief());

    }
}
