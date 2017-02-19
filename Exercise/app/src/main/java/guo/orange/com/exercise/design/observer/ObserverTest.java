package guo.orange.com.exercise.design.observer;

/**
 * Created by guo on 2017/2/19.
 * 观察者模式
 * 使用场景
 * A类对B类的变化特别敏感，需要在b类改变的一瞬间做出反应。
 *
 * 使用方法
 * 1.被观察者持有观察者对象，这一步骤通常是通过被观察者注册（Register方法）或者订阅（Subscribe方法）观察者实现的。
 * 2.观察者同样持有被观察者对象，同时调用被观察者的订阅方法完成订阅。（被观察者拿到观察者对象这一步通常在观察者类中去做。）
 * 3.被观察者具有一个"通知观察者的"方法，该方法通过调用被观察者内部持有的观察者对象的方法来达到通知观察者的目的。
 * 其实所谓收到通知就是被观察者做某些操作时，同时调用了观察者的特定方法。
 */

public class ObserverTest {
    public static void main(String[] args) {
        Observer observer=new Observer();
        Subscribe subscribe=new Subscribe();
        //观察者开始监视被观察者
        observer.subscribe(subscribe);
        //被观察者要做操作了
        subscribe.doSomething();
    }
}
