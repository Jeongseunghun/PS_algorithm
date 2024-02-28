import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int K,W,H;
	static int[][][] visited;
	static int[] hdx = {-1,-2,-2,-1,1,2,2,1};
	static int[] hdy = {-2,-1,1,2,-2,-1,1,2};
	static int[] dx = {0,0,-1,1};
	static int[] dy = {-1,1,0,0};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		K = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[H][W];
		for(int i = 0 ; i < H ; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < W; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int ans = bfs(board);
		System.out.println(ans);
	}

	private static int bfs(int[][] board) {
		visited = new int[H][W][K+1];
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[] {0,0,0});
		visited[0][0][0] = 1;
		while(!q.isEmpty()) {
			int[] pos = q.poll();
			int x = pos[0];
			int y = pos[1];
			int z = pos[2];
			
			if(x == H-1 && y == W-1) {
				return visited[x][y][z] - 1;
			}
			
			for(int i = 0 ; i < 4 ; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(0 <= nx && nx < H && 0 <= ny && ny < W && visited[nx][ny][z] == 0  && board[nx][ny] == 0) {
					visited[nx][ny][z] = visited[x][y][z] + 1;
					q.offer(new int[] {nx,ny,z});
				}
			}
			
			if(z<K) {
				for(int i = 0 ; i < 8 ; i++) {
					int hx = x + hdx[i];
					int hy = y + hdy[i];
					if(0 <= hx && hx < H && 0 <= hy && hy < W && visited[hx][hy][z+1] == 0  && board[hx][hy] == 0){
						visited[hx][hy][z+1] = visited[x][y][z] + 1;
						q.offer(new int[] {hx,hy,z+1});
					}
				}
			}
			
		}
		
		return -1;
		
	}

}