import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int[] ans = new int[N];
		
		ArrayList<Integer> lst = new ArrayList<>();
		for(int i = 1 ; i <= N; i++) {
			lst.add(i);
		}
		
		for(int i = 0 ; i < N-1 ; i++) {
			Collections.rotate(lst, -(K-1));
			sb.append(lst.remove(0)).append(", ");
		}
		sb.append(lst.remove(0));
		sb.append(">");
		System.out.println(sb);

	}

}