public class switchb {

    public static void main (String[] args){
        char not = 'P';
        
        switch(not) {

            case 'A':
            System.out.println("Not A");
            break;

            case 'B':
            System.out.println("Not B");
            break;

            case 'C':
            System.out.println("Not C");
            break;

            case 'P':
            case 'R':
            System.out.println("kaldiniz");
            break;

            case 'D':
            System.out.println("Not D");
            break;

            case 'F':
            System.out.println("Not F");
            break;
            default:
            System.out.println("Geçersiz");

        }
    }
}