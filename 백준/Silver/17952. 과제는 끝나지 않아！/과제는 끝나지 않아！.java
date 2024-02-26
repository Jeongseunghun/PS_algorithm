import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int ans = 0;
	static Stack<Integer[]> stack;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		stack = new Stack<>();
		
		for(int i = 0 ; i < N ; i++) {
		
			st = new StringTokenizer(br.readLine());
			int c = Integer.parseInt(st.nextToken());
			if(c==1) {
				int A = Integer.parseInt(st.nextToken());
				int T = Integer.parseInt(st.nextToken());
				stack.add(new Integer[] {A,T});
				stack.peek()[1] -=1;
				if(stack.peek()[1] == 0) {
					ans+=stack.peek()[0];
					stack.pop();
				}

			}else if(c==0) {
				if(!stack.isEmpty()) {
				stack.peek()[1] -=1;
				if(stack.peek()[1] == 0) {
					ans+=stack.peek()[0];
					stack.pop();
				}
			}
			}
			
		}
		
		System.out.println(ans);
		
	}

}