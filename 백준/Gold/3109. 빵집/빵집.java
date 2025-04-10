import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int R,C,cnt = 0;
	static char[][] board;
	static boolean[][] chk;
	//오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선
	static int[] dc = {-1,0,1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new char[R][C];
		
		for(int i = 0 ; i < R ; i++) {
			String l = br.readLine();
			for(int j = 0 ; j < C; j++) {
				board[i][j] = l.charAt(j);
			}
		}
		
		for(int i = 0 ; i < R ; i++) {
			dfs(0,i);
		}
		System.out.println(cnt);

	}

	private static boolean dfs(int x, int y) {
		for(int i=0; i<3; i++) {
			int nx = x + 1;
			int ny = y + dc[i];
			
			if(nx < 0 || nx > C-1 || ny < 0 || ny > R-1)
				continue;
			if(board[ny][nx] =='.') {
				if(nx == C-1) {
					cnt ++;
					return true;
				}
				
				board[ny][nx] = 'O';
  			   if(dfs(nx,ny))
  				   return true;
			}
			
		}
		return false;
	}
		
}