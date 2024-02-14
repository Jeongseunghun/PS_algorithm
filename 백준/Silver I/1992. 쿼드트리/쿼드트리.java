import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static int[][] image;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        image = new int[N][N];

        for(int i = 0; i < N; i++) {
            String str = br.readLine();

            for(int j = 0; j < N; j++) {
                image[i][j] = str.charAt(j) - '0';
            }
        }

        QuadTree(0, 0, N);
        System.out.println(sb);
    }

    public static void QuadTree(int x, int y, int size) {

        if(chk(x, y, size)) { 
            sb.append(image[x][y]);
            return;
        }

        int newSize = size / 2;	

        sb.append('(');

        QuadTree(x, y, newSize);						// 왼쪽 위
        QuadTree(x, y + newSize, newSize);				// 오른쪽 위
        QuadTree(x + newSize, y, newSize);				// 왼쪽 아래
        QuadTree(x + newSize, y + newSize, newSize);	// 오른쪽 아래

        sb.append(')');

    }
    public static boolean chk(int x, int y, int size) {
        int value = image[x][y];

        for(int i = x; i < x + size; i++) {
            for(int j = y; j < y + size; j++) {
                if(value != image[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}