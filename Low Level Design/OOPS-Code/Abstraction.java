// Abstraction is hiding details and only showing necessary info to the user
// This can be acheived by using Abstract Classes or Interfaces

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

class Main {
  public static void main(String[] args) {
    Dog myDog = new Dog(); // Create a Pig object
    myDog.makeSound();
    myDog.sleep();
  }
}
