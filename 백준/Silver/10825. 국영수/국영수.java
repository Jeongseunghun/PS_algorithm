import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

class Point implements Comparable<Point>{
    public String name;
    public int korean,english,math;

    Point(String name,int korean, int english, int math){
        this.korean = korean;
        this.english = english;
        this.math = math;
        this.name = name;
    }

    @Override
    public int compareTo(Point o) {
        if(this.korean == o.korean) {
            if (this.english == o.english) {
                if(this.math == o.math){
                    return this.name.compareTo(o.name);
                }
                return o.math - this.math;
            }
            return this.english - o.english;
        }
        return o.korean - this.korean;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        ArrayList<Point> arr = new ArrayList<Point>();
        for(int i = 0 ; i < N; i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int korean = Integer.parseInt(st.nextToken());
            int english = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());
            arr.add(new Point(name, korean,english,math));
        }

        Collections.sort(arr);

        for(Point a : arr){
            System.out.println(a.name);
        }
    }
}