package vol10.p1922;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n;

    while((n = in.nextInt()) != 0) {
      double d = Double.MAX_VALUE;
      while(n-- > 0) {
        int v = in.nextInt(), t = in.nextInt();
        if(t >= 0) {
          d = Math.min(d, 450.0 * 36 / v + t);
        }
      }
      System.out.println((int)Math.ceil(d));
    }
  }
}
