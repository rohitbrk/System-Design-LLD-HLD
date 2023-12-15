class Phone {
    private int RAM;

    Phone() {
        this.RAM = 4;
    }

    public int getRam() {
        return RAM;
    }

    public void setRam(int RAM) {
        // the selection would be made only if the user selects RAM as per conditions
        if (RAM < 12 && RAM > 3) {
            this.RAM = RAM;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Phone phone1 = new Phone();
        System.out.println(phone1.getRam());
        phone1.setRam(6);
        System.out.println(phone1.getRam());
        phone1.setRam(1);
        System.out.println(phone1.getRam());
        phone1.setRam(13);
        System.out.println(phone1.getRam());
    }
}
