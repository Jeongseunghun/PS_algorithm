import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N,r,c;
	static int x,y,cnt = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		int ans = Z((int) Math.pow(2, N),r,c);
		System.out.println(ans);
	
	}

	public static int Z(int n, int r, int c) {
		n /= 2;
		//좌상
		if(r < x + n && c < y + n) {
			cnt += n*n*0;
		//우상
		}else if(r < x + n && c >= y + n) {
			cnt += n*n*1;
			y += n;
		//좌하
		}else if(c < y + n) {
			cnt += n*n*2;
			x += n;
		//우하
		}else {
			cnt += n*n*3;
			x += n;
			y += n;
		}
		if(n == 1) return cnt;
		return Z(n, r, c);
	}


}