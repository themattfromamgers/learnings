import java.util.Scanner;
public class opaction extends Roles {

    void i() {
        xy = new Scanner(System.in);
        System.out.println("Enter: ");

        y = xy.nextInt();
        sayi = 1;
        sayi2 = 10;
    }

    void iiee() {
       if (sayi < y) {
           System.out.println("1>y");
       } else if(sayi2 >  y) {
           System.out.println("10<y");
        } else {
           System.out.println("else");
       }
    }
}
