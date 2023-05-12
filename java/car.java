public class car {

    public static void main (String[] args) {

        String yazi1 = "buvak";
        String yazi2 = "emme";

        int birincil = yazi1.length();
        int ikincil = yazi2.length();

        int toplama = birincil + ikincil;

    

        if (birincil > ikincil) {
            System.out.println("Birincil, ikincil'den büyüktür." + birincil);
            System.out.println("Toplam:" +toplama);
        }

        if (ikincil > birincil) {
            System.out.println("İkincil, birincil'den büyüktür." + ikincil);
            System.out.println("Toplam:" +toplama); 
        } 

    } 
}
