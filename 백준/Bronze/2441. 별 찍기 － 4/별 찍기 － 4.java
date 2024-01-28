
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for(int i = 1 ; i <= N ; i++){
            for(int j = 1 ; i-j > 0; j++){
                System.out.print(" ");
            }
            for(int j = N ; j-i >= 0 ; j--){
                System.out.print("*");
            }
            System.out.println();
        }

    }

}
