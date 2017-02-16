package guo.orange.com.exercise.design.proxy.dynamicproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

import guo.orange.com.exercise.design.proxy.staticproxy.HaHaProxyImp;
import guo.orange.com.exercise.design.proxy.staticproxy.ProxyInterface;

/**
 * Created by apple on 2017/2/16.
 * 动态代理类
 * 1.实现ProxyHandler
 */

public class DynamicProxyTest {
   static class MyProxyHandler implements InvocationHandler {
        Object mProxy;
        public MyProxyHandler(Object proxy){
            this.mProxy=proxy;
        }

        @Override
        public Object invoke(Object o, Method method, Object[] args) throws Throwable {
            return method.invoke(mProxy,args);
        }
    }

    public static void main(String[] args) {
        HaHaProxyImp mRealObject=new HaHaProxyImp();
        ProxyInterface mDynamicProxyImp= (ProxyInterface) Proxy.newProxyInstance(ProxyInterface.class.getClassLoader(),
                new Class[]{ProxyInterface.class},new MyProxyHandler(mRealObject));
        mDynamicProxyImp.proxyName();
    }
}
