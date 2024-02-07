import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int paper = Integer.parseInt(br.readLine());
		int[][] board = new int[100][100];
		int cnt = 0;
		for(int i = 0 ; i < paper ; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			for(int x = s ; x < s+10 ; x++) {
				for(int y = e ; y < e+10 ; y++) {
					if(board[x][y] != 1) {
						board[x][y] = 1;
						cnt +=1;
					}
				}
			}
		}
		
		System.out.println(cnt);

	}

}