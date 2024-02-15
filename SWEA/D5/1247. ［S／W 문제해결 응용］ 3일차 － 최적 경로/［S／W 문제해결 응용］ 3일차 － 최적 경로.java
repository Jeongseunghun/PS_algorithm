import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static boolean[] visited;
	static int[][] loc;
	static int ans,N;
	
	public static void main(String[] args) throws NumberFormatException, IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc <= T ; tc++) {
			
			N = Integer.parseInt(br.readLine());
			//위치 좌표
			loc = new int[N+2][2];
			visited = new boolean[N+1];
			
			st = new StringTokenizer(br.readLine());
			//회사 좌표
			loc[0][0] = Integer.parseInt(st.nextToken());
			loc[0][1] = Integer.parseInt(st.nextToken());
			//집 좌표
			loc[N+1][0] = Integer.parseInt(st.nextToken());
			loc[N+1][1] = Integer.parseInt(st.nextToken());
			
			
			for(int i = 1 ; i <= N ; i++) {
				loc[i][0] = Integer.parseInt(st.nextToken());
				loc[i][1] = Integer.parseInt(st.nextToken());
			}
			
			ans = Integer.MAX_VALUE;

			dfs(0,loc[0][0],loc[0][1],0);
			
			System.out.println("#" + tc + " " + ans);
			
		}

	}

	private static void dfs(int cnt, int x, int y, int len) {
		if(cnt == N) {
			len+= dis(x,y,loc[N+1][0],loc[N+1][1]);
			if(len < ans)
				ans = len;
			
			return;
		}
		
		for(int i = 1; i <= N ; i++) {
			if(!visited[i]) {
				visited[i] = true;
				dfs(cnt+1,loc[i][0],loc[i][1],len+dis(x,y,loc[i][0],loc[i][1]));
				visited[i] = false;
			}
		}
		
	}

	private static int dis(int x1, int y1, int x2, int y2) {
		return Math.abs(x1-x2) + Math.abs(y1-y2);
	}

}