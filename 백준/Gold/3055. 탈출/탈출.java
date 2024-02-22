import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int R,C;
	static int gx,gy;
	static char[][] board;
	static Queue<Integer[]> q;
	static int[][] visited;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		q = new LinkedList<>();
		visited = new int[R][C];
		board = new char[R][C];
		
		for(int i = 0 ; i < R ; i++) {
			String a = br.readLine();
			for(int j = 0 ; j < C ; j++) {
				board[i][j] = a.charAt(j);
			}
		}
		
		for(int i = 0 ; i < R; i++) {
			for(int j = 0 ; j < C; j++) {
				if(board[i][j] == 'S') {
					q.add(new Integer[] {i,j});
				}else if(board[i][j] == 'D') {
					gx = i;
					gy = j;
				}
			}
		}
		
		for(int i = 0 ; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(board[i][j] == '*') {
					q.add(new Integer[] {i,j});
				}
			}
		}
		
		
		int ans = bfs(gx,gy);
		if(ans == -1) {
			System.out.println("KAKTUS");
		}else {
			System.out.println(ans);
		}

	}
	private static int bfs(int gx, int gy) {
		while(!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();
			if(board[gx][gy] == 'S') {
				return visited[gx][gy];
			}
			
			for(int i = 0 ; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(0 <= nx && nx < R && 0 <= ny && ny < C) {
					if(board[nx][ny] == '.' || board[nx][ny] == 'D') {
						if(board[x][y] == 'S') {
							board[nx][ny] = 'S';
							visited[nx][ny] = visited[x][y] + 1;
							q.add(new Integer[] {nx,ny});
						}
					}
					if(board[nx][ny] == '.' || board[nx][ny] == 'S') {
						if(board[x][y] == '*') {
							board[nx][ny] = '*';
							q.add(new Integer[] {nx,ny});
						}
					}
					
				}
			}

		}
		
		return -1;
		
	}

}