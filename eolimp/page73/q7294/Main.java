package page73.q7294;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long n = in.nextLong(), m = in.nextLong();
    System.out.println(n * m / gcd(n, m));
  }

  private static long gcd(long a, long b) {
    return b == 0 ? a : gcd(b, a%b);
  }
}
