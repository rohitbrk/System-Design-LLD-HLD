// Inheritance - Inherit attributes and methods from one class to another

class Box {
    int length;
    int height;
    int width;

    Box(int length, int height, int width) {
        this.length = length;
        this.height = height;
        this.width = width;
    }
}

class BoxWithWeight extends Box {
    int weight;

    BoxWithWeight(int length, int height, int width, int weight) {
        super(length, height, width);
        this.weight = weight;

    }
}

class BoxWithPrice extends BoxWithWeight {
    int price;

    BoxWithPrice(int length, int height, int width, int weight, int price) {
        super(length, height, width, weight);
        this.price = price;
    }
}

public class Inheritance {
    public static void main(String[] args) {
        Box box = new BoxWithPrice(1, 1, 1, 1, 1);
        System.out.print(box.length + "," + box.height + "," + box.width + ",");
    }
}
