package guo.orange.com.exercise.design.observer;

/**
 * 被观察者
 */

public class Subscribe {
    public Observer mObserver;

    public String getThief() {
        return thief;
    }

    private String thief = "没有发现";

    //被观察者持有观察者
    public void register(Observer observer) {
        this.mObserver = observer;
    }

    //通知观察者,实际调用观察者的特定方法。
    public void notifyObserver() {
        mObserver.recieveNotiy();
    }

    /**
     * 做某些操作的时候调用了观察者的方法。达到通知的目的。
     */
    public void doSomething() {
        System.out.println(thief);
        this.thief = "被发现了";
        notifyObserver();
    }


}
