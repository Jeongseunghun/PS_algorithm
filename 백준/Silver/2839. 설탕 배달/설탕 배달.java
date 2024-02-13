import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int ans = 0;
		while(N>=0) {
			if(N%5 == 0){
				ans += N /= 5;
				System.out.println(ans);
				System.exit(0);;
			}
			N-=3;
			ans+=1;
		}
		System.out.println(-1);
	
	}
}