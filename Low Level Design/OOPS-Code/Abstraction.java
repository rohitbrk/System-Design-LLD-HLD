// Abstraction is hiding details and only showing necessary info to the user/ ( the one who is going to use this abstraction class )
// This can be acheived by using Abstract classes or Interfaces

// interface Animal {
  // the body for these methods should be implemented in the class
  // public void makeSound(); 
  // public void sleep(); 
// }

abstract class Animal {
  public abstract void makeSound();
  public void sleep() {
    System.out.println("sleeping..");
  }
}

class Dog extends Animal {
  public void makeSound() {
    System.out.println("bow bow");
  }
}

class Cat extends Animal {
  public void makeSound() {
    System.out.println("meow meow");
  }
}

class Main {
  public static void main(String[] args) {
    Dog myDog = new Dog(); 
    myDog.makeSound();
    myDog.sleep();
    
    Cat myCat = new Cat(); 
    myCat.makeSound();
    myCat.sleep();
  }
}
