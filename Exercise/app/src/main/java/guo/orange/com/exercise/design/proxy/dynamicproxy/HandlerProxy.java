package guo.orange.com.exercise.design.proxy.dynamicproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * 简单封装一个代理工具类
 */

public class HandlerProxy implements InvocationHandler{
    private Object mTarget;
    private HandlerProxy(){}
    public Object newProxyInstance(Object targetObject){
        this.mTarget=targetObject;
        return Proxy.newProxyInstance(targetObject.getClass().getClassLoader(),targetObject.getClass().getInterfaces(),this);
    }
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        return method.invoke(mTarget,args);
    }
}
