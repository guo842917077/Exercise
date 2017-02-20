package guo.orange.com.exercise.design.factory.simplefactory;

import guo.orange.com.exercise.design.factory.Product;
import guo.orange.com.exercise.design.factory.ProductA;

/**
 * Created by apple on 2017/2/20.
 */

public class ReflectFactory{
    public static  <T extends Product>  T  createProduct(Class<T> clazz){
        Product object=null;
        try {
           object= (Product) Class.forName(clazz.getName()).newInstance();
        } catch (InstantiationException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        return (T) object;
    }

    public static void main(String[] args) {
        Product p=createProduct(ProductA.class);
        p.whichProduct();
    }
}
