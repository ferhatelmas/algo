package page17.q1602;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long a = in.nextLong(), b = in.nextLong();
    System.out.println((a*b) / gcd(Math.max(a, b), Math.min(a, b)));
  }

  private static long gcd(long a, long b) {
    return b == 0 ? a : gcd(b, a%b);
  }
}
