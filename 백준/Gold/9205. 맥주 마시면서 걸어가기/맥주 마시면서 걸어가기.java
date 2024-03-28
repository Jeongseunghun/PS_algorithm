import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

class Main {

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void bfs(int hx, int hy, int fx, int fy, Point[] stores, int n) {
        Queue<Point> q = new ArrayDeque<>();
        q.add(new Point(hx, hy));
        while (!q.isEmpty()) {
            Point p = q.poll();
            int x = p.x;
            int y = p.y;
            if (Math.abs(x - fx) + Math.abs(y - fy) <= 1000) {
                System.out.println("happy");
                return;
            }
            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    Point store = stores[i];
                    int nx = store.x;
                    int ny = store.y;
                    if (Math.abs(x - nx) + Math.abs(y - ny) <= 1000) {
                        visited[i] = 1;
                        q.add(new Point(nx, ny));
                    }
                }
            }
        }
        System.out.println("sad");
    }

    static int[] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int test = 0; test < t; test++) {
            int n = scanner.nextInt();
            int hx = scanner.nextInt();
            int hy = scanner.nextInt();
            Point[] stores = new Point[n];
            for (int j = 0; j < n; j++) {
                int x = scanner.nextInt();
                int y = scanner.nextInt();
                stores[j] = new Point(x, y);
            }
            int fx = scanner.nextInt();
            int fy = scanner.nextInt();
            visited = new int[n + 1];
            bfs(hx, hy, fx, fy, stores, n);
        }
    }
}