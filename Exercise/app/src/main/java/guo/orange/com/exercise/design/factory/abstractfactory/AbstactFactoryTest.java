package guo.orange.com.exercise.design.factory.abstractfactory;

/**
 * 抽象工厂
 * 适合当有不同的产品需要提供给工厂时，工厂尽量根据产品的特征，自身需求等条件
 * 进行分类，将类型相同的放在一起。
 */

public class AbstactFactoryTest {
    public static class AndroidButton implements Button {
        @Override
        public void createButton() {
            System.out.println("android button");
        }
    }

    public static class IOSButton implements Button {
        @Override
        public void createButton() {
            System.out.println("ios button");
        }
    }

    public static class AndroidTextView implements TextView {

        @Override
        public void createTextView() {
            System.out.println("android textview");
        }
    }

    public static class IOSTextView implements TextView {

        @Override
        public void createTextView() {
            System.out.println("iOS textview");
        }
    }
    /**
     * 抽象工厂 分类条件：同是android的控件
     */
    public interface AbstartFactory {
        Button createButton();

        TextView createTextView();
    }


    public class abstractAndroidFactory implements AbstartFactory{

        @Override
        public Button createButton() {
            return new AndroidButton();
        }

        @Override
        public TextView createTextView() {
            return new AndroidTextView();
        }
    }


    public class abstractIOSFactory implements AbstartFactory{

        @Override
        public Button createButton() {
            return new IOSButton();
        }

        @Override
        public TextView createTextView() {
            return new IOSTextView();
        }
    }
}
