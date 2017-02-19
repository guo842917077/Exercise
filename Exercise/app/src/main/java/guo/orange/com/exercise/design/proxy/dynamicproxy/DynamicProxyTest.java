package guo.orange.com.exercise.design.proxy.dynamicproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

import guo.orange.com.exercise.design.proxy.staticproxy.HaHaProxyImp;
import guo.orange.com.exercise.design.proxy.staticproxy.HeiHaProxyImp;
import guo.orange.com.exercise.design.proxy.staticproxy.ProxyInterface;

/**
 * Created by guo on 2017/2/16.
 * 动态代理类
 * 1.具有接口
 * 2.实现ProxyHandler 代理方法类，调用动态代理生成的代理类的方法时，会触发代理方法类的invoke方法返回结果。
 * 3.根据构造器，接口，和代理方法类为接口创件代理类。
 */

public class DynamicProxyTest {
   static class MyProxyHandler implements InvocationHandler {
        Object mProxy;
        public MyProxyHandler(Object proxy){
            this.mProxy=proxy;
        }

        @Override
        public Object invoke(Object o, Method method, Object[] args) throws Throwable {

            /**
             * 在调用方法之前也可以做一些其他的事情
             */
            System.out.println("do something");
            //在这里将真实对象固定
//            o=new HeiHaProxyImp();
//            return method.invoke(o,args);
            //根据参数通过反射调用执行mProxy对象的方法
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
