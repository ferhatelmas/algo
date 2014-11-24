package page33.q3258;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        a = 0, b = 1;

    while(n-- > 1) {
      int t = b;
      b += a;
      a = t;
    }
    System.out.println(b);
  }
}
