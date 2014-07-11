package page6.q566;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt(), m, n, s, r, c;

    while(t-- > 0) {
      s = 0; r = 0; m = in.nextInt(); n = in.nextInt();
      for(int i=1; i<=m; i++) {
          for (int j=1; j<=n; j++) {
            c = Math.max(m-i+1, 0) * Math.max(n-j+1, 0);

            if(i == j) s += c;
            else r += c;
          }
      }
      System.out.println(s + " " + r);
    }
  }
}
