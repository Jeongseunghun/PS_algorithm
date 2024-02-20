import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int[][] city = new int[N][N];
        List<int[]> chicken = new ArrayList<>();
        List<int[]> house = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                city[i][j] = Integer.parseInt(row[j]);
                if (city[i][j] == 2) {
                    chicken.add(new int[]{i, j});
                }
                if (city[i][j] == 1) {
                    house.add(new int[]{i, j});
                }
            }
        }

        int res = 999999;
        
        List<List<int[]>> chickenCombinations = new ArrayList<>();
        combine(chicken, M, 0, new ArrayList<>(), chickenCombinations);

        for (List<int[]> comb : chickenCombinations) {
            int tmp = 0;
            for (int[] i : house) {
                int min_d = 99;
                for (int[] j : comb) {
                    min_d = Math.min(min_d, Math.abs(j[0] - i[0]) + Math.abs(j[1] - i[1]));
                }
                tmp += min_d;
            }
            res = Math.min(res, tmp);
        }

        System.out.println(res);
    }

    private static void combine(List<int[]> chicken, int m, int start, List<int[]> temp, List<List<int[]>> result) {
        if (temp.size() == m) {
            result.add(new ArrayList<>(temp));
            return;
        }
        for (int i = start; i < chicken.size(); i++) {
            temp.add(chicken.get(i));
            combine(chicken, m, i + 1, temp, result);
            temp.remove(temp.size() - 1);
        }
    }
}