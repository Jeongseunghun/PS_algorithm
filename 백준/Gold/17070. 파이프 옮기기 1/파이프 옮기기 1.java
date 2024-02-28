import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N+1][N+1];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 0 : 가로 , 1 : 세로, 2 : 대각선
        int[][][] dp = new int[N+1][N+1][3];

        dp[1][2][0] = 1;

        for (int i = 1; i <= N; i++) {
            for (int j = 2; j <= N; j++) {
                // 벽
                if (board[i][j] == 1) {
                    continue;
                }
                
                // 가로
                dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2];
                // 세로
                dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2];
                // 대각선
                if (board[i - 1][j] != 1 && board[i][j - 1] != 1) {
                    dp[i][j][2] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2];
                }
            }
        }

        System.out.println(dp[N][N][0] + dp[N][N][1] + dp[N][N][2]);
    }
}