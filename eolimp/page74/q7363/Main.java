package page74.q7363;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(),
        c = in.nextInt(), d = in.nextInt();

    a = a*d + b*c;
    b *= d;
    if(a%b == 0)
      System.out.println(a / b);
    else {
      d = gcd(a, b);
      System.out.println(a/d + " " + b/d);
    }
  }

  private static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a%b);
  }
}
