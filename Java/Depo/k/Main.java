import java.util.Scanner;


public class Main {

    public static void main(String[] args) {

        YabguK yabguK = new YabguK();

        Scanner x = new Scanner(System.in);
        System.out.print("Enter: ");
        String y = x.nextLine();

        switch (y) {
            case "İlber Ortaylı":
                yabguK.turklerintarihi();
                yabguK.turklerinaltincagi();

        }



    }
}
