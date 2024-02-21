import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

//최소 1개 모음 + 최소 2개 자음
public class Main {
	static char[] vowel = {'a','e','i','o','u'};
	static int L,C;
	static char[] pw;
	static ArrayList<Character> ans;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		pw = new char[C];
		for(int i = 0 ; i < C; i++) {
			pw[i] = st.nextToken().charAt(0);
		}
		
		Arrays.sort(pw);
		
		ans = new ArrayList<>();
		
		back(0,0);
		
		
	}
	private static void back(int cnt, int s) {
		if(cnt == L) {

			int v = 0;
			int c = 0;
			
			for(int t = 0 ; t < ans.size(); t++) {
				if(ans.get(t) == 'a' || ans.get(t) == 'e' || ans.get(t) == 'i' || ans.get(t) == 'o' || ans.get(t) == 'u') {
						v++;
				} else {
						c++;
					}
			}
					
				
			if(v >= 1 && c >= 2) {
				for(char i : ans) {
					System.out.print(i);
				}
				System.out.println();
				return;
			}else {
				return;
			}
		}
			
		for(int i = s ; i < C ; i++) {
			ans.add(pw[i]);
			back(cnt+1,i+1);
			ans.remove(ans.size()-1);
			
		}
			
		
		
		
	}

}