import java.util.*;

public class Main {
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static int inf = (int)1e9;

    static class Node implements Comparable<Node> {
        int cost, x, y;

        Node(int cost, int x, int y) {
            this.cost = cost;
            this.x = x;
            this.y = y;
        }

        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    static void dijkstra(int[][] board, int N) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(board[0][0], 0, 0));
        board[0][0] = 0;

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int c = current.cost;
            int x = current.x;
            int y = current.y;

            if (x == N - 1 && y == N - 1) {
                System.out.printf("Problem %d: %d%n", cnt, visited[N - 1][N - 1]);
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    int nc = c + board[nx][ny];
                    if (visited[nx][ny] > nc) {
                        visited[nx][ny] = nc;
                        pq.add(new Node(nc, nx, ny));
                    }
                }
            }
        }
    }

    static int cnt = 1;
    static int[][] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            int N = scanner.nextInt();
            if (N == 0) break;

            int[][] board = new int[N][N];
            visited = new int[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    board[i][j] = scanner.nextInt();
                    visited[i][j] = inf;
                }
            }

            dijkstra(board, N);
            cnt++;
        }

        scanner.close();
    }
}