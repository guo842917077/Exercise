package guo.orange.com.exercise.design.factory;

import guo.orange.com.exercise.design.proxy.staticproxy.ProxyInterface;

/**
 * 产品b
 */

public class ProductB implements Product{

    @Override
    public void whichProduct() {
        System.out.println("产品B");
    }
}
