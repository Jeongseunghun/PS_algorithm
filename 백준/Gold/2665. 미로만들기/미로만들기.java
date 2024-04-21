import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int N;
    static int[][] visited;
    static int[][] board;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        visited = new int[N][N];
        for(int i = 0; i < N ; i++){
            String s = br.readLine();
            for(int j = 0 ; j < N ; j++){
                board[i][j] = s.charAt(j) - '0';
            }
        }

        bfs();
        
    }
    private static void bfs() {
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[] {0,0});
        visited[0][0] = 1;
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int x = tmp[0];
            int y = tmp[1];
            if(x== N-1 && y == N-1){
                System.out.println(visited[x][y]-1);
                return;
            }
            for(int i = 0 ; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0 <= nx && nx < N && 0 <= ny && ny < N && visited[nx][ny] == 0){
                    //흰 방
                    if(board[nx][ny] == 1){
                        visited[nx][ny] = visited[x][y];
                        q.addFirst(new int[] {nx,ny});
                    }else if(board[nx][ny] == 0){
                        visited[nx][ny] = visited[x][y] + 1;
                        q.add(new int[] {nx,ny});
                    }
                    
                }
            }

        }

    }
    
}