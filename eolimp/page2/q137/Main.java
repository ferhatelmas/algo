package page2.q137;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), gcd;

    gcd=gcd(in.nextInt(), in.nextInt());
    for(int i=0; i<n-2; i++)
      gcd = gcd(gcd, in.nextInt());

    System.out.println(gcd);
  }

  private static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a%b);
  }
}