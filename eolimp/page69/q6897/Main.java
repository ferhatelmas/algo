package page69.q6897;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n;
    while((n = in.nextInt()) != 0)
      System.out.println(conjecture(n));
  }

  private static int conjecture(int n) {
    int c = 1;
    while(n != 1) {
      n = n % 2 == 0 ? n / 2 : 3 * n + 1;
      c++;
    }
    return c;
  }
}
