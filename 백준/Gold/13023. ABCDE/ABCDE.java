import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

     static int answer = 0;
     static int N,M;
     static ArrayList<Integer>[] edgeList;
     static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        String[] split = line.split(" ");

        N = Integer.parseInt(split[0]);
        M = Integer.parseInt(split[1]);
        visited = new boolean[N];
        edgeList = new ArrayList[N];

        for (int i = 0; i < N; i++) {
            edgeList[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            String line1 = br.readLine();
            String[] split1 = line1.split(" ");
            int from = Integer.parseInt(split1[0]);
            int to = Integer.parseInt(split1[1]);
            edgeList[from].add(to);
            edgeList[to].add(from);
        }

        for (int i = 0; i < N; i++) {
            if (answer != 1) dfs(i, 1);
        }

        System.out.println(answer + "\n");

    }

    public static void dfs(int s, int cnt) {
        if (cnt == 5) {
            answer = 1;
            return;
        }
        visited[s] = true;
        for (int to : edgeList[s]) {
            if (!visited[to]) {
                dfs(to, cnt + 1);
            }
        }
        visited[s] = false;
    }
}