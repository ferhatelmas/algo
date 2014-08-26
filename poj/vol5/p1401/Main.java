package vol5.p1401;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      int n = in.nextInt();

      int cnt = 0;
      while(n >= 5) {
        n /= 5;
        cnt += n;
      }
      System.out.println(cnt);
    }
  }

}
