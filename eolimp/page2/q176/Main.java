package page2.q176;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    br.readLine();

    int max = 0, cnt = 0, n;
    String s = br.readLine();
    for(int i=0, l=s.length(), j; i<l;) {
      j = i;
      while(j < l && s.charAt(j) != ' ') j++;
      n = Integer.parseInt(s.substring(i, j));
      if(n > max) {
        max = n;
        cnt = 1;
      } else if(n == max) cnt++;
      i = j+1;
    }
    System.out.println(cnt);
  }
}
