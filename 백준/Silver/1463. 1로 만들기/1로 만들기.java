import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int[] dp;
	static int N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		dp = new int[1000001];
		dp[0] = 0;
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		
		for(int i = 4 ; i <= N ; i++) {
			dp[i] = dp[i-1] + 1;
			if(i%3 == 0) {
				dp[i] = Math.min(dp[i/3]+1,dp[i]);
			}if(i%2 == 0) {
				dp[i] = Math.min(dp[i/2]+1,dp[i]);
			}
		}
		
		System.out.println(dp[N]);

	}

}