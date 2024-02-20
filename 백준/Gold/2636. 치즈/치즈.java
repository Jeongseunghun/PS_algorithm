import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N,M,cnt,ans;
	static int[][] board;
	static int[][] visited;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static ArrayList<Integer> cz;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		board = new int[N][M];
		for(int i = 0 ; i < N ; i++) {
			st = new StringTokenizer(br.readLine()," ");
			for(int j = 0 ; j < M ; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		cz = new ArrayList<>();
		

		ans = 0;
		while(true) {
			visited = new int[N][M];
			int cnt = bfs();
			
			for(int i = 0 ; i < N ; i++) {
				for(int j = 0 ; j < M; j++) {
					if(visited[i][j] > 1) {
						board[i][j] = 0;
					}
				}
			}
			
			
			if(cnt == 0) {
				System.out.println(ans);
				System.out.println(cz.get(cz.size()-2));
				break;
			}
			ans+=1;

		}

	}


	private static int bfs() {
		
		int tmp = 0;
		visited[0][0] = 1;
		Queue<Integer[]> q = new LinkedList<>();
		q.add(new Integer[] {0,0});
		while(!q.isEmpty()) {
			int x = q.peek()[0];
			int y = q.peek()[1];
			q.poll();
			for(int d = 0 ; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if(0 <= nx && nx < N && 0 <= ny && ny < M && visited[nx][ny] == 0) {
					if(board[nx][ny] == 1) {
						visited[nx][ny] = visited[x][y] + 1;
						tmp+=1;
						
					}else if(board[nx][ny] == 0){
						q.add(new Integer[] {nx,ny});
						visited[nx][ny] = 1;
					}
				}
			}

		}
		
		cz.add(tmp);
		return tmp;
		
		
		
	}

}