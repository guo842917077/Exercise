package guo.orange.com.exercise.design.proxy.staticproxy;

/**
 * Created by guo on 2017/2/16.
 * 实现代理接口
 */

public class HaHaProxyImp implements ProxyInterface{
    @Override
    public void proxyName() {
        System.out.println(HaHaProxyImp.class.getSimpleName()+" 的方法被调用");
    }
}
