public class dersone {

       public static void main(String[] args) {

            //For Döngüsü
           for(int i=1;i<10000;i++) {
            System.out.println(i);
           }

           System.out.println("End");

           int i = 1;
           //While
           while(i<10) {
               System.out.println(i);
               i++; //tek sayılar
               //i+=2; //çift sayı
           }
           System.out.print("End: While");

           //Do-while döngüsü
           int j=1;
           do{
               
                System.out.print(j);
                j+=2;
             
               
           }while (i<10);
           
           System.out.println("End: do-while");

         
       }

}