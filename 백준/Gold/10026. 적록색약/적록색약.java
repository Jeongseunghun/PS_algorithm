import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static char board[][];
	static int N;
	static int visited[][];
	static int ans1,ans2;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(br.readLine());
		
		board = new char[N][N];
		for(int i = 0 ; i < N ; i++) {
			String t = br.readLine();
			for(int j = 0; j < N ; j++) {
				board[i][j] = t.charAt(j);
			}
		}
	
		
		ans1 = 0;
		//적록색약X
		visited = new int[N][N];
		for(int i = 0 ; i < N ; i++) {
			for(int j = 0 ; j < N ; j++) {
				if(visited[i][j] == 0) {
					rgb(i,j);
					ans1+=1;
				}
					
		
			}
		}
		
		ans2 = 0;
		//적록색약
		visited = new int[N][N];
		for(int i = 0 ; i < N; i++) {
			for(int j = 0 ; j < N ; j++) {
				if(board[i][j] == 'R') {
					board[i][j] = 'G';
				}
			}
		}
		
		
		for(int i = 0 ; i < N; i++) {
			for(int j = 0 ; j < N ; j++) {
				if(visited[i][j] == 0) {
					rgb(i,j);
					ans2+=1;
				}
					
			}
		}
		

		
		sb.append(ans1).append(" ").append(ans2);
		System.out.println(sb);
		

	}
	
	private static void rgb(int i , int j) {
		Queue<Integer[]> q = new LinkedList<>();
		q.add(new Integer[] {i,j});
		char color = board[i][j];
		visited[i][j] = 1;
		while(!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.remove();
			for(int d = 0 ; d < 4 ; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if(0 <= nx && nx < N && 0 <= ny && ny < N) {
					if(board[nx][ny] == color && visited[nx][ny] == 0) {
						visited[nx][ny] = 1;
						q.add(new Integer[] {nx,ny});

					}
				}
			}
		}

	}




}