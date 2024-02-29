import java.util.*;
import java.io.*;

public class Main {
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    static int bfs(int[][] tmp_board, List<Pair<Integer, Integer>> virus_lst, int N, int M) {
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        int[][] visited = new int[N][M];
        for (Pair<Integer, Integer> i : virus_lst) {
            q.add(i);
        }
        while (!q.isEmpty()) {
            Pair<Integer, Integer> pair = q.poll();
            int x = pair.getKey();
            int y = pair.getValue();
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    if (visited[nx][ny] == 0 && tmp_board[nx][ny] == 0) {
                        q.add(new Pair<>(nx, ny));
                        visited[nx][ny] = 1;
                        tmp_board[nx][ny] = 2;
                    }
                }
            }
        }

        int res = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (tmp_board[i][j] == 0) {
                    res++;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] board = new int[N][M];

        // 바이러스 위치
        List<Pair<Integer, Integer>> virus_lst = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 2) {
                    virus_lst.add(new Pair<>(i, j));
                }
            }
        }

        List<Pair<Integer, Integer>> wall = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] != 1 && board[i][j] != 2) {
                    wall.add(new Pair<>(i, j));
                }
            }
        }

        List<List<Pair<Integer, Integer>>> wall_candi = new ArrayList<>();
        for (int i = 0; i < wall.size(); i++) {
            for (int j = i + 1; j < wall.size(); j++) {
                for (int k = j + 1; k < wall.size(); k++) {
                    List<Pair<Integer, Integer>> combination = new ArrayList<>();
                    combination.add(wall.get(i));
                    combination.add(wall.get(j));
                    combination.add(wall.get(k));
                    wall_candi.add(combination);
                }
            }
        }

        int ans = 0;
        for (List<Pair<Integer, Integer>> combination : wall_candi) {
            int[][] tmp_board = new int[N][M];
            for (int i = 0; i < N; i++) {
                tmp_board[i] = Arrays.copyOf(board[i], M);
            }
            for (Pair<Integer, Integer> j : combination) {
                tmp_board[j.getKey()][j.getValue()] = 1;
            }
            int res = bfs(tmp_board, virus_lst, N, M);
            ans = Math.max(ans, res);
        }

        System.out.println(ans);
    }
    
    static class Pair<X, Y> {
        private final X first;
        private final Y second;

        public Pair(X first, Y second) {
            this.first = first;
            this.second = second;
        }

        public X getKey() {
            return first;
        }

        public Y getValue() {
            return second;
        }
    }
}