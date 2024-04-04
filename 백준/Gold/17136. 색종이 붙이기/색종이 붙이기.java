import java.util.Scanner;

public class Main {
    static int[][] board = new int[10][10];
    static int[] paper = new int[5];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Inputting board
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board[i][j] = scanner.nextInt();
            }
        }

        int result = dfs(0, 0, 0);
        if (result == 1e9) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    static int dfs(int x, int y, int cnt) {
        int minVal = 1_000_000_000;

        if (y > 9) {
            minVal = Math.min(minVal, cnt);
            return minVal;
        }

        if (x > 9) {
            return dfs(0, y + 1, cnt);
        }

        if (board[x][y] == 1) {
            for (int k = 0; k < 5; k++) {
                if (paper[k] == 5) {
                    continue;
                }
                if (x + k > 9 || y + k > 9) {
                    continue;
                }

                boolean flag = false;
                for (int i = x; i <= x + k; i++) {
                    for (int j = y; j <= y + k; j++) {
                        if (board[i][j] == 0) {
                            flag = true;
                            break;
                        }
                    }
                    if (flag) {
                        break;
                    }
                }

                if (!flag) {
                    for (int i = x; i <= x + k; i++) {
                        for (int j = y; j <= y + k; j++) {
                            board[i][j] = 0;
                        }
                    }
                    paper[k]++;
                    minVal = Math.min(minVal, dfs(x + k + 1, y, cnt + 1));
                    paper[k]--;

                    for (int i = x; i <= x + k; i++) {
                        for (int j = y; j <= y + k; j++) {
                            board[i][j] = 1;
                        }
                    }
                }
            }
        } else {
            minVal = dfs(x + 1, y, cnt);
        }
        return minVal;
    }
}