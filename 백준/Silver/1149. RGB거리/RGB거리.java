import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] rgb;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());

		rgb = new int[N+1][3];
		
		for(int i = 1 ; i <= N ; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			rgb[i][0] = Math.min(rgb[i-1][1],rgb[i-1][2]) + r;
			rgb[i][1] = Math.min(rgb[i-1][0],rgb[i-1][2]) + g;
			rgb[i][2] = Math.min(rgb[i-1][0],rgb[i-1][1]) + b;
		}
		
		System.out.println(Math.min(rgb[N][0], Math.min(rgb[N][1], rgb[N][2])));

	}

}