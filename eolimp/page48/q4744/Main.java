package page48.q4744;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt();
    System.out.println((a / gcd(a, b)) * b);
  }

  private static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a%b);
  }
}
