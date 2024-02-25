import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.System.in;
import static java.lang.System.out;

public class Main {
    static int N,M;
    static int[] ans;
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(in));
      StringTokenizer st = new StringTokenizer(br.readLine());

      N = Integer.parseInt(st.nextToken());
      M = Integer.parseInt(st.nextToken());

      ans = new int[M];
      back(0,1);

    }

    private static void back(int cnt,int s) {
        if(cnt == M){
            for(int i : ans){
                out.print(i+ " ");
            }
            out.println();
            return;
        }
        for(int i = s ; i <= N ; i++){
            ans[cnt] = i;
            back(cnt+1,i+1);
        }

    }
}