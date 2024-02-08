import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] lst = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < N ; i++) {
			lst[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] res = new int[N];
		
		//정답 저장
		Stack<int[]> stack = new Stack<>();

		for(int j = 0 ; j < N ; j++) {
			while(stack.size() > 0) {
				if(stack.peek()[1] < lst[j]) {
					stack.pop();
				}
				else {
					res[j] = stack.peek()[0] + 1;
					break;
				}
				
			}
			stack.push(new int[] {j,lst[j]});
		}
		
		StringBuilder sb = new StringBuilder();
		
		for(int i : res)
			sb.append(i).append(" ");
	
		System.out.println(sb);
	}
	
	

}