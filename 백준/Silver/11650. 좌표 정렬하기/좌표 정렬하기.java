import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        board = new int[N][2];
        for(int i = 0 ; i < N; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            board[i][0] = x;
            board[i][1] = y;
        }

        Arrays.sort(board, (e1,e2) -> {
            if(e1[0] == e2[0]) {
                return e1[1] - e2[1];
            }else{
                return e1[0] - e2[0];
            }
        });

        for(int i = 0 ; i < N ; i++){
            sb.append(board[i][0]).append(" ").append(board[i][1]).append('\n');
        }

        System.out.println(sb);
    }

}