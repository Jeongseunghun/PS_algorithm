import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> (Math.abs(o1) - Math.abs(o2)) == 0 ? o1 - o2 : (Math.abs(o1) - Math.abs(o2)));

	
		for(int i = 0 ; i < N ; i++) {
			int x = Integer.parseInt(br.readLine());
			
			if(x==0) {
				if(pq.isEmpty() == false) {
					System.out.println(pq.poll());
				}else {
					System.out.println(0);
				}
			}else {
				pq.offer(x);
				
			}
		}
		
	}

}