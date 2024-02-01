import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Main {
	static int s,p;
	//{A,C,G,T}
	static int a,c,g,t;
	//문자열 N자리만큼 받아오기
	static int ans;
	static int[] cnt_acgt;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		s = Integer.parseInt(st.nextToken());
		p = Integer.parseInt(st.nextToken());

		String[] dna = br.readLine().split("");

		st = new StringTokenizer(br.readLine());

		a = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		g = Integer.parseInt(st.nextToken());
		t = Integer.parseInt(st.nextToken());

		ans = 0;
		cnt_acgt = new int[4];
		for(int i = 0; i < 4 ; i++) {
			cnt_acgt[i] = 0;
		}

		//맨 앞 p자리 문자열 받아오기
		for(int i = 0; i < p ; i++) {
			chk(dna[i]);
		}
		if(cnt_acgt[0] >= a && cnt_acgt[1] >= c && cnt_acgt[2] >= g && cnt_acgt[3] >= t) {
			ans+=1;
		}
		int idx=0;
		//다음 문자열들 체크
		for(int i = p; i < s ; i++,idx++) {
			if(dna[idx].equals("A")) {
				cnt_acgt[0] -=1;
			}else if(dna[idx].equals("C")) {
				cnt_acgt[1] -=1;
			}else if(dna[idx].equals("G")) {
				cnt_acgt[2] -=1;
			}else if(dna[idx].equals("T")) {
				cnt_acgt[3] -=1;
			}
			chk(dna[i]);
			if(cnt_acgt[0] >= a && cnt_acgt[1] >= c && cnt_acgt[2] >= g && cnt_acgt[3] >= t) {
				ans+=1;
			}
		}
		System.out.println(ans);

	}

	private static void chk(String s) {
		if(s.equals("A")) {
			cnt_acgt[0] +=1;
		}else if(s.equals("C")) {
			cnt_acgt[1] +=1;
		}else if(s.equals("G")) {
			cnt_acgt[2] +=1;
		}else if(s.equals("T")) {
			cnt_acgt[3] +=1;
		}

	}

}