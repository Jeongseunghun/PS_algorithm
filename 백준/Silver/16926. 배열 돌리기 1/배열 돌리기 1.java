import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		//N: 행, M: 열, R: 회전수 
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[N][M];
		
		//정답 저장할 배열
		int[][] ans = new int[N][M];
		
		for(int i = 0 ; i < N ; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int s = 0;
		
		//겹마다 반복
		while(s < Math.min(N, M) /2) {
			//1차원 배열로 만들기
			ArrayList<Integer> arr = new ArrayList<>();
			
			//상(좌->우)
			for(int i = s; i < M-s; i++) {
				arr.add(board[s][i]);
			}
			
			//우(위->아래)
			for(int i = s+1; i < N-s; i++) {
				arr.add(board[i][M-s-1]);
			}
			//하(우->좌)
			for(int i = s+1; i < M-s; i++) {
				arr.add(board[N-s-1][M-i-1]);
			}
			//좌(아래->위)
			for(int i = s+1; i < N-s-1; i++) {
				arr.add(board[N-i-1][s]);
			}
			
//			//check
//			for(int i : arr)
//				System.out.print(i + " ");
//			System.out.println();
//
			Collections.rotate(arr, -R);
//			
//			//check
//			for(int i : arr)
//				System.out.print(i + " ");
//			System.out.println();

			//ans에 넣기
			//상(좌->우)
			for(int i = s; i < M-s; i++) {
				ans[s][i] = arr.remove(0);
			}

			//우(위->아래)
			for(int i = s+1; i < N-s; i++) {
				ans[i][M-s-1] = arr.remove(0);
			}
			//하(우->좌)
			for(int i = s+1; i < M-s; i++) {
				ans[N-s-1][M-i-1] = arr.remove(0);
			}
					
			//좌(아래->위)
			for(int i = s+1; i < N-s-1; i++) {
				ans[N-i-1][s] = arr.remove(0);
			}
			
			
			s+=1;
		}
		
		//ans
		for(int i = 0 ; i < N; i++) {
			for(int j = 0 ; j< M ; j ++) {
				System.out.print(ans[i][j] + " ");
			}
			System.out.println();
		}
		

	}

}