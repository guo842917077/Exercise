package guo.orange.com.exercise.design.proxy.staticproxy;

/**
 * 静态代理的实现类
 * 1.设计方法接口
 * 2.有具体的实现类实现接口：例如HaHaProxyImp
 * 3.静态代理类实现接口
 * 4.静态代理类内部持有具体的实现类对象
 * 5.静态代理内部的方法实现由具体实现类完成
 */

public class StaticProxyManager implements ProxyInterface{
    ProxyInterface mProxyImp;
    public StaticProxyManager(ProxyInterface proxyImp){
        //持有具体的实现类
        this.mProxyImp=proxyImp;
    }
    @Override
    public void proxyName() {
        //由具体实现类完成
        this.mProxyImp.proxyName();
    }

    public static void main(String[] args) {
        StaticProxyManager manager=new StaticProxyManager(new HaHaProxyImp());
        manager.proxyName();
        System.out.println("------------分割线--------------");
        StaticProxyManager manager2=new StaticProxyManager(new HeiHaProxyImp());
        manager2.proxyName();
    }
}
