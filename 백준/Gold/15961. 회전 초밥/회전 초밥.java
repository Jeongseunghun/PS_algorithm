import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        HashMap<Integer, Integer> map = new HashMap<>();
        int[] belt = new int[N];
        for (int i = 0; i < N; i++) {
            belt[i] = Integer.parseInt(br.readLine());
        }

        int ans = 0;
        for (int i = 0; i < k; i++) {
            map.put(belt[i], map.getOrDefault(belt[i], 0) + 1);
        }
        map.put(c, map.getOrDefault(c, 0) + 1);

        for (int i = 0; i < N; i++) {
            int s = i;
            int next = (i + k) % N;

            map.put(belt[s], map.get(belt[s]) - 1);
            if (map.get(belt[s]) == 0) {
                map.remove(belt[s]);
            }

            map.put(belt[next], map.getOrDefault(belt[next], 0) + 1);

            ans = Math.max(ans, map.size());
        }

        System.out.println(ans);
    }
}