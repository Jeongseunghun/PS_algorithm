import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static int win, lose;
    static int[] gyuCard, inCard;
    static boolean[] used;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            gyuCard = new int[9];
            inCard = new int[9];
            used = new boolean[19];

            // 규영이의 카드
            for (int i = 0; i < 9; i++) {
                int card = Integer.parseInt(st.nextToken());
                gyuCard[i] = card;
                used[card] = true;
            }

            // 인영이의 카드
            int idx = 0;
            for (int i = 1; i <= 18; i++) {
                if (!used[i]) {
                    inCard[idx++] = i;
                }
            }

            win = 0;
            lose = 0;
            permutation(0, 0, 0);

            System.out.println("#" + tc + " " + win + " " + lose);
        }
    }

    // 인영이의 카드 순열 생성 및 게임 결과 판정
    static void permutation(int depth, int gyuSum, int inSum) {
        if (depth == 9) {
            if (gyuSum > inSum) {
                win++;
            } else if (gyuSum < inSum) {
                lose++;
            }
            return;
        }

        for (int i = 0; i < 9; i++) {
            if (!used[inCard[i]]) {
                used[inCard[i]] = true;
                if (gyuCard[depth] > inCard[i]) {
                    permutation(depth + 1, gyuSum + gyuCard[depth] + inCard[i], inSum);
                } else {
                    permutation(depth + 1, gyuSum, inSum + gyuCard[depth] + inCard[i]);
                }
                used[inCard[i]] = false;
            }
        }
    }
}