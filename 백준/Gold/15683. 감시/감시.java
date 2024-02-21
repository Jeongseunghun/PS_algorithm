import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
 
public class Main {
    static int n, m, ans;
    static int[][] arr;
    static ArrayList<CCTV> cctv = new ArrayList<CCTV>();
    static int[] cctv_dir = {4, 2, 4, 4, 1};
 
    static class CCTV {
        int r;
        int c;
        int type;
 
        public CCTV(int r, int c, int type) {
            this.r = r;
            this.c = c;
            this.type = type;
        }
    }
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
 
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = Integer.MAX_VALUE;
        arr = new int[n][m];
 
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
 
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
 
                if (arr[i][j] != 0 && arr[i][j] != 6) {
                    cctv.add(new CCTV(i, j, arr[i][j] - 1));
                }
            }
        }
 
        solve(0);
 
        bw.write(Integer.toString(ans));
        br.close();
        bw.flush();
        bw.close();
    }
 
    static void solve(int cctv_idx) {
        if (cctv_idx == cctv.size()) {
            int cnt = 0;
 
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == 0) {
                        cnt++;
                    }
                }
            }
 
            if (cnt < ans) {
                ans = cnt;
            }
 
            return;
        }
 
        int cctv_type = cctv.get(cctv_idx).type;
        int[][] tmp = new int[n][m];
 
        for (int i = 0; i < cctv_dir[cctv_type]; i++) {
            copyArr(arr, tmp);
 
            if (cctv_type == 0) {
                update(cctv.get(cctv_idx), i);
            } else if (cctv_type == 1) {
                update(cctv.get(cctv_idx), i);
                update(cctv.get(cctv_idx), i + 2);
            } else if (cctv_type == 2) {
                update(cctv.get(cctv_idx), i);
                update(cctv.get(cctv_idx), i + 1);
            } else if (cctv_type == 3) {
                update(cctv.get(cctv_idx), i);
                update(cctv.get(cctv_idx), i + 1);
                update(cctv.get(cctv_idx), i + 2);
            } else { // cctv_type == 4
                update(cctv.get(cctv_idx), i);
                update(cctv.get(cctv_idx), i + 1);
                update(cctv.get(cctv_idx), i + 2);
                update(cctv.get(cctv_idx), i + 3);
            }
 
            solve(cctv_idx + 1);
            copyArr(tmp, arr);
        }
    }
 
    static void copyArr(int[][] from, int[][] to) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                to[i][j] = from[i][j];
            }
        }
    }
 
    static void update(CCTV tv, int dir) {
        dir %= 4;
 
        if (dir == 0) {
            for (int i = tv.c + 1; i < m; i++) {
                if (arr[tv.r][i] == 6) {
                    break;
                }
 
                arr[tv.r][i] = -1;
            }
        } else if (dir == 1) {
            for (int i = tv.r - 1; i >= 0; i--) {
                if (arr[i][tv.c] == 6) {
                    break;
                }
 
                arr[i][tv.c] = -1;
            }
        } else if (dir == 2) {
            for (int i = tv.c - 1; i >= 0; i--) {
                if (arr[tv.r][i] == 6) {
                    break;
                }
 
                arr[tv.r][i] = -1;
            }
        } else { // dir == 3
            for (int i = tv.r + 1; i < n; i++) {
                if (arr[i][tv.c] == 6) {
                    break;
                }
 
                arr[i][tv.c] = -1;
            }
        }
    }
}