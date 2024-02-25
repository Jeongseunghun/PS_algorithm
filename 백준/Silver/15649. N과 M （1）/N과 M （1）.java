import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import static java.lang.System.in;
import static java.lang.System.out;

public class Main {
    static int N,M;
    static int[] ans;
    static boolean[] isSelected;

    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(in));
      StringTokenizer st = new StringTokenizer(br.readLine());

      N = Integer.parseInt(st.nextToken());
      M = Integer.parseInt(st.nextToken());

      ans = new int[M];
      isSelected = new boolean[N+1];
      back(0);

    }
    private static void back(int cnt) {
        StringBuilder sb = new StringBuilder();
        if(cnt == M){
            for(int i : ans) {
                sb.append(i).append(" ");
            }
            out.println(sb);
            return;
        }
        for(int i = 1; i <= N; i++){
            if(!isSelected[i]){
                isSelected[i] = true;
                ans[cnt] = i;
                back(cnt+1);
                isSelected[i] = false;
            }
        }
    }
}