import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] board;
    static int[] visited;
    static int m = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        visited = new int[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited[0] = 1;
        dfs(0, 0, 0);

        System.out.println(m);
    }

    static void dfs(int cnt, int s, int cost) {
        if (cnt == N - 1 && board[s][0] != 0) {
            m = Math.min(m, cost + board[s][0]);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visited[i] != 1 && board[s][i] != 0) {
                visited[i] = 1;
                dfs(cnt + 1, i, cost + board[s][i]);
                visited[i] = 0;
            }
        }
    }
}