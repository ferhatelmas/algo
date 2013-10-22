package page3.q280;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(gcd(in.nextLong(), in.nextLong()));
  }

  private static long gcd(long a, long b) {
    return b == 0 ? a : gcd(b, a%b);
  }

}