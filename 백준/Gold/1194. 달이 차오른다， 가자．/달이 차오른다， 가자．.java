import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static char[] keyDict = {'a', 'b', 'c', 'd', 'e', 'f'};
    static char[] doorDict = {'A', 'B', 'C', 'D', 'E', 'F'};

    static int bfs(int i, int j, char[][] board) {
        int[][][] visited = new int[board.length][board[0].length][64];
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{i, j, 0});
        int cnt = -1;
        visited[i][j][0] = 1;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int z = current[2];

            if (board[x][y] == '1') {
                cnt = visited[x][y][z] - 1;
                break;
            }

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (0 <= nx && nx < board.length && 0 <= ny && ny < board[0].length && board[nx][ny] != '#' && visited[nx][ny][z] == 0) {
                    // If it's a key
                    if (isKey(board[nx][ny])) {
                        int nz = z | (1 << (board[nx][ny] - 'a'));
                        if (visited[nx][ny][nz] == 0) {
                            q.add(new int[]{nx, ny, nz});
                            visited[nx][ny][nz] = visited[x][y][z] + 1;
                        }
                    }
                    // If it's a door
                    else if (isDoor(board[nx][ny])) {
                        if ((z & (1 << (board[nx][ny] - 'A'))) != 0) {
                            q.add(new int[]{nx, ny, z});
                            visited[nx][ny][z] = visited[x][y][z] + 1;
                        }
                    }
                    // If it's a path
                    else {
                        q.add(new int[]{nx, ny, z});
                        visited[nx][ny][z] = visited[x][y][z] + 1;
                    }
                }
            }
        }
        return cnt;
    }

    static boolean isKey(char c) {
        for (char key : keyDict) {
            if (c == key)
                return true;
        }
        return false;
    }

    static boolean isDoor(char c) {
        for (char door : doorDict) {
            if (c == door)
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        scanner.nextLine();

        char[][] board = new char[N][M];
        for (int i = 0; i < N; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == '0') {
                    int ans = bfs(i, j, board);
                    System.out.println(ans);
                }
            }
        }
    }
}