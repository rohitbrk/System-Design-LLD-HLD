// Polymorphism refers to many forms, or it is a process that performs a single action in different ways. 
// It is of two different types - runtime polymorphism (method overriding) and compile-time polymorphism (method overloading)

// method overloading
public class Polymorphism {
    public static void main(String[] args) {

        int p = add(1, 1);
        int q = add(1, 1, 1);

        System.out.println(p);
        System.out.println(q);
    }

    public static int add(int a, int b) {
        return a + b;
    }

    public static int add(int a, int b, int c) {
        return a + b + c;
    }

}

// method overriding
class Parent {
    public int add(int a, int b) {
        return a + b;
    }
}

class Child1 extends Parent {
    public int add(int a, int b) {
        return a + b + b;
    }
}

class Child2 extends Parent {
    public int add(int a, int b) {
        return a + b + b;
    }
}

public class Polymorphism {
    public static void main(String[] args) {

        Child1 child1 = new Child1();
        int result = child1.add(1, 1);
        System.out.println(result);
    }

}
