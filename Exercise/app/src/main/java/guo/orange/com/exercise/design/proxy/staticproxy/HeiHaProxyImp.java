package guo.orange.com.exercise.design.proxy.staticproxy;

/**
 * Created by apple on 2017/2/16.
 */

public class HeiHaProxyImp implements ProxyInterface{

    @Override
    public void proxyName() {
        System.out.println(HeiHaProxyImp.class.getSimpleName()+"：的方法被调用");
    }
}
