// Class - An object constructor, or a "blueprint" for creating objects.
// Object - An instance of a Class
// Class can be used to represent any real world entity by using properties and methods
// For example, A Person class can have properties like "planet" and methods like "run".

// class Person defines the properties(planet) and methods(run)
// Every object that is created by the Person class will have these properties/ methods

class Person {
    String planet = "earth";
    int id;
    public Person(int id) {
        this.id = id;
    }
    void run() {
        System.out.println("running ..");
    }
}

class Main {
    public static void main(String[] args) {
        // person1 is the actual object/ instance that is created based on class Person
        Person person1 = new Person(1011);
        System.out.println(person1.id);
        System.out.println(person1.planet);
        person1.run();
    }
}