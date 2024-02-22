import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.List;
import java.util.Arrays;

public class Main {
    static int N;
    static int[] lst;
    static List<Integer>[] area;
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        lst = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            lst[i] = Integer.parseInt(st.nextToken());
        }

        area = new ArrayList[N + 1];
        
        for (int i = 1; i <= N; i++) {
        	st = new StringTokenizer(br.readLine());
            area[i] = new ArrayList<>();
            int count = Integer.parseInt(st.nextToken());
            for (int j = 0; j < count; j++) {
                area[i].add(Integer.parseInt(st.nextToken()));
            }
        }

        for (int i = 1; i <= N / 2; i++) {
            List<List<Integer>> combi = combinations(N, i);
            for (List<Integer> c : combi) {
                int[] cArr = new int[c.size()];
                for (int k = 0; k < c.size(); k++) {
                    cArr[k] = c.get(k);
                }
                int[] cArrComplement = getComplement(cArr);
                int[] res1 = bfs(cArr);
                int[] res2 = bfs(cArrComplement);
                if (res1[1] + res2[1] == N) {
                    res = Math.min(res, Math.abs(res1[0] - res2[0]));
                }
            }
        }

        if (res != Integer.MAX_VALUE) {
            System.out.println(res);
        } else {
            System.out.println(-1);
        }
    }

    static int[] bfs(int[] arr) {
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        q.offer(arr[0]);
        visited.add(arr[0]);
        int num = 0;
        while (!q.isEmpty()) {
            int x = q.poll();
            num += lst[x];
            for (int i : area[x]) {
                if (!visited.contains(i) && contains(arr, i)) {
                    q.offer(i);
                    visited.add(i);
                }
            }
        }
        return new int[]{num, visited.size()};
    }

    static boolean contains(int[] arr, int target) {
        for (int num : arr) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }

    static List<List<Integer>> combinations(int n, int r) {
        List<List<Integer>> result = new ArrayList<>();
        int[] indices = new int[r];
        for (int i = 0; i < r; i++) {
            indices[i] = i;
        }
        while (true) {
            List<Integer> combination = new ArrayList<>();
            for (int index : indices) {
                combination.add(index + 1);
            }
            result.add(combination);
            int next = r - 1;
            while (next >= 0 && indices[next] == n - r + next) {
                next--;
            }
            if (next < 0) {
                break;
            }
            indices[next]++;
            for (int i = next + 1; i < r; i++) {
                indices[i] = indices[i - 1] + 1;
            }
        }
        return result;
    }

    static int[] getComplement(int[] arr) {
        int[] complement = new int[N - arr.length];
        int complementIndex = 0;
        Arrays.sort(arr);
        int arrIndex = 0;
        for (int i = 1; i <= N; i++) {
            if (arrIndex < arr.length && i == arr[arrIndex]) {
                arrIndex++;
            } else {
                complement[complementIndex++] = i;
            }
        }
        return complement;
    }
}