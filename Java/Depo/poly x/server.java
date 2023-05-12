//Inheritance

class server {

    public static void main(String[] args) {

    insan ali = new insan();
    kaganlar kagan = new kaganlar();

    kagan.boy = 180;
    kagan.kilo = 70;
    System.out.println(kagan.kilo);
    kagan.yemek();
    System.out.println(kagan.kilo);
    System.out.println(kagan.maas);
    kagan.maas = 5000;
    kagan.zam();
    System.out.println(kagan.maas);
    System.out.println("*-----------------*");
    System.out.println(ali.kilo);
    ali.yemek();
    System.out.println(ali.kilo);






    }
}