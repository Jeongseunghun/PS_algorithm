import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//승,패 합은 같아야 함
//무는 짝수여야 함
//총 15경기, 30점

public class Main {
	static int win[],draw[],lose[];
	static boolean flag;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		win = new int[6];
		draw = new int[6];
		lose = new int[6];
		
		
		StringBuilder sb = new StringBuilder();
		//4가지 경우
		for(int tc = 0 ; tc < 4; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int ans = 0;
			for(int i = 0 ; i < 6 ; i++) {
				ans += win[i] = Integer.parseInt(st.nextToken());
				ans += draw[i] = Integer.parseInt(st.nextToken());
				ans += lose[i] = Integer.parseInt(st.nextToken());
			}
			flag = false;
			if(ans == 30) {
				dfs(0,0,1);
			}
			
			if(!flag) {
				sb.append(0).append(" ");
			}else {
				sb.append(1).append(" ");
			}
					
		}
		System.out.println(sb);
		
	}

	private static void dfs(int team, int game, int idx) {
		if(flag) return;
		if(win[team] < 0 || lose[team] < 0 || draw[team] < 0 || win[team+idx-1] < 0 || lose[team+idx-1] < 0 || draw[team+idx-1] < 0)
			return;
		if(game == 15) {
			flag = true;
			return;
		}
		
		if(game == 5) {
			team++;
			idx = 1;
		}
		else if(game == 9) {
			team++;
			idx = 1;
		}
		else if(game == 12) {
			team++;
			idx = 1;
		}
		else if(game == 14) {
			team++;
			idx = 1;
		}
		
		win[team]--;
		lose[team+idx]--;
		dfs(team,game+1,idx+1);
		win[team]++;
		lose[team+idx]++;
		
		win[team+idx]--;
		lose[team]--;
		dfs(team,game+1,idx+1);
		win[team+idx]++;
		lose[team]++;
		
		draw[team]--;
		draw[team+idx]--;
		dfs(team,game+1,idx+1);
		draw[team]++;
		draw[team+idx]++;
		
	}

}