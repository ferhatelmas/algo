package vol14.p2309;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k;

    while(n-- > 0) {
      k = in.nextInt();
      int p = k, c = 0;
      while(p%2 == 0) {
        p /= 2;
        c++;
      }
      p = (int)Math.pow(2, c);
      System.out.println((k-p+1) + " " + (k+p-1));
    }
  }
}
