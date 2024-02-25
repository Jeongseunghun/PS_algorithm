import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

import static java.lang.System.in;
import static java.lang.System.out;

public class Main {
    static int N,M,V;
    static ArrayList<Integer>[] arr;
    static int[] visited;

    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      N = Integer.parseInt(st.nextToken());
      M = Integer.parseInt(st.nextToken());
      V = Integer.parseInt(st.nextToken());
      arr = new ArrayList[N+1];
      for(int i = 0 ; i < arr.length ; i++){
          arr[i] = new ArrayList<>();
      }
      for(int i = 1 ; i <= M ; i++){
          st = new StringTokenizer(br.readLine());
          int a = Integer.parseInt(st.nextToken());
          int b = Integer.parseInt(st.nextToken());
          arr[b].add(a);
          arr[a].add(b);
      }

      for(int i = 0 ; i <= N; i++){
          Collections.sort(arr[i]);
      }

      visited = new int[N+1];
      dfs(V);

      out.println();
      bfs(V);

    }

    private static void dfs(int v) {
        visited[v] = 1;
        out.print(v + " ");
        for(int i : arr[v]){
            if(visited[i] == 0){
                dfs(i);
            }
        }
    }

    private static void bfs(int v) {
        visited = new int[N+1];
        Queue<Integer> q = new LinkedList<>();
        q.offer(v);
        visited[v] = 1;
        while(!q.isEmpty()){
            int x = q.poll();
            out.print(x + " ");
            for(int i : arr[x]){
                if(visited[i] == 0){
                    q.offer(i);
                    visited[i] = 1;
                }
            }
        }


    }
}