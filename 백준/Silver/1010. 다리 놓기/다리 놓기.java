import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		
		for(int tc = 0 ; tc < T; tc++) {
			long res = 1;
			st = new StringTokenizer(br.readLine());
			long N = Integer.parseInt(st.nextToken());
			long M = Integer.parseInt(st.nextToken());
			
			for(int i = 0; i < N; i++) {
				res = res * (M-i);
				res /= i+1;
			}
			
			System.out.println(res);
			}
		}

	}