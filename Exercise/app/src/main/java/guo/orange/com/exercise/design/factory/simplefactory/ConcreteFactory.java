package guo.orange.com.exercise.design.factory.simplefactory;

import guo.orange.com.exercise.design.factory.Factory;
import guo.orange.com.exercise.design.factory.Product;
import guo.orange.com.exercise.design.factory.ProductA;

/**
 * 简单工厂
 */

public class ConcreteFactory implements Factory {
    @Override
    public Product createProduct() {
        return new ProductA();
    }
}
