
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import static java.lang.System.in;
import static java.lang.System.out;

public class Main {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));
      int input = Integer.parseInt(br.readLine());
      br.close();

      for(int i = 1 ; i <= input ; i++){
          for(int j = input-1 ; j >= i ; j--) {
              bw.write(" ");
          }
          for(int j = 1 ; j <= i ; j++){
              bw.write("*");
          }
          bw.newLine();
      }


      bw.flush();
      bw.close();
    }


}
