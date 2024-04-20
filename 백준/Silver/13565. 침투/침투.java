import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

import static java.lang.System.in;
import static java.lang.System.out;

public class Main {
    static int M,N;
    static int[][] board;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int[][] visited;
    static Queue<int []> q;

    static boolean Flag;

    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      M = Integer.parseInt(st.nextToken());
      N = Integer.parseInt(st.nextToken());
      q = new LinkedList<>();
      board = new int[M][N];
      visited = new int[M][N];
      for(int i = 0 ; i < M ; i++){
          String b = br.readLine();
          for(int j = 0 ; j < N ; j++){
              board[i][j] = b.charAt(j) - '0';
              if(i == 0 && board[i][j] == 0){
                  q.add(new int[] {i,j});
                  visited[i][j] = 1;
              }
          }
      }

      Flag = bfs();

      if(Flag == true){
          out.println("YES");
        } else{
          out.println("NO");
        }

    }
    private static boolean bfs() {

        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int x = tmp[0];
            int y = tmp[1];
            if(x == M-1){
                return true;
            }
            for(int i = 0 ; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0<= nx && nx < M && 0<= ny && ny < N && visited[nx][ny] == 0 && board[nx][ny] == 0){
                    visited[nx][ny] = 1;
                    q.add(new int[] {nx,ny});
                }
            }
        }

        return false;
    }
}