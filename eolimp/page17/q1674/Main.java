package page17.q1674;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(),
        s = in.nextInt(), n = in.nextInt(), t;

    while(n-- > 0) {
      t = in.nextInt();
      s = t > 0 ? Math.min(s + t, b) : Math.max(s + t, a);
    }
    System.out.println(s);
  }
}
