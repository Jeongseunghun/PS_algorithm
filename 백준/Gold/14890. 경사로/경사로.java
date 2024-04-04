import java.util.Scanner;

public class Main {
    static int N;
    static int L;
    static int[][] street;
    static int cnt = 0;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        N = scanner.nextInt();
        L = scanner.nextInt();
        street = new int[N][N];
        
        // Inputting street
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                street[i][j] = scanner.nextInt();
            }
        }
        
        // Checking rows
        for (int i = 0; i < N; i++) {
            boolean[] slope = new boolean[N];
            if (check(getRow(i))) {
                cnt++;
            }
        }
        
        // Checking columns
        for (int j = 0; j < N; j++) {
            boolean[] slope = new boolean[N];
            if (check(getColumn(j))) {
                cnt++;
            }
        }
        
        System.out.println(cnt);
    }
    
    // Function to get a row from the street
    static int[] getRow(int rowIndex) {
        return street[rowIndex];
    }
    
    // Function to get a column from the street
    static int[] getColumn(int colIndex) {
        int[] column = new int[N];
        for (int i = 0; i < N; i++) {
            column[i] = street[i][colIndex];
        }
        return column;
    }
    
    // Function to check if the given line meets the conditions
    static boolean check(int[] line) {
        boolean[] slope = new boolean[N];
        for (int i = 1; i < N; i++) {
            // Difference between adjacent elements should not be greater than 1
            if (Math.abs(line[i] - line[i - 1]) > 1) {
                return false;
            }
            // When the next element is smaller
            if (line[i] < line[i - 1]) {
                for (int j = 0; j < L; j++) {
                    if (i + j >= N || line[i] != line[i + j] || slope[i + j]) {
                        return false;
                    }
                    slope[i + j] = true;
                }
            }
            // When the previous element is smaller
            else if (line[i] > line[i - 1]) {
                for (int j = 0; j < L; j++) {
                    if (i - j - 1 < 0 || line[i - 1] != line[i - j - 1] || slope[i - j - 1]) {
                        return false;
                    }
                    slope[i - j - 1] = true;
                }
            }
        }
        return true;
    }
}